# Reinforcement Learning



## Lecture 9: Exploration and Exploitation



### 1. Introduction

#### 1.1 Exploration vs. exploitation dilemma

Online decision-making involves a fundamental choice:

- Exploitation: make the best decision given current information.
- Exploration: gather more information.

It is shown that:

1. The best long-term strategy may involve short-term sacrifices.
2. Gather enought information to make the bset overall decisions.



#### 1.2 Examples

| Decision process      | Exploitation                  | Exploration             |
| --------------------- | ----------------------------- | ----------------------- |
| Restaurant selection  | Go to the favourite one.      | Try a new restaurant.   |
| Online advertisements | Show the most successful ad.  | Change to different ad. |
| Oil drilling          | Drill at the best known pos.  | Try a new location.     |
| Game playing          | Play the best move you think. | Play experimental move. |



#### 1.3 Principles

- Naive exploration:
  - Add noise to greedy policy, e.g. $\epsilon$-greedy.
- Optimistic initialisation:
  - Assume the best until proven otherwise.
- Optimism in the face of uncertainty:
  - Prefer actions with uncertain values.
- Probability matching:
  - Select actions according to probability that they are the best.
- Information state search:
  - Lookahead search incorporating value of information.



### 2. Multi-armed bandits

#### 2.1 Bandit

A multi-armed bandit is a tuple $\left\langle \mathcal{A,R}\right\rangle $.

- $\mathcal A$ is a known set of $m$ actions i.e. arms.
- $\mathcal R^a(r)=\mathbb P[r|a]$ is an unknown probability distribution over rewards.
- At each step $t$, the agent selects an action $a_t\in\mathcal A$.
- The environment generates a reward $r_t\sim \mathcal R^{a_t}$.

The goal is to maximise **cumulative reward** $\sum_{\tau=1}^t r_\tau$.



#### 2.2 Regret

- The action-value is the mean reward for action *a*:

$$
Q(a) = \mathbb E[r|a]
$$

- The optimal value $V^*$ is given as:

$$
V^*=Q^*(a) = \max_{a\in\mathcal A}Q(a)
$$

- The **regret** is the opportunity loss for one step:

$$
l_t = \mathbb E[V^*-Q(a_t)]
$$

- The total regret is the total oppotunity loss:

$$
L_t = \mathbb E[\sum_{\tau=1}^tV^*-Q(a_\tau)]
$$

Thus the goal of maximising cumulative reward $≡$ **minimising total regret**.



#### 2.3 Counting regret

The count $N_t(a)$ is the expected number of selections for action *a*.

- Gap $\Delta_a$ is the difference in value between action *a* and optimal action $a^*$:

$$
\Delta_a = V^*-Q(a)
$$

- Regret can be formulated as a function of gaps and the counts:

$$
\begin{align}L_t &= \mathbb E[\sum_{\tau=1}^tV^*-Q(a_\tau)] \\ &= \sum_{a\in\mathcal A} \mathbb E[N_t(a)](V^*-Q(a)) \\ &= \sum_{a\in\mathcal A}\mathbb E[N_t(a)]\Delta_a \end{align}
$$

- A good algorithm needs small counts for large gaps.

- The problem is that gaps are not known.



#### 2.4 Linear or sublinear regret

- If an algorithm **forever** explores, it will have linear total regret.
- If an algorithm **never** explores, it will have linear total regret.
- We need to find method to achieve sublinear total regret.



#### 2.5 Greedy algorithm

We consider algorithms that estimate $\hat Q_t(a)\approx Q(a)$.

- Estimate the value of each action by Monte-Carlo evaluation:

$$
\hat Q_t(a)=\frac1{N_t(a)}\sum_{t=1}^Tr_t\mathbf 1(a_t=a)
$$

- The **greedy** algorithm always selects action with highest value:

$$
a^*_t = \arg\max_{a\in\mathcal A} \hat Q_t(a)
$$

- Being greedy can lock onto a suboptimal action forever.

Greedy has linear total regret.



#### 2.6 $\epsilon$-Greedy algorithm

The $\epsilon$-greedy algorithm continues to explore forever.

- With probability $1-\epsilon$, select the best action $a=\arg\max_{a\in\mathcal A}\hat Q(a)$.
- With probability $\epsilon$, select a **random** action.

Constant $\epsilon$ ensures minimum regret:
$$
l_t\geq \frac\epsilon{\mathcal A}\sum_{a\in\mathcal A}\Delta_a
$$

- $\epsilon$-greedy has **linear** total regret.



#### 2.7 Optimistic initialisation

A simple and practical idea is to initialise action-value at **high**.

- Update $Q(a)$ by incremental Monte-Carlo evaluation:

