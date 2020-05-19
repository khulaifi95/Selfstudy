# Reinforcement Learning



## Lecture 2: Markov Decision Processes

### 1. Introduction to MDPs

*Markov decision processes* formally describe an environment for RL.

- The environment is fully **observable**.
- i.e. the current state completely characterises the process.
- Almost all RL problems can be formalised as MDPs, e.g.
  - Optimal control $\rightarrow$ continuous MDP
  - Partialy observable problems $\rightarrow$ MDP
  - MDPs with one state $\rightarrow$ *bandit*



### 2. Markov property

> The future is independent of the past given the present.

A state $S_t$ is **Markov** *iff*
$$
\mathbb P[S_{t+1}|S_t]=\mathbb P[S_{t+1}|S_1,...,S_t]
$$

- The state captures all relevant information from the history.
- Once the state is known, the history may be thrown away.
- The state is a sufficient statistic of the future.



### 3. State transition matrix

For a **Markov** state $s$ and successor state $s'$, the *state transition probability* is defined by:
$$
\mathcal P_{ss'}=\mathbb P[S_{t+1}=s'|S_t=s]
$$
State transition matrix $\mathcal P$ defines transition probabilities from all states $s$ to all successor states $s'$.
$$
\mathcal P =  \ \ \begin{bmatrix} {  \mathcal P_{11} \ ... \ \mathcal P_{1n} \\ \vdots \ \ \ \ \ \ \ \ \ \ \ \ \ \ \vdots\\ \mathcal P_{n1} \ ... \ \mathcal P_{nn}} \end{bmatrix}
$$
where each row of the matrix sums to $1$, representing transition to all other states.



### 4. Markov process

A Markov process is a memoryless *random* process, i.e. a **sequence** of random states $S_1, S_2,...$ with the **Markov** property.

A Markov process/chain can be defined as a tuple $\left\langle \mathcal S, \mathcal P \right\rangle$:

- $\mathcal S$: a finite set of states
- $\mathcal P$: a state transition probability matrix, $\mathcal P_{ss'}=\mathbb P[S_{t+1}=s'|S_t=s]$



### 5. Markov reward process

A Markov reward process is a Markov chain with values as a tuple $\left\langle \mathcal {S,P, R,\gamma} \right\rangle$.

- $\mathcal R$: a reward function, $\mathcal R_s = \mathbb E[R_{t+1}|S_t =s]$
- $\gamma$: a discount factor, $\gamma \in [0,1]$



| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 2_MDP.assets/Screenshot 2020-05-19 at 10.22.33.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|       **Fig 2.1** Example of student MDP with rewards        |



### 6. Return

The return $G_t$ is the total **discounted** **reward** from time step $t$:
$$
G_t = R_{t+1} + \gamma R_{t+2}, +\gamma^2 R_{t+3}+... = \sum_{k=0}^\infty\gamma^kR_{t+k+1}
$$

- The discount $\gamma\in[0,1]$ is the present value of future rewards.
- The value of receiving reward $R$ after $k+1$ time steps is $\gamma^kR$.
- Values immediate reward above delayed reward.
  - $\gamma \rightarrow 0$ : myopic
  - $\gamma \rightarrow 1$ : far-sighted



##### Why discount?

1. Mathematically convenient to discount rewards.

2. Avoids infinite returns in **cyclic** Markov processes.

3. **Uncertainty** about the future may not be fully represented

4. If the reward is financial, immediate rewards may earn more interest than delayed rewards
5. Animal/human behaviour shows **preference** for immediate reward

It is sometimes possible to use *undiscounted* Markov reward processes (i.e. $γ$ = 1), e.g. if all sequences terminate.



### 7. Value function

The state value function $v(s)$ of an MRP is the long-term expected return starting from state $s$.
$$
v(s) = \mathbb E[G_t|S_t = s]
$$
where the measured **expectation** indicate a stochasitic process.



### 8. Bellman equation

The value function can be decomposed into two parts:

- immediate reward $R_{t+1}$
- discounted value of successor state $\gamma v(S_{t+1})$

$$
\begin{align}
v(s) &= \mathbb E[G_t|S_t=s]
\\ &= \mathbb E[R_{t+1}+\gamma R_{t+2}+\gamma^2 R_{t+3}+...|S_t=s]
\\ &= \mathbb E[R_{t+1}+\gamma(R_{t+2+\gamma R_{t+3}+...})|S_t=s]
\\ &= \mathbb E[R_{t+1}+\gamma G_{t+1}|S_t=s]
\\ &= \mathbb E[R_{t+1}+\gamma v(S_{t+1})|S_t=s]
\end{align}
$$

