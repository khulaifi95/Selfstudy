# Reinforcement Learning



## Lecture 3: Planning by Dynamic Programming

### 1. Introduction

#### 1.1 What is dynamic programming?

*Dynamic*: sequential or temporal component to the problem.

*Programming*: optimising a *program* i.e. policy.

Dynamic programming is a method for solving complex problems by breaking them down into subproblems.

1. Solve the subproblems
2. Combine solutions to subproblems



#### 1.2 Requirements for DP

Dynamic Programming is a very general solution method for problems which have two properties:

1. Optimal substructure
   - principle of optimality applies
   - optimal solution can be decomposed into subproblems
2. Overlapping subproblems
   - recur many times
   - cached and reused

MDPs satisfy both properties by:

- Bellman equation $\rightarrow$ recursive decomposition
- Value function $\rightarrow$ stores and reuses solutions



#### 1.3 Planning by DP

Dynamic programming assumes full knowledge of the MDP. It is used for planning in an MDP.

- For prediction:
  - Input: MDP $\left\langle \mathcal {S,A, P, R,\gamma} \right\rangle$ and policy $\pi$ **or** MRP $\left\langle \mathcal {S,P, R,\gamma} \right\rangle$
  - Output: value function $v_\pi$
- For control:
  - Input: MDP $\left\langle \mathcal {S,A, P, R,\gamma} \right\rangle$
  - Output: optimal value function $v_*$ **and** optimal policy $\pi_*$



#### 1.4 Other applications of DP

Dynamic programming is used to solve many other problems, e.g.

- Scheduling algorithms

- String algorithms (e.g. sequence alignment)

- Graph algorithms (e.g. shortest path algorithms)

- Graphical models (e.g. Viterbi algorithm)

- Bioinformatics (e.g. lattice models)



### 2. Policy evaluation

#### 2.1 Iterative policy evaluation

- Problem: **evaluate** a given policy $\pi$. 

-  Solution: iterative application of Bellman expectation equation as backup.

Update value function $v_1 \rightarrow v_2 \rightarrow ... \rightarrow v_\pi$ use **synchronous** backups: 

