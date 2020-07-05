# Reinforcement Learning



## Lecture 8: Integrating Learning and Planning



### 1. Introduction

#### 1.1 Model-based RL

- Last lecture: learn **policy** directly from experience.
- Previous lectures: learn **value** function from experience.
- This lecture: learn **model** directly from experience.
  - Use **planning** to construct a value function *or* policy.
  - Integrate learning and planning into a single architecture.



#### 1.2 Model-based and model-free

- Model-free RL:
  - No model.
  - **Learn** value function (and/or policy) from experience.
- Model-based RL:
  - Learn a model from experience.
  - **Plan** value function (and/or policy) from model.



| <img src="Lecture 8_Model-based.assets/Screenshot 2020-07-06 at 01.19.14.png" style="zoom:40%;" /> | <img src="Lecture 8_Model-based.assets/Screenshot 2020-07-06 at 01.19.22.png" style="zoom:40%;" /> |
| -----------------------------------------------------------: | :----------------------------------------------------------- |
|                                    **Fig 8.1** Model-free RL | vs. Model-based RL                                           |



### 2. Model-based reinforcement learning

#### 2.1 Properties of model-based RL

Advantages:

- Can efficiently learn model by **supervised** learning methods.
- Can reason about model **uncertainty**.

Disadvantages:

- First learn a model, then construct a value function.
  - Two sources of approximation error.



| <img src="Lecture 8_Model-based.assets/Screenshot 2020-07-06 at 02.54.01.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|         **Fig 8.2** Process cycle of model-based RL          |



#### 2.2 What is a model?

A model $\mathcal M$ is a representation of an MDP $\left\langle \mathcal{S,A,P,R}\right\rangle$ parametrised by $\eta$.

- We assume state space $\mathcal S$ and action space $\mathcal A$ are known.
- So a model $\mathcal M = \left\langle \mathcal P_\eta, \mathcal R_\eta\right\rangle$ represents state transitions and rewards:

$$
\mathcal P_\eta \approx \mathcal P, \mathcal R_\eta \approx \mathcal R \\ S_{t+1}\sim \mathcal P_\eta(S_{t+1}|S_t,A_t) \\ R_{t+1} = \mathcal R_\eta(R_{t+1}|S_t,A_t)
$$

- Typically, we assume **conditional independence** between state transitions and rewards

$$
\mathbb P[S_{t+1},R_{t+1}|S_t,A_t] = \mathbb P[S_{t+1}|S_t,A_t]\mathbb P[R_{t+1}|S_t,A_t]
$$



#### 2.3 Model learning

The goal is to estimate model $\mathcal M_\eta$ from experience $\{S_1,A_1,R_2,...,S_T\}$.

Essentially, this is a supervised learning problem
$$
S_1,A_1\rarr R_2, S_2 \\ S_2,A_2\rarr R_3, S_3 \\ \vdots \\ S_{T-1}, A_{T-1} \rarr R_T, S_T
$$

- Learning $s,a\rarr r$ is a **regression** problem.
- Leraning $s,a\rarr s'$ is a **density estimation** problem.
- Loss functions including e.g. MSE, KL divergence, etc.
- Find parameters $\eta$ that minimise empirical loss.



#### 2.4 Example of models

There are different representations of models, e.g.

- Table lookup model.
- Linear expectation model.
- Linear Gaussian model.
- Gaussian process model.
- Deep belief network model.

Table lookup model is an explicit MDP $\left\langle \mathcal {\hat P, \hat R}\right\rangle$.

- Count visits $N(s,a)$ to each state action pair:

$$
\hat{\mathcal P}_{s,s'}^a=\frac1{N(s,a)}\sum_{t=1}^T\mathbf 1(S_t,A_t,S{t+1}=s,a,s') \\ \hat{\mathcal R}_s^a=\frac1{N(s,a)}\sum_{t=1}^T\mathbf 1(S_t,A_t=s,a)R_t
$$

- Alternatively:
  - At each time-step *t*, record experience tuple $\left\langle S_t,A_t,R_{t+1},S_{t+1}\right\rangle$.
  - To sample model, randomly pick tuple matching $\left\langle s,a,.,. \right\rangle$.



#### 2.5 Planning with a model

Given a model $\mathcal M_\eta=\left\langle \mathcal{P_\eta,R_\eta}\right\rangle$:

