# Reinforcement Learning



## Lecture 5: Model-free Control



### 1. Introduction

#### 1.1 Model-free reinforcement learning

Model-free prediction:

- Estimate the value function of an *unknown* MDP.

Model-free control:

- **Optimise** the value function of an *unknown* MDP.



#### 1.2 Uses of model-free control

Some example problems that can be modelled as MDPs:

- Elevator
- Parking
- Portfolio management
- Logistics

For most of these problems, either:

- MDP model is unknown, but experience can be sampled.
- MDP model is known, but is too big to use, except by sampling.

Model-free control can solve these problems.



#### 1.3 On and off-policy learning

On-policy learning learns on the job.

- Learn about policy $\pi$ from experience sampled from $\pi$.

Off-policy learning looks over someone's shoulder.

- Learn about policy $\pi$ from experience sampled from $\mu$.



### 2. On-policy Monte-Carlo control

#### 2.1 Generalised policy iteration with MC evaluation



| <img src="Lecture 5_MC_TD_2.assets/Screenshot 2020-06-25 at 08.26.45.png" style="zoom:50%;" /> | <img src="Lecture 5_MC_TD_2.assets/Screenshot 2020-06-25 at 08.27.01.png" style="zoom:60%;" /> |
| -----------------------------------------------------------: | :----------------------------------------------------------- |
|                     **Fig 5.1** Generalised policy iteration | with Monte-Carlo evaluation                                  |

- Policy evaluation: Monte-Carlo policy evaluation, $Q=q_\pi$.

- Policy improvement: $\epsilon$-greedy policy improvement.



#### 2.2 Model-free policy iteration using action-value function

Greedy policy improvement over $V(s)$ requires dynamics of MDP:
$$
\pi'(s)=\arg\max_{a\in\mathcal A} \mathcal R_s^a+\mathcal P_{ss'}^aV(s')
$$
Greedy policy improvement over **action-value function** $Q(s,a)$ is model-free:
$$
\pi'(s) = \arg\max_{a\in\mathcal A} Q(s,a)
$$
Thus we use Monte-Carlo action-value function $Q(s,a)$ for policy evaluation.



#### 2.3 $\epsilon$-Greedy exploration

The simplest idea for ensuring continual exploration is to use $\epsilon$-greedy.

It ensures all *m* actions are tried with non-zero probability.

- With probability $1-\epsilon$, choose the **greedy** action.
- With probability $\epsilon$, choose an action at **random**.

$$
\pi(a|s)=\cases {\epsilon/m+1-\epsilon & if a*=argmax Q(s,a) \\ \epsilon/m  &\text{otherwise}}
$$



#### 2.4 $\epsilon$-Greedy policy improvement

**Theorem**:

For any $\epsilon$-greedy policy $\pi$, the $\epsilon$-greedy policy $\pi'$ with respect to $q_\pi$ is an improvement, $v_{\pi'}(s)\geq v_\pi(s)$.