- At each iteration $k+1$, 
- for **all states** $s\in \mathcal S$, 
- update $v_{k+1}(s)$ from $v_k(s')$, 
- where $s'$ is a successor state of $s$.

Convergence to $v_\pi$ will be proved in the later section.

From the Bellman expectation equation, we iterate the process of updating value function:
$$
v_{k+1} =\sum_{a\in \mathcal A} \pi(a|s)(\mathcal R_s^a+\gamma\sum_{s'\in \mathcal S}\mathcal P_{ss'}^av_k(s'))
$$
In matrix form:
$$
\mathbf v^{k+1} = \mathcal R^\pi+\gamma \mathcal P^\pi \mathbf v^k
$$
Thus we can update the value functions of all states in iterations.



#### 2.2 Evaluating a random policy in the grid world

| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 3_DP.assets/Screenshot 2020-06-02 at 16.32.05.png" style="zoom:100%;" /> |
| :----------------------------------------------------------: |
|         **Fig 3.1** The grid world policy evaluation         |



- Undiscounted episodic MDP with $\gamma =1$.
- Nonterminal states $1,...,14$.
- One terminal state shown twice in shaded squares.
- Actions leading out of the grid leave state unchanged.
- Reward is -1 until the terminal state is reached.
- Agent follows uniform random policy:

$$
\pi(n|\cdot)=\pi(e|\cdot)=\pi(s|\cdot)=\pi(w|\cdot)=0.25
$$

We want to know: 

On average, how many steps until hit the terminal state?



|      Iteration       |                   $v_k$ for random policy                    |                  Greedy policy w.r.t. $v_k$                  |
| :------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|         k=0          | ![Screenshot 2020-06-02 at 16.45.53](/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 3_DP.assets/Screenshot 2020-06-02 at 16.45.53.png) | ![Screenshot 2020-06-02 at 16.46.15](/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 3_DP.assets/Screenshot 2020-06-02 at 16.46.15.png) |
|         k=1          | ![Screenshot 2020-06-02 at 16.45.59](/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 3_DP.assets/Screenshot 2020-06-02 at 16.45.59.png) | ![Screenshot 2020-06-02 at 16.46.21](/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 3_DP.assets/Screenshot 2020-06-02 at 16.46.21.png) |
|         k=2          | ![Screenshot 2020-06-02 at 16.46.07](/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 3_DP.assets/Screenshot 2020-06-02 at 16.46.07.png) | ![Screenshot 2020-06-02 at 16.46.27](/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 3_DP.assets/Screenshot 2020-06-02 at 16.46.27.png) |
|     k=3: optimal     | ![Screenshot 2020-06-02 at 16.46.34](/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 3_DP.assets/Screenshot 2020-06-02 at 16.46.34.png) | ![Screenshot 2020-06-02 at 16.46.46](/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 3_DP.assets/Screenshot 2020-06-02 at 16.46.46.png) |
|         k=10         | ![Screenshot 2020-06-02 at 16.46.37](/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 3_DP.assets/Screenshot 2020-06-02 at 16.46.37.png) | ![Screenshot 2020-06-02 at 16.46.52](/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 3_DP.assets/Screenshot 2020-06-02 at 16.46.52.png) |
| k=$\infty$: converge | ![Screenshot 2020-06-02 at 16.46.41](/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 3_DP.assets/Screenshot 2020-06-02 at 16.46.41.png) | ![Screenshot 2020-06-02 at 16.46.56](/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 3_DP.assets/Screenshot 2020-06-02 at 16.46.56.png) |
|                      |           **Fig 3.2** Iteration policy evaluation            |                                                              |



We figure out the value of current policy by iterating a Bellman equation for the new values in every state.

- Value function helps figure out better policies.
- We can build a better policy by acting greedily on the evaluation of one policy.



### 3. Policy iteration

#### 3.1 Improve a policy

Given a policy $\pi$:

1. Evaluate the policy $\pi$

$$
v_\pi(s) = \mathbb E[R_{t+1}+\gamma R_{t+2}+...|S_t=s]
$$

2. Improve the policy by acting greedily w.r.t. $v_\pi$

$$
\pi' = greedy(v_\pi)
$$

The improved policy is not always optimal. 

In real-world applications, need more iterations of improvement and evaluation. 

The process of policy iteration always **converges** to $\pi^*$.



| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 3_DP.assets/Screenshot 2020-06-02 at 17.17.41.png" style="zoom:67%;" /> |
| :----------------------------------------------------------: |
|  **Fig 3.3** Policy iteration of improvement and evaluation  |


$$
\pi^* \rightleftarrows v^*
$$

- Policy **evaluation** estimate $v_\pi$.
- Policy **improvement** generate greedy policy $\pi'\geq \pi$.



#### 3.2 Policy improvement

Consider a deterministic policy $a=\pi(s)$. 

We can improve the policy by acting **greedily**
$$
\pi'(s) = \arg\max_{a\in \mathcal A} q_\pi(s,a)
$$
This improves the value from any state $s$ over one step:
$$
q_\pi(s, \pi'(s)) = \max_{a\in\mathcal A}q_\pi(s,a)\geq q_\pi(s,\pi(s)) = v_\pi(s)
$$
where $q_\pi(s,\pi'(s))$ means take one step greedily followed by the policy $\pi$ after.

It therefore improves the value function, $v_\pi'(s)\geq v_\pi(s)$:
$$
\begin{align}
v_\pi(s) &\leq q_\pi(s,\pi'(s)) =\mathbb E_{\pi'}[R_{t+1}+\gamma v_\pi(S_{t+1})|S_t=s] \\ &\leq \mathbb E_{\pi'}[R_{t+1}+\gamma q_\pi(S_{t+1},\pi'(S_{t+1}))|S_t=s] \\ &\leq \mathbb E_{\pi'}[R_{t+1}+ \gamma R_{t+2}+\gamma^2q_\pi(S_{t+2}, \pi'(S_{t+2}))|S_t=s]  \\ &\leq \mathbb E_{\pi'}[R_{t+1}+\gamma R_{t+2}+...|S_t=s]=v_{\pi'}(s)
\end{align}
$$

- If improvements stop:

$$
q_\pi(s,\pi'(s)) = \max_{a\in \mathcal A}q_\pi(s,a) = q_\pi(s,\pi(s))=v_\pi(s)
$$

- Then the Bellman optimality equation has been satisfied as:

$$
v_\pi(s)=\max_{a\in \mathcal A}q_\pi(s,a)
$$

- Therefore:

$$
v_\pi(s)=v_*(s) \ \forall s\in \mathcal S
$$



#### 3.3 Modified policy iteration

Policy evaluation needs not always converge to $v_\pi$.

- Introduce a stopping condition.
- Stop after *k* iterations of iterative policy evaluation.
- Update policy **every** iteration.
  - Equivalent to value iteration.



### 4. Value iteration

#### 4.1 Principle of optimality

Any optimal policy can be subdivided into two components:

- An optimal first action $A_*$.
- Followed by an optimal policy from successor state $s'$.

**Theorem**: 

A policy $\pi(a|s)$ achieves the optimal value from state *s*, $v_\pi(a|s)=v_*(s)$ if and only if:

- For any state *s'* reachable from *s*, $\pi$ achieves the optimal value from state *s'*, $v_\pi(s')=v_*(s')$.



#### 4.2 Deterministic value iteration

If we know the solution to subproblems $v_*(s')$.

The solution $v_*(s)$ can be found by one-step lookahead using Bellman optimality equation:
$$
v_*(s)\leftarrow \max_{a\in \mathcal A}\mathcal R_s^a+\gamma \sum_{s'\in \mathcal S}\mathcal P_{ss'}^av_*(s')
$$

- The idea of value iteration is to apply the updates iteratively.
- Start with final rewards and work **backwards**.
- Still works with loopy, stochastic MDPs.



| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 3_DP.assets/Screenshot 2020-06-02 at 18.47.38.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|        **Fig 3.4** Find the shortest path in the grid        |



- We update all the states in every iteration.
- The value of a state uses the optimal as backup.



#### 4.3 Value iteration in MDPs

- Problem: find optimal policy $\pi$.
- Solution: iterative application of Bellman optimality backup.

Update value function $v_1 \rightarrow v_2 \rightarrow ... \rightarrow v_\pi$ using **synchronous** backups:

- At each iteration $k+1$,
- For all states $s\in \mathcal S$,
- Update $v_{k+1}(s)$ from $v_k(s')$.

Different from policy iteration:

- There is no explicit policy.
- Intermediate value functions may not correspond to any policy.

From the Bellman optimality equation, we iterate the process of updating value function:
$$
v_{k+1}(s)=\max_{a\in \mathcal A}(\mathcal R_s^a+\gamma \sum_{s'\in \mathcal S}\mathcal P_{ss'}^av_k(s'))
$$
In matrix form:
$$
\mathbf v_{k+1} = \max_{a\in \mathcal A}(\mathcal R^a+\gamma \mathcal P^a\mathbf v_k)
$$


| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 3_DP.assets/Screenshot 2020-06-02 at 19.39.57.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
| **Fig 3.5** Value iteration using Bellman optimality backup  |



#### 4.4. Synchronous Dynamic Programming Algorithms

The following table summarises the problems DP solved using Bellman equation:

| Problem    | Bellman Equation                                         | Algorithm                   |
| ---------- | -------------------------------------------------------- | --------------------------- |
| Prediction | Bellman expectation equation                             | Iterative policy evaluation |
| Control    | Bellman expectation equation + Greedy policy improvement | Policy iteration            |
| Control    | Bellman optimality equation                              | Value iteration             |

- Algorithms are based on state-value function $v_\pi(s)$ or $v_*(s)$.
- Complexity $O(mn^2)$ per iteration, for *m* actions and *n* states.
- Could also apply to **action-value** function $q_\pi(s,a)$ or $q_*(s,a)$.
- Complexity becomes $O(m^2n^2)$ per iteration.



### 5. Extensions to DP

#### 5.1 Asynchronous dynamic programming

So far, the DP methods used *synchronous* backups, i.e., backed up all states in parallel.

*Asynchronous* DP backs up states individually in any order.

- For each selected state, apply only the **appropriate** backup.
- Significantly **reduced computation**.
- Guaranteed to converge if all states continue to be selected.

Three simple ideas for asynchronous dynamic programming:

1. In-place DP

   Only stores one copy of value function.

2. Prioritised sweeping

   Backup the state with the largest remaining Bellman error:

$$
|\max_{a\in\mathcal A}(\mathcal R_s^a+\gamma \sum_{s'\in \mathcal S}\mathcal P_{ss'}^av(s'))-v(s)|
$$

3. Real-time DP

   Use agent's experience to guide the selection of relevant states.



#### 5.2 Full-width backups

The above DP algorithms use full-width backups. 

For each backup:

- Consider every successor state and action.
- Use knowledge of the MDP trasitions and reward function.

DP is effective for medium-sized problems. 

For large problems, DP suffers Bellman's *curse of dimensionality*.

- Number of states $n=|\mathcal S|$ grows exponentially with number of state variables.

- Even one backup can be too expensive.



#### 5.3 Sample backups

We consider **sample** backups in DP.

- Instead of reward function $\mathcal R$ and transition dynamics $\mathcal P$,
- We use sample rewards and sample transitions $\left\langle S,A,R,S'\right\rangle$.

**Advantages**:

- Model-free: no advance knowledge of MDP required.
- Breaks the curse of dimensionality through **sampling**.
- Cost of backup is constant, independent of $n=|\mathcal S|$.



#### 5.4 Approximate dynamic programming

We approximate the value function when sampling.

-  Use a **function approximator** $\hat v(s,\mathbf w)$.

- Apply dynamic programming to $\hat v(s,\mathbf w)$.

- Fitted value iteration repeats at each iteration *k*,

  - Sample states $\mathcal {\tilde S \sube S}$.
  - For each state $s\in \mathcal {\tilde S}$, estimate target value using Bellman optimality equation:

  $$
  \tilde v_k(s)\max_{a\in\mathcal A}(\mathcal R_s^a+\gamma \sum_{s'\in \mathcal S}\mathcal P_{ss'}^a\hat v(s', \mathbf w_k))
  $$

  - Train next value function $\hat v(\cdot, \mathbf w_{k+1})$ using targets $\{\left\langle s,\tilde v_k(s)\right\rangle\}$.



### 6. Contraction mapping

Some fundamental theorems need to be proved for the use of the DP.

- Why value iteration converges to $v_*$?
- Why iterative policy evaluation converges to $v_\pi$?
- And therefore that policy iteration converges to $v_*$?
- Is the solution unique?
- How fast do these algorithms converge?

We can resolve these questions by **contraction mapping** theorem.



#### 6.1 Value function space

We first consider the vector space $\mathcal V$ over the value functions.

- It has $|\mathcal S|$ dimensions.
- Each point in the space fully specifies a value function $v(s)$.
- We will show that a Bellman backup brings the points i.e. value functions closer.
- Therefore the backups must **converge** on a **unique** solution.

We measure the **distance** between state-value functions *u* and *v* by the $\infty$-norm.

- The distance is the largest difference between state values on each dimension:

$$
\Vert u-v\Vert_\infty = \max_{s\in \mathcal S}|u(s)-v(s)|
$$



#### 6.2 Contraction mapping

**Theorem**:

For any metric space $\mathcal V$ that is complete (closed) under an operator $T(v)$, where $T$ is a $\gamma$-contraction:

- $T$ converges to a unique fixed point.
- At a linear convergence rate of $\gamma$.



#### 6.3 Contraction of Bellman expectation backup

Define the Bellman expectation backup operator $T^\pi$ as:
$$
T^\pi(v) = \mathcal R^\pi + \gamma \mathcal P^\pi v
$$
which is a $\gamma$-contraction that makes value functons **closer** by at least $\gamma$:
$$
\begin{align} \Vert T^\pi(u)-T^\pi(v)\Vert_\infty&=\Vert (\mathcal R^\pi+\gamma \mathcal P^\pi u)-(\mathcal R^\pi+\gamma \mathcal P^\pi v)\Vert_\infty \\ &= \Vert\gamma\mathcal P^\pi(u-v)\Vert_\infty \\ &\leq\Vert \gamma\mathcal P^\pi\Vert u-v\Vert_\infty\Vert_\infty\\&\leq\gamma\Vert u-v\Vert_\infty\end{align}
$$


#### 6.4 Convergence of policy iteration

- The Bellman expectation operator $T^\pi$ has a unique fixed point.
- By Bellman expectation equation, $v_\pi$ is a fixed point of $T^\pi$.

Thus by the theorem:

- Iterative policy evaluation converges on $v_\pi$.
- Policy iteration converges on $v_*$.



#### 6.5 Contraction of Bellman optimality backup

Define the Bellman optimality backup operator $T^*$ as:
$$
T^*(v)=\max_{a\in \mathcal A}\mathcal R^a+\gamma \mathcal P^av
$$
which is a $\gamma$-contraction that makes value functions closer by at least $\gamma$:
$$
\Vert T^*(u)-T^*(v)\Vert_\infty\leq\gamma\Vert u-v\Vert_\infty\
$$


#### 6.6 Convergence of value iteration

- The Bellman optimality operator $T^*$ has a unique fixed point.
- By Bellman optimality equation, $v_*$ is a fixed point of $T^*$.

Thus by the theorem:

- Value iteration converges on $v_*$.

