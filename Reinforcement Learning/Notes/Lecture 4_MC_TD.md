# Reinforcement Learning



## Lecture 4: Model-free Prediction



### 1. Monte-Carlo learning

#### 1.1 Monte-Carlo reinforcement learning

MC methods learn directly from episodes of experience.

- Model-free: no knowledge of MDP transitions & rewards.
- No bootstrpping: learn from *complete* episodes.
- Simple idea: use the **mean return** as an estimate of value function.
- Caveat: can only apply to *episodic* MDPs that all must terminate.



#### 1.2 Monte-Carlo policy evaluation

- Goal: learn $v_\pi$ from episodes of experience under policy $\pi$

$$
S_1,A_1, R_2, ...,S_k \sim \pi
$$

- Recall the return is the total discounted **reward**:

$$
G_t=R_{t+1}+\gamma R_{t+2}+...+\gamma^{T-1}R_T
$$

- Recall the value function is the **expected return**:

$$
v_\pi(s)=\mathbb E_\pi[G_t|S_t=s]
$$

Monte-Carlo policy evaluation uses **empirical mean** return instead of expected return.



#### 1.3 First-visit







### 2. Temporal-difference learning