- Solve the MDP $\left\langle \mathcal{S,A,P_\eta,R_\eta}\right\rangle$.
- Use appropriate planning algorithm:
  - Value iteration.
  - Policy iteration.
  - Tree search.



#### 2.6 Sample-based planning

Sample-based planning is a simple but powerful approach to planning.

- It uses the model only to **sample experience**:

$$
S_{t+1}\sim \mathcal P_\eta(S_{t+1}|S_t,A_t) \\ R_{t+1}\sim \mathcal R_\eta(R_{t+1}|S_t,A_t)
$$

- Then apply **model-free** RL to samples, e.g.
  - Monte-Carlo control.
  - Sarsa.
  - Q-learning.

- Sample-based planning methods are often more **efficient**.



#### 2.7 Planning with an inaccurate model

Given an **imperfect** model $\left\langle \mathcal{P_\eta,R_\eta}\right\rangle \neq \left\langle \mathcal{P,R}\right\rangle$:

- Performance of model-based RL is **limited to optimal** policy for approximate MDP $\left\langle \mathcal{S,A,P_\eta,R_\eta}\right\rangle $.
  - Model-based RL is only as good as the estimated model.
- When the model is inaccurate, planning process will compute a **suboptimal** policy.

Solutions:

1. When model is wrong, use model-free RL.
2. Reason explicitly about model uncertainty.



### 3. Integrated architectures

#### 3.1 Real and simulated experience

We consider two sources of experiences:

1. **Real experience**, sampled from environment i.e. **true** MDP:

$$
\mathcal {S'\sim P}_{s,s'}^a \\ R = \mathcal R_s^a
$$

2. **Simulated experience**, sampled from model i.e. approximate MDP:

$$
S'\sim \mathcal P_\eta(S'|S,A) \\ R = \mathcal R_\eta(R|S,A)
$$



#### 3.2 Integrating learning and planning

- Model-free RL:
  - No model.
  - **Learn** value function (and/or policy) from real experience.
- Model-based RL:
  - Learn a model from real experience.
  - **Plan** value function (and/or policy) from simulated experience.
- Dyna:
  - Learn a model from real experience.
  - **Learn and plan** value function (and/or policy) from real and simulated experience.



| <img src="Lecture 8_Model-based.assets/Screenshot 2020-07-06 at 03.15.14.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|                **Fig 8.3** Dyna architecture                 |



#### 3.3 Dyna-Q algorithm

