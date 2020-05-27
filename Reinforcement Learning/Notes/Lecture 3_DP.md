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

The problem is to **evaluate** a given policy $\pi$. It can be solved by iterative application of Bellman expectation backup.

**Synchronous** backups: $v_1 \rightarrow v_2 \rightarrow ... \rightarrow v_\pi$

- At each iteration $k+1$, 
- for all states $s\in \mathcal S$, 
- update $v_{k+1}(s)$ from $v_k(s')$, 
- where $s'$ is a successor state of $s$.



#### 2.2 Evaluating a random policy in the grid world





### 3. Policy iteration

Given a policy $\pi$:

1. Evaluate the policy $\pi$

$$
v_\pi(s) = \mathbb E[R_{t+1}+\gamma R_{t+2}+...|S_t=s]
$$

2. Improve the policy by acting greedily w.r.t. $v_\pi$

$$
\pi' = greedy(v_\pi)
$$

The improved policy is not always optimal. In real-world applications, need more iterations of improvement and evaluation. The process of policy iteration always **converges** to $\pi^*$.



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
v_\pi(s) \leq q_\pi(s,\pi'(s)) =\mathbb E_\pi'[R_{t+1}+\gamma v_\pi(S_{t+1})|S_t=s]
$$



### 4. Value iteration











### 5. Extensions to DP









### 6. Contraction mapping