$$
\hat Q_t(a_t) = \hat Q_{t-1}+\frac1{N_t(a_t)}(r_t-\hat Q_{t-1})
$$

In practice, $\epsilon$-greedy with optimistic initialisation has very good performance overall.

- It encourages systematic exploration early on.
- But it can still lock onto suboptimal action.
- $\epsilon$-greedy + optimistic initialisahastion has **linear** total regret.



#### 2.8 Decaying $\epsilon_t$-greedy algorithm

We can pick a decay schedule for $\epsilon$ at different time-steps.

Consider the following schedule:
$$
c>0 \\ d = \min_{a|\Delta_a>0} \Delta_i \\ \epsilon_t = \min\Big\{1, \frac{c|\mathcal A|}{d^2t}\Big\}
$$
where $c$ is the step-size parameter, $d$ is the minimum gap for all actions.

- Decaying $\epsilon_t$-greedy has **logarithmic** asymptotic total regret.
- However, this schedule requires prior knowledge of gaps.

**Goal**: The realistic one is to find an algorithm with **sublinear** regret for any multi-armed bandit without knowledge of $\mathcal R$.



#### 2.9 Lower bound

The optimal total regret has a lower bound at **logarithmic** level.

- The performance of algorithms is determined by **similarity** between optimal arm and other arms.
- Hard problems have similar-looking arms with different means.
- Need to correlate the similarity to the gap to distinguish the optimal arm.



**Theorem**: (*Lai and Robbins*)

Asymptotic total regret is at least logarithmic in number of steps.
$$
\lim_{t\to\infty}L_t\geq\log t\sum_{a|\Delta_a>0}\frac{\Delta_a}{KL(\mathcal R^a||\mathcal R^a_*)}
$$
where $KL(\mathcal R^a||\mathcal R^a_*)$ is the KL-divergence describing the similarity of distributions
$$
{KL}(p||q)=\int p\log\frac{p}{q}
$$



#### 2.10 Optimism in the face of uncertainty

We are often in the face of actions with different uncertainties.

The more uncertain we are about an action-value:

- The more important it is to explore that action.

- The more likely to pick another action afterwards.

Until the best action.



| <img src="Lecture 9_Exploration.assets/Screenshot 2020-07-09 at 03.08.20.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|       **Fig 9.1** Optimism in the face of uncertainty        |



#### 2.11 Upper confidence bounds

We estimate an upper confidence bound $\hat U_t(a)$ for each action-value, such that with high probability:
$$
Q(a)\leq \hat Q_t(a)+\hat U_t(a)
$$
The UCB depends on the number of times $N(a)$ that an action has been selected.

- Small $N_t(a)\rarr \hat U_t(a)$ large, i.e. estimate is uncertain.
- Large $N_t(a)\rarr \hat U_t(a)$ small, i.e. estimate is accurate.