| Dyna-Q                                                       |
| ------------------------------------------------------------ |
| **Initialise** $Q(s,a)$ and $\mathcal M(s,a) \ \forall s\in\mathcal S, a\in\mathcal A(s)$ |
| **Iterate**:                                                 |
| $S\larr $ current state (nonterminal)                        |
| $A\larr \epsilon\text{-greedy}(S,Q)$                         |
| Execute action $A$, observe resultant reward $R$ and state $S'$. |
| $Q(S,A)\larr Q(S,A)+\alpha[R+\gamma\max_aQ(S',a)-Q(S,A)]$    |
| $\mathcal M(S,A)\larr R,S'$ (assuming deterministic environment) |
| **Repeat** *n* times:                                        |
| $S\larr$ random previously observed state                    |
| $A\larr$ random action previously taken in $S$               |
| $R,S'\larr \mathcal M(S,A)$                                  |
| $Q(S,A)\larr Q(S,A)+\alpha[R+\gamma \max_aQ(S',a)-Q(S,A)]$   |
| **End**                                                      |
| **End**                                                      |



#### 3.4 Dyna-Q with an inaccurate model

An environment with blocked path is changed after 1000 time-steps.

Comparing performance of three Dyna algorithms:

|                                Changed to harder environment | Changed to easier environment                                |
| -----------------------------------------------------------: | ------------------------------------------------------------ |
| <img src="Lecture 8_Model-based.assets/Screenshot 2020-07-06 at 04.09.10.png" style="zoom:50%;" /> | <img src="Lecture 8_Model-based.assets/Screenshot 2020-07-06 at 04.10.02.png" style="zoom:50%;" /> |
|                               **Fig 8.4** Dyna with changing | environment                                                  |



### 4. Simulation-based search

#### 4.1 Forward search

Forward search algorithms select the best action by **lookahead**.

- Build a **search tree** with the current state $s_t$ at the root.
- Using a **model** of the MDP to look ahead.
- No need to solve whole MDP, just sub-MDP from **now**.



| <img src="Lecture 8_Model-based.assets/Screenshot 2020-07-06 at 04.14.12.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|               **Fig 8.5** Forward search tree                |



#### 4.2 Simulation-based search

Simulation-based search is a forward search paradigm using **sample-based** planning.

- Simulate episodes of experience from **now** with the model:

$$
\{s_t^k,A_t^k,R_{t+1}^k,...,S_T^k\}_{k=1}^K \sim\mathcal M_v
$$

- Apply model-free RL to simulated episodes.
  - Monto-Carlo control $\rarr$ Monte-Carlo search.
  - Sarsa $\rarr$ TD search.



#### 4.3 Simple Monte-Carlo search

Given a model $\mathcal M_v$ and a **simulation policy** $\pi$:

- For each action $a\in\mathcal A$:

  - Simulate $K$ episodes from current (real) state $s_t$:

  $$
  \{s_t,a,R_{t+1}^k,S_{t+1}^k,A_{t+1}^k,...,S_T^k\}_{k=1}^K \sim \mathcal M_v,\pi
  $$

  - Evaluate actions by **mean return** i.e. Monte-Carlo evaluation:

$$
Q(s_t,a) = \frac1K\sum_{k=1}^KG_t\xrightarrow{P}q_\pi(s_t,a)
$$

- Select current (real) action with maximum value

$$
a_t = \arg\max_{a\in\mathcal A}Q(s_t,a)
$$



#### 4.4 Monte-Carlo tree search evaluation

Given a model $\mathcal M_v$:

- Simulate $K$ episodes from current state $s_t$ using current simulation policy $\pi$:

$$
\{s_t,A_t^k,R_{t+1}^k,S_{t+1}^k,...,S_T^k\}_{k=1}^K \sim \mathcal M_v,\pi
$$

- Build a search tree containing **visited** states and actions.
- **Evaluate** states $Q(s,a)$ by mean return of episodes from $s,a$:

$$
Q(s,a) = \frac1{N(s,a)}\sum_{k=1}^K\sum_{u=t}^T\mathbf 1(S_u,A_u=s,a)G_u\xrightarrow{P}q_\pi(s,a)
$$

- Select current (real) action with maximum value in search tree

$$
a_t = \arg\max_{a\in\mathcal A}Q(s_t,a)
$$



#### 4.5 Monte-Carlo tree search simulation

In MCTS, the simulation policy **improves**.

- Each simulation consists of two phases, i.e. in-tree and out-of-tree:
  - **Tree policy**(improves): pick actions to maximise $Q(S,A)$.
  - **Default policy**(fixed): pick actions randomly.
- In each simulation, repeat:
  - **Evaluate** states $Q(S,A)$ by Monte-Carlo evaluation.
  - **Improve** tree policy, e.g. by $\epsilon\text{-greedy}(Q)$.

- Monte-Carlo control is applied to **simulated experience**.
- Converges on the optimal search tree, $Q(S,A)\rarr q_*(S,A)$.



#### 4.6 Advantages of MCTS

- Hightly selective best-first search.

- Evaluates states **dynamically**. (unlike DP)
- Uses **sampling** to break curse of dimensionality.
- Works for *black-box* models that only requires samples.
- Computationally efficient, anytime, parallelisable.



#### 4.7 Temporal-difference search

TD search is another simulation-based search using TD instead of MC.

Sarsa is applied to sub-MDP from now instead of MC control.

- Simulate episodes from the current (real) state $s_t$.
- Estimate action-value function $Q(s,a)$.
- For each step of simulation, update action-values by Sarsa:

$$
\Delta Q(S,A) = \alpha(R+\gamma Q(S',A')-Q(S,A))
$$

- Select actions based on action-values $Q(s,a)$ using e.g. $\epsilon\text{-greedy}$.

- Value $Q$ can be approximated using functions.



#### 4.8 Dyna-2

In Dyna-2, the agent stores two sets of feature weights:

- **Long-term** memory:
  - Updated from **real experience** using TD learning.
  - **General** domain knowledge that applies to any episode.
- **Working** memory:
  - Updated from **simulated experience** using TD search.
  - Specific **local** knowledge about the current simulation.

The overall value function is the **sum** of long and short-term memories.



| <img src="Lecture 8_Model-based.assets/Screenshot 2020-07-06 at 04.43.29.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|            **Fig 8.6** Results of TD search in Go            |