**Proof**:
$$
\begin{align} q_\pi(s,\pi'(s)) &= \sum_{a\in\mathcal A}\pi'(a|s)q_\pi(s,a) \\&=\epsilon/m\sum_{a\in\mathcal A}q_\pi(s,a) + (1-\epsilon)\max_{a\in\mathcal A}q_\pi(s,a) \\&\geq \epsilon/m\sum_{a\in\mathcal A}q_\pi(s,a) + (1-\epsilon)\sum_{a\in\mathcal A} \frac{\pi(a|s)-\epsilon/m}{1-\epsilon}q_\pi(s,a) \\&=\sum_{a\in\mathcal A}\pi(a|s)q_\pi(s,a)=v_\pi(s) \end{align}
$$
Therefore from policy improvement theorem, we have $v_{\pi'}(s)\geq v_\pi(s)$.



#### 2.5 Monte-Carlo control

In **every episode**:

- Policy evaluation: Monte-Carlo policy evaluation, $Q=q_\pi$.

- Policy improvement: $\epsilon$-greedy policy improvement.

We immediately update the policy after episode.



| <img src="Lecture 5_MC_TD_2.assets/Screenshot 2020-06-25 at 09.33.40.png" style="zoom:67%;" /> |
| :----------------------------------------------------------: |
|           **Fig 5.2** Monte-Carlo policy iteration           |



#### 2.6 GLIE

To balance the exploration and exploitation, we utilise the Greedy in the Limit with Infinite Exploration.

We need to ensure:

- **All** state-action pairs are **explored** infinitely many times:

$$
\lim_{k\rarr\infty}N_k(s,a)=\infty
$$

- The policy **converges** on a greedy policy:

$$
\lim_{k\rarr \infty}\pi_k(a|s)=\mathbf 1(a=\arg\max_{a'\in\mathcal A}Q_k(s,a'))
$$

- Simple example of GLIE is to decay $\epsilon$ to zero at $\epsilon_k=\frac1k$ in an $\epsilon$-greedy policy.



#### 2.7 GLIE Monte-Carlo control

**Algorithm**:

1. Sample *k* episodes using $\pi$: $\{S_1,A_1, R_2,...,S_T\}\sim\pi$.

2. For each state $S_t$ and action $A_t$ in the episode, evaluate:

$$
N(S_t,A_t)\larr N(S_t,A_t)+1 \\ Q(S_t,A_t)\larr Q(S_t,A_t)+\frac 1{N(S_t,A_t)}(G_t-Q(S_t,A_t))
$$

3. Improve policy based on new action-value function

$$
\epsilon \larr 1/k \\ \pi \larr \epsilon\text{-greedy}(Q)
$$

**Theorem**:

GLIE Monte-Carlo control **converges** to the optimal action-value function, $Q(s,a)\rarr q_*(s,a)$.



### 3. On-policy temporal-difference learning

#### 3.1 MC vs. TD control

Temporal-difference learning has several advantages over Monte-Carlo:

- Lower variance.
- Online update.
- Incomplete sequences.

Natural idea: use TD instead of MC in control loop.

- Apply TD to estimate $Q(s,a)$.
- Use $\epsilon$-greedy policy improvement.
- Update every **time-step**.



#### 3.2 Sarsa

Update the action-value function:

| <img src="Lecture 5_MC_TD_2.assets/Screenshot 2020-06-25 at 10.59.13.png" style="zoom:67%;" /> |
| :----------------------------------------------------------: |
|    $Q(S,A)\larr Q(S,A)+\alpha(R+\gamma Q(S',A')-Q(S,A))$     |
|     **Fig 5.3** Update action-value function with Sarsa      |



#### 3.3 On-policy control with Sarsa

At every **time step**:

- Policy evaluation: Sarsa, $Q\approx q_\pi$.
- Policy improvement: $\epsilon$-greedy policy improvement.

We update the value function after **one step** of Sarsa.

The policy is implicitly represented by the Q value.

| <img src="Lecture 5_MC_TD_2.assets/Screenshot 2020-06-25 at 11.02.23.png" style="zoom:67%;" /> |
| :----------------------------------------------------------: |
|           **Fig 5.4** On-policy control with Sarsa           |



#### 3.4 Sarsa

**Sarsa algorithm for on-policy control**:

> **Initialise** $Q(s,a), \forall s\in\mathcal S, a\in \mathcal A(s)$ arbitrarily, and $Q(terminalstate,\cdot)=0$
> **Repeat** (for each episode):
> 		Initialise $S$
> 		Choose $A$ from $S$ using policy derived from $Q$ (e.g. $\epsilon$-greedy) 
> 		**Repeat** (for each step of episode): 
> 				Take action $A$, observe $R,S'$
> 				Choose $A'$ from $S'$ using policy derived from $Q$ (e.g. $\epsilon$-greedy)
> 				$Q(S,A)\larr Q(S,A)+\alpha(R+\gamma Q(S',A')-Q(S,A))$
> 				$S\larr S'; A\larr A'$
> 		**Until** $S$ is terminal



#### 3.5 Convergence of Sarsa

Sarsa converges to the optimal action-value function, $Q(s,a)\rarr q_*(s,a)$, under the following conditions:

1. GLIE sequence of policies $\pi_t(a|s)$.

2. Robbin-Monro sequence of **step-sizes** $\alpha_t$

$$
\sum_{t=1}^\infty \alpha_t=\infty \\ \sum_{t=1}^\infty\alpha_t^2<\infty
$$



#### 3.6 n-Step Sarsa

Consider the following *n*-step returns for $n=1,2,\infty$:

- $n=1 \ (Sarsa):q_t^{(1)}=R_{t+1}+\gamma Q(S_{t+1})$ 
- $n=2:q_t^{(2)}=R_{t+1}+\gamma R_{t+2}+\gamma^2Q(S_{t+2})$
- $n=\infty \ (MC): q_t^{(\infty)}=R_{t+1}+\gamma R_{t+2}+...+\gamma^{T-1}R_T$

Define the *n*-step Q-return:
$$
q_t^{(n)} = R_{t+1}+\gamma R_{t+2}+...+\gamma^{n-1}R_{t+n}+\gamma^nQ(S_{t+n})
$$
*n*-Step Sarsa updates $Q(s,a)$ towards the *n*-step Q-return:
$$
Q(S_t,A_t)\larr Q(S_t,A_t)+\alpha(q_t^{(n)}- Q(S_t,A_t))
$$



#### 3.7 Forward-view Sarsa($\lambda$)

The $q^\lambda$ return combines all *n*-step Q-returns $q_t^{(n)}$:
$$
q_t^\lambda=(1-\lambda)\sum_{n=1}^\infty\lambda^{n-1}q_t^{(n)}
$$
where $(1-\lambda)\lambda^{n-1}$ is the weight for each $\lambda$-return.

Forward-view Sarsa($\lambda$) updates $Q(s,a)$ towards the $q^\lambda$ return:
$$
Q(S_t,A_t)\larr Q(S_t,A_t)+\alpha(q_t^\lambda- Q(S_t,A_t))
$$



#### 3.8 Backward-view Sarsa($\lambda$)

Just like TD($\lambda$), we use **eligibility trace** in an online algorithm.

- Sarsa($\lambda$) has one eligibility trace for **each** state-action **pair**:

$$
E_0(s,a)=0 \\ E_t(s,a)=\gamma\lambda E_{t-1}(s,a)+\mathbf 1(S_t=s,A_t=a)
$$

- $Q(s,a)$ is updated for every state *s* and action *a*.
- In proportion to TD-error $\delta_t$ and eligibility trace $E_t(s,a)$:

$$
\delta_t=R_{t+1}+\gamma Q(S_{t+1},A_{t+1})-Q(S_t,A_t) \\ Q(s,a)\larr Q(s,a) + \alpha\delta_tE_t(s,a)
$$



#### 3.9 Sarsa($\lambda$)

**Sarsa($\lambda$) algorithm with eligibility trace**:

> **Initialise** $Q(s,a), \forall s\in\mathcal S, a\in \mathcal A(s)$ arbitrarily
>
> **Repeat** (for each episode):
>
> ​		$E(s,a)=0, \forall s\in\mathcal S, a\in \mathcal A(s)$
>
> ​		Initialise S,A
>
> ​		**Repeat** (for each step of episode):
>
> ​				Take action $A$, observe $R,S'$
>
> ​				Choose $A'$ from $S'$ using policy derived from $Q$ (e.g. $\epsilon$-greedy)
>
> ​				$\delta \larr R+\gamma Q(S',A')-Q(S,A)$
>
> ​				$E(S,A)\larr E(S,A)+1$
>
> ​				For all $s\in\mathcal S, a\in \mathcal A(s)$:
>
> ​						$Q(s,a)\larr Q(s,a)+\alpha\delta E(s,a)$
>
> ​						$E(s,a) \larr \gamma\lambda E(s,a)$
>
> ​				$S\larr S';A\larr A'$
>
> ​		**Until** $S$ is terminal



#### 3.10 Sarsa($\lambda$) Gridworld

|                    Action values increased by one-step Sarsa | Action values increased by Sarsa($\lambda$) with $\lambda=0.9$ |
| -----------------------------------------------------------: | :----------------------------------------------------------- |
| <img src="Lecture 5_MC_TD_2.assets/Screenshot 2020-06-25 at 12.44.14.png" style="zoom:67%;" /> | <img src="Lecture 5_MC_TD_2.assets/Screenshot 2020-06-25 at 12.44.19.png" style="zoom:67%;" /> |
|                                        **Fig 5.5** Gridworld | Sarsa($\lambda$) example                                     |

- At the end of episode, the values on the path are updated by the eligibility trace once reward is gain.

- At each step in the episode, the values are updated but unchanged since not seeing the final reward.



### 4. Off-policy learning

#### 4.1 Why is off-policy learning important?

In off-policy learning, we

- Evaluate **target policy** $\pi(a|s)$ to compute $v_\pi(s)$ or $q_\pi(s,a)$.

- While following **behaviour policy** $\mu(a|s)$.

It is important when:

- Learn from **observing** humans or other agents.
- **Re-use** experience generated from old policies $\pi_1, \pi_2,...,\pi_{t-1}$.
- Learn about **optimal** policy while following **exploratory** policy.
- Learn about **multiple** policies while following *one* policy.



#### 4.2 Importance sampling

We can estimate the expectation of a different distribution by:
$$
\begin{align}\mathbb E_{X\sim P}[f(X)]&=\sum P(X)f(X) \\&=\sum Q(X)\frac{P(X)}{Q(X)}f(X) \\&=\mathbb E_{X\sim Q}[\frac{P(X)}{Q(X)}f(X)]\end{align}
$$



#### 4.3 Importance sampling for off-policy MC

We use returns generated from $\mu$ to evaluate $\pi$.

- Weight return $G_t$ according to **similarity** between policies.
- Multiply importance sampling corrections along entire trajectory of **whole episode**:

$$
G_t^{\pi/\mu}=\frac{\pi(A_t|S_t)\pi(A_{t+1}|S_{t+1})}{\mu(A_t|S_t)\mu(A_{t+1}|S_{t+1})}\cdots\frac{\pi(A_t|S_T)}{\mu(A_T|S_T)}\cdot G_t
$$

- Update value towards **corrected** return

$$
V(S_t)\larr V(S_t)+\alpha(G_t^{\pi/\mu}-V(S_t))
$$

Monte-Carlo is **bad** with off-policy learning because of too high variance by multiple importance sampling.



#### 4.4 Importance sampling for off-policy TD

We use TD targets generated from $\mu$ to evaluate $\mu$.

- Weight TD target $R+\gamma V(S')$ by importance sampling.
- Only need a **single** importance sampling correction:

$$
V(S_t) \larr V(S_t)+\alpha(\frac{\pi(A_t|S_t)}{\mu(A_t|S_t)}(R_{t+1}+\gamma V(S_{t+1}))-V(S_t))
$$

Temporal-difference has much **lower variance** than Monte-Carlo importance sampling.

- Policies only need to be similar over a **single** step.



#### 4.5 Q-learning

We now consider off-policy learning of action-values $Q(s,a)$.

- **No** importance sampling is required.
- Next action is chosen using policy **behaviour** policy $A_{t+1}\sim \mu(\cdot|S_t)$.
- But we consider **alternative** successor action $A'\sim\pi(\cdot|S_t)$.
- Update $Q(S_t,A_t)$ towards value of alternative action:

$$
Q(S_t,A_t)\larr Q(S_t,A_t)+\alpha(R_{t+1}+\gamma Q(S_{t+1},A')-Q(S_t,A_t))
$$



#### 4.6 Off-policy control with Q-learning

We now allow both behaviour and target policies to **improve**.

- The target policy $\pi$ is **greedy** *w.r.t.* $Q(s,a)$

$$
\pi(S_{t+1})=\arg\max_{a'}Q(S_{t+1},a')
$$

- The behaviour policy $\mu$ is e.g. $\epsilon$-greedy *w.r.t.* $Q(s,a)$.
- The Q-learning target then simplifies:

$$
\begin{align}&R_{t+1}+\gamma Q(S_{t+1},A') \\=&R_{t+1}+\gamma Q(S_{t+1}, \arg\max_{a'}Q(S_{t+1},a')) \\=&R_{t+1}+\max_{a'}\gamma Q(S_{t+1},a') \end{align}
$$



#### 4.7 Q-learning control algorithm

| <img src="Lecture 5_MC_TD_2.assets/Screenshot 2020-06-25 at 13.48.01.png" style="zoom:80%;" /> |
| :----------------------------------------------------------: |
| $Q(S,A)\larr Q(S,A)+\alpha(R+\gamma \max\limits_{a'}Q(S',a')-Q(S,A))$ |
|           **Fig 5.6** Q-learning control algorithm           |



**Theorem**:

Q-learning control converges to the optimal action-value function, $Q(s,a)\rarr q_*(s,a)$.

**Q-learning (SARSAMAX)**:

> **Initialise** $Q(s,a) \forall s\in\mathcal S, a\in\mathcal A(s)$ arbitrarily, and $Q(terminalstate,\cdot)=0$
>
> **Repeat** (for each episode):
>
> ​		Initialise $S$
>
> ​		**Repeat** (for each step of episode):
>
> ​				Choose $A$ from $S$ using policy derived from $Q$ e.g. $\epsilon$-greedy
>
> ​				Take action $A$, observe $R,S'$
>
> ​				$Q(S,A)\larr Q(S,A)+\alpha[R+\gamma \max\limits_aQ(S',a)-Q(S,A)]$
>
> ​				$S\larr S'$
>
> ​		**Until** $S$ is terminal



### 5. Summary

#### 5.1 Relationship between DP and TD

|                                           |                       Full backup (DP)                       |                      Sample backup (TD)                      |
| :---------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|  Bellman expectation equation $v_\pi(s)$  | <img src="Lecture 5_MC_TD_2.assets/Screenshot 2020-06-25 at 14.04.09.png" style="zoom:67%;" /> | <img src="Lecture 5_MC_TD_2.assets/Screenshot 2020-06-25 at 14.04.50.png" style="zoom:67%;" /> |
|                                           |                 Iterative policy evaluation                  |                         TD learning                          |
| Bellman expectation equation $q_\pi(s,a)$ | <img src="Lecture 5_MC_TD_2.assets/Screenshot 2020-06-25 at 14.04.21.png" style="zoom:67%;" /> | <img src="Lecture 5_MC_TD_2.assets/Screenshot 2020-06-25 at 14.04.58.png" style="zoom:67%;" /> |
|                                           |                      Q-policy iteration                      |                            Sarsa                             |
|  Bellman optimality equation $q_*(s,a)$   | <img src="Lecture 5_MC_TD_2.assets/Screenshot 2020-06-25 at 14.04.34.png" style="zoom:67%;" /> | <img src="Lecture 5_MC_TD_2.assets/Screenshot 2020-06-25 at 14.05.10.png" style="zoom:67%;" /> |
|                                           |                      Q-value iteration                       |                          Q-learning                          |
|                                           |             **Fig 5.7** Relationship of DP & TD              |                                                              |



#### 5.2 Update rules of DP and TD

| Full backup (DP)                                             | Sample backup (TD)                                           |
| :----------------------------------------------------------- | ------------------------------------------------------------ |
| Iterative Policy Evaluation:                                 | TD Learning:                                                 |
| $V(s)\larr \mathbb E[R+\gamma V(S')|s]$                      | $V(S)\xleftarrow{a}R+\gamma V(S')$                           |
| Q-Policy Iteration:                                          | Sarsa:                                                       |
| $Q(s,a)\larr \mathbb E[R+\gamma Q(S',A')|s,a]$               | $Q(S,A)\xleftarrow{a}R+\gamma Q(S',A')$                      |
| Q-Value Iteration:                                           | Q-Learning:                                                  |
| $Q(s,a)\larr \mathbb E[R+\gamma \max\limits_{a'\in\mathcal A}Q(S',a')|s,a]$ | $Q(S,A)\xleftarrow{a}R+\gamma \max\limits_{a'\in\mathcal A}Q(S',a')$ |