Select action maximising the **upper confidence bound**:
$$
a_t = \arg\max_{a\in\mathcal A}\hat Q_t(a)+\hat U_t(a)
$$
**Theorem**: (*Hoeffding's inequality*)

Let $X_1,...,X_t$ be *i.i.d.* random variables $\in [0,1]$, and let $\bar X_t=\frac1\tau\sum_{\tau=1}^tX_\tau$ be the sample mean. Then:
$$
\mathbb P[\mathbb E[X]>\bar X_t+u]\leq e^{-2tu^2}
$$
We can apply Hoeffding's inequality to UCB conditioned on selecting action *a*:
$$
\mathbb P[Q(a)>\hat Q_t(a)+U_t(a)]\leq e^{-2N_t(a)U_t(a)^2}
$$
*l.h.s* is the probability *p* that true value exceeds UCB and solve for $U_t(a)$:
$$
p = e^{-2N_t(a)U_t(a)^2} \\ U_t(a) = \sqrt{\frac{-\log p}{2N_t(a)}}
$$


#### 2.12 UCB1

The probability that true value exceeds UCB is reduced $\darr$ as more rewards $\uarr$ are observed, e.g. take $p=t^{-4}$. We have:
$$
U_t(a) = \sqrt{\frac{2\log t}{N_t(a)}}
$$
It gives the **UCB1** algorithm:
$$
a_t = \arg\max_{a\in\mathcal A}Q(a)+\sqrt{\frac{2\log t}{N_t(a)}}
$$
The UCB algorithm achieves **logarithmic** asymptotic total regret
$$
\lim_{t\to\infty}L_t\leq 8\log t\sum_{a|\Delta_a>0}\Delta_a
$$


#### 2.13 Bayesian bandits

The methods so far make no assumption about the **reward distribution** $\mathcal R$ except bounds on rewards.

**Bayesian bandits** exploit prior knowledge of rewards $p[\mathcal R]$.

- Compute posterior distribution of rewards $p[\mathcal R|h_t]$ given history of actions and rewards.
- Use posterior to guide exploration:
  - Upper confidence bound. (Batesian UCB)
  - Probability matching. (Thompson sampling)
- It returns better performance if prior knowledge is accurate.



#### 2.14 Bayesian UCB

Consider an example of Bayesian UCB with independent Gaussians.



| <img src="Lecture 9_Exploration.assets/Screenshot 2020-07-09 at 04.01.20.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|         **Fig 9.2** Gaussian distribution of rewards         |

- We assume reward distribution is Gaussian, i.e.

$$
\mathcal R_a(r)=\mathcal N(r;\mu_a,\sigma_a^2)
$$

- Compute Gaussian posterior over $\mu_a, \sigma_a^2$ by Bayes' rule:

$$
p[\mu_a,\sigma_a^2|h_t] \propto p[\mu_a,\sigma_a^2]\prod_{t|a_t=a} \mathcal N(r_t;\mu_a, \sigma_a^2)
$$

- Pick action that maximises **standard error** of $Q(a)$

$$
a_t = \arg\max_{a\in\mathcal A} \mu_a+c\sigma_a/\sqrt{N(a)}
$$



#### 2.15 Probability matching

Probability matching selects action *a* according to probability that *a* is optimal
$$
\pi(a|h_t) = \mathbb P[Q(a)>Q(a'),\forall a' \neq a|h_t]
$$

- Probability matching is **optimistic** in the face of uncertainty.
- **Uncertain** actions have higher probability of being max.
- Difficult to compute **analytically** from posterior.



#### 2.16 Thompson sampling

Thompson sampling is the oldest implementation of probability matching
$$
\pi(a|h_t) = \mathbb P[Q(a)>Q(a'),\forall a' \neq a|h_t] \\ = \mathbb E_{\mathcal R|h_t}[\mathbf 1(a=\arg\max_{a\in\mathcal A}Q(a))]
$$

- **Sample** a reward distribution $\mathcal R$ from posterior for each action.
- Compute action-value function $Q(a)=\mathbb E[\mathcal R_a]$.
- Select action maximising value on sample $a_t = \arg\max_{a\in\mathcal A} Q(a)$.

For Bernoulli bandits, Thompson sampling achieves *Lai and Robbins* lower bound.



#### 2.17 Value of information

Exploration is useful because it gains information. Can we quantify its value?

- The **amount** of reward to pay for information.
- **Long-term** reward after gaining information vs. *immediate* reward.

Information gain is higher in **uncertain** situations.

- It makes sense to explore uncertain situations more.
- We can trade-off exploration and exploitation optimally if know its value.



#### 2.18 Information state space

We can also view bandits in **sequential** decision-making problems.

- At each step, there is an **information state** $\tilde s$:
  - A statistic of the **history**, i.e. $\tilde s = f(h_t)$.
  - Summarises all information accumulated so far.
- Each action *a* causes a transition to a new information space $\tilde s'$:
  - By adding new information.
  - With transition probability $\tilde {\mathcal P}_{\tilde s, \tilde s'}^a$.

- This defines MDP $\tilde {\mathcal M}$ in **augmented** information state space

$$
\tilde{\mathcal M} = \left\langle \mathcal{\tilde S,A,\tilde P, R,\gamma}\right\rangle
$$



#### 2.19 Solving information state search

We now have an **infinite** MDP over information states.

This MDP can be solved by reinforcement learning.

- Model-free RL:
  - e.g. Q-learning.
- Bayesian model-based RL:
  - e.g. Gittins indices(DP) $\rarr$ apply simulation-based search.
  - AKA Bayes-adaptive RL.
  - Finds Bayes-optimal exploration/ exploitation trade-off *w.r.t.* prior.



#### 2.20 Bayes-adaptive Bernoulli bandits

Given prior $Beta(\alpha_a,\beta_a)$ over reward function $\mathcal R^a$:

- Each time action *a* is selected, update posterior for $\mathcal R^a$:

$$
\cases {Beta(\alpha_a+1,\beta_a) &r=0 \\ Beta(\alpha_a,\beta_a+1) &r=1 }
$$

- This defines transition function $\tilde {\mathcal P}$ for the **Bayes-adaptive** MDP.
- Information state $\left\langle\alpha,\beta\right\rangle$ corresponds to reward model $Beta(\alpha,\beta)$.
- Each state transition corresponds to a Bayesian **model update**.



| <img src="Lecture 9_Exploration.assets/Screenshot 2020-07-09 at 05.06.44.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|     **Fig 9.3** Bayes-Adaptive MDP for Bernoulli bandits     |



### 3. Contextual bandits

#### 3.1 What is a contextual bandit?

A contextual can be formulated as a tuple $\left\langle\mathcal{A,S,R}\right\rangle$.

- $\mathcal A$ is a known set of actions i.e. arms.
- $\mathcal S=\mathbb P[s]$ is an unknown distribution over states i.e. contexts.
- $\mathcal R_s^a(r)=\mathbb P[r|s,a]$ is an unknown probability distribution over rewards.

At each time-step *t*:

- Environment generates state $s_t\sim\mathcal S$.
- Agent selects action $a_t\in\mathcal A$.
- Environment generates reward $r_t\sim\mathcal R_{s_t}^{a_t}$.

**Goal** is to maximise cumulative reward $\sum_{\tau=1}^t r_\tau$.



#### 3.2 Linear UCB

We estimate the action-value function with a linear function approximator:
$$
Q_\theta(s,a) = \phi(s,a)^T\theta\approx Q(s,a)
$$

- We can estimate parameters by **least squares** regression:

$$
\begin{align} A_t &= \sum_{\tau=1}^t\phi(s_\tau,a_\tau)\phi(s_\tau,a_\tau)^T \\ b_t &= \sum_{\tau=1}^t\phi(s_\tau,a_\tau)r_\tau \\ \theta_t &= A_t^{-1}b_t \end{align}
$$

While estimating the mean, we can also estimate the **variance** of the action-value $\sigma_\theta^2(s,a)$, i.e. the uncertainty due to parameter estimation error.

- We add on a bonus for uncertainty

$$
U_\theta(s,a)=c\sigma
$$

​		where UCB is defined to be *c* standard deviation above the mean.



| <img src="Lecture 9_Exploration.assets/Screenshot 2020-07-09 at 05.56.04.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|      **Fig 9.4** Geometric interpretation of linear UCB      |



#### 3.3 Calculating linear UCB

- For least squares regression, parameter covariance is $A^{-1}$.
- Action-value is linearly represented in features

$$
Q_\theta(s,a)=\phi(s,a)^T\theta
$$

- Thus action-value **variance** is quadratic

$$
\sigma_\theta^2=\phi(s,a)^TA^{-1}\phi(s,a)
$$

- Upper confidence bound is

$$
Q_\theta(s,a)+c\sqrt{\phi(s,a)^TA^{-1}\phi(s,a)}
$$

Select action maximising upper confidence bound.



### 4. MDPs

#### 4.1 Exploration & exploitation principles in MDP

The same priciples for exploration & exploitation apply to MDPs.

- Naive exploration.
- Optimistic initialisation.
- Optimism in the face of uncertainty.
- Probability matching.
- Information state search.



#### 4.2 Optimistic initialisation in MDP

Optimistic initialisation applies in both model-free and model-based RL.

- Model-free RL:
  - Initialise action-value function $Q(s,a)\to\frac{r_\max}{1-\gamma}$.
- Model-based RL:
  - Construct an **optimistic model** of the MDP.
  - Initialise transitions to go to heaven, e.g. terminal state with $r_\max$ reward.

Encourages systematic exploration of states and actions.



#### 4.3 Upper confidence bound in MDP

Maximise UCB on action-value function $Q^\pi(s,a)$:
$$
a_t = \arg\max_{a\in\mathcal A}Q(s_t,a)+U(s_t,a)
$$

- Estimate uncertainty in policy evaluation.
- **Ignores** uncertainty from policy improvement.

Maximise UCB on optimal action-value function $Q^*(s,a)$:

- Estimate uncertainty in policy evaluation.
- Also estimate uncertainty from policy improvement. (**hard**)



#### 4.4 Bayesian model-based RL

- Maintain posterior distribution over MDP models.
- Estimate both transitions and rewards $p[\mathcal{P,R}|h_t]$.
- Use posterior to guide exploration.
  - Bayesian UCB.
  - Thompson sampling.



#### 4.5 Information state search in MDP

MDPs can be augmented to include information state.

- Posterior distribution over MDP model is an information state

$$
\tilde s_t=\mathbb[\mathcal{P,R}|h_t]
$$

- Augmented MDP over $\left\langle s,\tilde s\right\rangle$ is called **Bayes-adaptive MDP**.
  - $s$ is the original state within MDP.
  - $\tilde s$ is a statistic of the history i.e. accumulated information.
- Each action *a* causes a transition:
  - To a new state $s'$ with probability $\mathcal P_{s,s'}^a$.
  - To a new information state $\tilde s'$.
- Defines MDP $\mathcal M$ in augmented information state space:

$$
\tilde{\mathcal M} = \left\langle \mathcal{S,\tilde S,A,\tilde P, R,\gamma}\right\rangle
$$