which can be interpreted as a one-step look ahead search, integrating the values of possible states.
$$
v(s)=\mathcal R_s+\gamma \sum_{s'\in\mathcal S}\mathcal P_{ss'}v(s')
$$


### 9. Bellman equation in matrix form

The Bellman equation can be expressed concisely using matrices:
$$
\mathbb v=\mathcal R + \gamma \mathcal P\mathbb v
$$
where $\mathbb v$ is a column vector with one entry per **state**
$$
\begin{bmatrix} v(1) \\ \vdots \\v(n)\end{bmatrix} = \begin{bmatrix} \mathcal R_1 \\ \vdots \\ \mathcal R_n\end{bmatrix} + \gamma \begin{bmatrix} \mathcal P_{11} \ \cdots \mathcal P_{1n} \\ \vdots \ \ \ \ \ \ \ \ \ \ \ \ \vdots \\ \mathcal P_{n1} \ \cdots \mathcal P_{nn} \end{bmatrix}\begin{bmatrix} v(1) \\ \vdots \\v(n)\end{bmatrix}
$$


### 10. Solving the Bellman equation

The Bellman equation is a linear equation and can be solved directly:
$$
\mathbb v = \mathcal R + \gamma \mathcal P\mathbb v \\
(I-\gamma\mathcal P)\mathbb v = \mathcal R \\
\mathbb v = (I-\gamma\mathcal P)^{-1}\mathcal R
$$

- Computational complexity is $O(n^3)$ for n states.
- Many iterative methods for large MRPs:
  - Dynamic programming
  - Monte-Carlo evaluation
  - Temporal-difference learning



### 11. Markov decision process

A Markov decision process is a Markov reward process with decisions. It is an environment in which all states are Markov. MDP is a tuple $\left\langle \mathcal {S,A,P, R,\gamma} \right\rangle$.

- $\mathcal A$: a finite set of actions
- $\mathcal P$: a state transition probability matrix, $\mathcal P_{ss'}^a=\mathbb P[S_{t+1}=s'|S_t=s, A_t=a]$

- $\mathcal R$: a reward function, $\mathcal R_s^a = \mathbb E[R_{t+1}|S_t =s, A_t=a]$



| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 2_MDP.assets/Screenshot 2020-05-19 at 11.37.56.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|              **Fig 2.2** Example of Student MDP              |



### 12. Policies

A policy $\pi$ is a distribution over actions given states
$$
\pi(a|s) = \mathbb P[A_t=a|S_t=s]
$$

- Policy fully defines the behaviour of an agent.
- MDP policies depend on the current state.
- Policies are *stationary* i.e. time-independent, $A_t \sim \pi(\cdot|S_t), \forall t>0$

Given an *MDP* $\mathcal {M=\left\langle S,A,P,R,\gamma\right\rangle}$ and a policy $\pi$, 

- the state sequence $S_1,S_2,...$ is a **Markov process** $\mathcal {\left\langle S,P^\pi \right\rangle}$.
- the state and reward sequence $S_1, R_2, S_2,...$ is a **Markov reward process** $\mathcal {\left\langle S,P^\pi \right\rangle}, R^\pi, \gamma$.
- where transition dynamics and the value function averaged over the policy.

$$
\mathcal P^\pi_{s,s'} = \sum_{a\in\mathcal A}\pi(a|s)\mathcal P^a_{ss'}
$$

$$
 \mathcal R_s^\pi = \sum_{a\in \mathcal A}\pi(a|s)\mathcal R_s^a
$$



### 13. Value function

The *state-value* function $v_\pi(s)$ of an MDP is the expected return strating from state $s$, and **following policy** $\pi$
$$
v_\pi(s)=\mathbb E_\pi[G_t|S_t=s]
$$
The *action-value* function $q_\pi(s,a)$ of an MDP is the expected return starting from state $s$, **taking action** $a$, and then following policy $\pi$
$$
q_\pi(s,a)=\mathbb E_\pi[G_t|S_t=s, A_t=a]
$$


### 14. Bellman expectation equation

The state-value function can be decomposed into immediate reward and discounted value of successor state,
$$
v_\pi(s)=\mathbb E_\pi[R_{t+1}+\gamma v_\pi(S_{t+1})|S_t=s]
$$
The action-value function can be similarly decomposed as
$$
q_\pi(s,a)=\mathbb E_\pi[R_{t+1}+\gamma q_\pi(S_{t+1}, A_{t+1})|S_t =s ,A_t=a]
$$


| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 2_MDP.assets/Screenshot 2020-05-19 at 12.25.59.png" style="zoom:50%;" /> | <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 2_MDP.assets/Screenshot 2020-05-19 at 12.26.06.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|         **Fig 2.3** Bellman expectation for $v_\pi$          |               Bellman expectation for $q_\pi$                |



By summing up the reward of taking possible actions given a state, we have the value of the current state $s$
$$
v_\pi(s) = \sum_{a\in \mathcal A}\pi(a|s)q_\pi(s,a)
$$
By summing up the possible state dynamics given taking an action, we have the value of taking the action $a$
$$
q_\pi(s,a) = \mathcal R_s^a+\gamma \sum_{s'\in \mathcal S}\mathcal P_{ss'}^av_\pi(s')
$$


| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 2_MDP.assets/Screenshot 2020-05-19 at 12.36.23.png" style="zoom:50%;" /> | <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 2_MDP.assets/Screenshot 2020-05-19 at 12.36.28.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|             **Fig 2.4** $v_\pi$ in the next step             |                   $q_\pi$ in the next step                   |



Recursion of the value in state $v_\pi$ with respect to itself:
$$
v_\pi(s) = \sum_{a\in \mathcal A}\pi(a|s)(\mathcal R_s^a+\gamma \sum_{s'\in \mathcal S}\mathcal P_{ss'}^av_\pi(s'))
$$
Recursion of the value of action $q_\pi$ with respect to itself:
$$
q_\pi(s,a)=\mathcal R_s^a+\gamma \sum_{s'\in \mathcal S}\mathcal P_{ss'}^a\sum_{a'\in \mathcal A}\pi(a'|s')q_\pi(s',a')
$$


### 15. Bellman expectation equation in matrix form

The Bellman expectation equation can be expressed concisely using the induced MRP
$$
v_\pi=\mathcal R^\pi +\gamma \mathcal P^\pi v_\pi
$$
with direct solution
$$
v_\pi = (I-\gamma \mathcal P^\pi)^{-1}\mathcal R^\pi
$$


### 16. Optimal value function

The optimal state-value function $v_*(s)$ is the maximum value function over all policies
$$
v_*(s) = \max_\pi v_\pi(s)
$$
The optimal action-value function $q_*(s,a)$ is the maximum action-value function over all policies
$$
q_*(s,a) = \max_\pi q_\pi(s,a)
$$

- specifies the best possible performance in the MDP
- MDP solved when we know the optimal value $q_*$



| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 2_MDP.assets/Screenshot 2020-05-19 at 13.08.20.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|    **Fig 2.5** Example for optimal action-value function     |



### 17. Optimal policy

Define a partial ordering over policies
$$
\pi \geq \pi' \ \text{if} \ v_\pi(s) \geq v_{\pi'}(s), \forall s
$$

##### Theorem:

For any Markov decision process,

- There exists an optimal policy $\pi_*$ that is better than or equal to all other policies, $\pi_*\geq \pi, \forall \pi$. Can be *multiple*.
- All optimal policies achieve the optimal *value function* 

$$
v_{\pi_*}(s)=v_*(s,a)
$$

- All optimal policies achieve the optimal action-value function

$$
q_{\pi_*}(s,a) = q_*(s,a)
$$



### 18. Finding an optimal policy

An optimal policy can be found by maximising over $q_*(s,a)$,
$$
\pi_*(a|s) = \cases {1 & if a = argmax q*(s,a) \\ 0 & otherwise}
$$

- There is always a deterministic optimal policy for any MDP.
- If we know $q_*(s,a)$, we immediately have the optimal policy.



### 19. Bellman optimality equation

The optimal value functions are recursively related by the Bellman optimality equations:
$$
v_*(s) = \max_a q_*(s,a)
$$

$$
q_*(s,a) = \mathcal R_s^a+\gamma \sum_{s'\in\mathcal S}\mathcal P_{ss'}^av_*(s')
$$

Combine the two steps:
$$
v_*(s) = \max_a\mathcal R_s^a+\gamma\sum_{s'\in\mathcal S}\mathcal P_{ss'}^av_*(s')
$$

$$
q_*(s,a) = \mathcal R_s^a+\gamma \sum_{s'\in \mathcal S}\mathcal P_{ss'}^a\max_{a'}q_*(s',a')
$$



| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 2_MDP.assets/Screenshot 2020-05-19 at 13.28.40.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
| **Fig 2.6** Example of Bellman optimality equation in student MDP |



### 20. Solving the Bellman optimality equation

Bellman optimality equation is non-linear, in general, no closed form solution.

- value iteration
- policy iteration
- Q-learning
- Sarsa



### @Extensions to MDPs

