# Reinforcement Learning



## Lecture 4: Model-free Prediction



### 1. Monte-Carlo learning

#### 1.1 MC reinforcement learning

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



#### 1.3 First-visit MC

To evaluate state *s*, use the time-step *t* where state *s* is **first** visited in an episode.

Update:

- Increment counter $N(s)\leftarrow N(s)+1$
- Increment total return $S(s)\leftarrow S(s) + G_t$
- Estimate **value** by **mean** return $V(s)=S(s)/N(s)$

By law of large numbers, $V(s)\rarr v_\pi(s)$ as $N(s)\rarr \infty$.



#### 1.4 Every-visit MC

To evaluate state *s*, use **every** time-step *t* where state *s* is visited in an episode.

Update:

- Increment counter $N(s)\leftarrow N(s)+1$
- Increment total return $S(s)\leftarrow S(s) + G_t$
- Estimate **value** by **mean** return $V(s)=S(s)/N(s)$

By law of large numbers, $V(s)\rarr v_\pi(s)$ as $N(s)\rarr \infty$.



#### 1.5 Incremental Monte-Carlo updates

The mean $\mu_1, \mu_2,...$ of a sequence $x_1,x_2,...$ can be computed incrementally:
$$
\begin{align}\mu_k&=\frac1k\sum_{j=1}^kx_j\\&=\frac1k(x_k+\sum_{j=1}^{k-1}x_j)\\&=\frac1k(x_k+(k-1)\mu_{k-1})\\&=\mu_{k-1}+\frac1k(x_k-\mu_{k-1}) \end{align}
$$
where the second part is an *error* in the estimate, which is reduced by taking step *k*.

Analogy to the incremental mean method, we update $V(s)$ incrementally after episode $S_1, A_1,R_2,...,S_T$.

- For each state $S_t$ with return $G_t$:

$$
N(S_t)\larr N(S_t)+1 \\ V(S_t)\larr V(S_t)+\frac1{N(S_t)}(G_t-V(S_t))
$$

-  In non-stationary problems, it can be useful to track a running mean, i.e. forget old episodes:

$$
V(S_t)\larr V(S_t)+\alpha(G_t-V(S_t))
$$



### 2. Temporal-difference learning

#### 2.1 TD reinforcement learning

TD methods learn directly from episodes of experience.

- Model-free: no knowledge of MDP transitions & rewards.
- Bootstrapping: learn from *incomplete* episodes.
- Idea: update a guess towards a guess.



#### 2.2 MC and TD

- Goal: learn $v_\pi$ online from experience under policy $\pi$.
- Incremental every-visit Monte-Carlo update value $V(S_t)$ towards actual return $G_t$:

$$
V(S_t)\larr V(S_t) + \alpha(G_t-V(S_t))
$$

- SImplest temporal-difference learning algorithm TD(0) update value $V(S_t)$ towards **estimated return** $R_{t+1}+\gamma V(S_{t+1})$:

$$
V(S_t)\larr V(S_t)+\alpha(R_{t+1}+\gamma V(S_{t+1})-V(S_t))
$$

​		where $R_{t+1}+\gamma V(S_{t+1})$ is called the **TD target**, $\delta_t=R_{t+1}+\gamma V(S_{t+1})-V(S_t)$ is the **TD error**.



#### 2.3 Driving home example

Model the process of driving home with predicted total time:

| State              | Elapsed time | Predicted time to go | Predicted total time |
| ------------------ | ------------ | -------------------- | -------------------- |
| leaving office     | 0            | 30                   | 30                   |
| Reach car, raining | 5            | 35                   | 40                   |
| exit highway       | 20           | 15                   | 35                   |
| behind truck       | 30           | 10                   | 40                   |
| home street        | 40           | 3                    | 43                   |
| arrive home        | 43           | 0                    | 43                   |



The changes recommended by MC and TD ($\alpha=1$) are illustrated below:



| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 4_MC_TD.assets/Screenshot 2020-06-23 at 12.30.24.png" style="zoom:66%;" /> | <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 4_MC_TD.assets/Screenshot 2020-06-23 at 12.30.14.png" style="zoom:66%;" /> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                 **Fig 4.1** Driving home MC                  |                       Driving home TD                        |



#### 2.4 MC vs. TD (1)

TD can learn ***before*** knowing the final outcome.

- TD can learn online after every step.
- MC must wait until end of episode before return is known.

TD can learn ***without*** the final outcome.

- TD can learn from incomplete sequences.
- MC can only learn from complete sequences.
- TD works in continuing (non-terminating) environments.
- MC only works for episodic (terminating) environments.



#### 2.5 Bias/variance trade-off

- Return $G_t=R_{t+1}+\gamma R_{t+2}+...+\gamma^{T-1}R_T$ is *unbiased* estimate of $v_\pi(S_t)$.
- True TD target $R_{t+1}+\gamma v_\pi(S_{t+1})$ is *unbiased* estimate of $v_\pi(S_t)$.
- TD target $R_{t+1}+\gamma V(S_{t+1})$ is **biased** estimate of $v_\pi(S_t)$.

Thus TD target has much lower variance than the return:

- Return depends on *many* random actions, transitions, rewards.
- TD target depends on **one** random action, transition and reward.



#### 2.6 MC vs. TD (2)

MC has high variance, zero bias.

- Good convergence properties (even with function approximation).
- Not very sensitive to initial value.
- Very simple to understand and use.

TD has low variance, some bias.

- Usually more efficient than MC.
- TD(0) converges to $v_\pi(s)$ (but not with function approximation).
- More sensitive to initial value.



#### 2.7 Certainty equivalence

MC and TD converge $V(s) \rarr v_\pi(s)$ as experience $\rarr \infty$.

For batch solution of finite experience, e.g. apply MC and TD(0) to repeatedly sample episode $k \in [1,K]$:
$$
s_1^1, a_1^1,r_2^1,...,s_{T_1}^1 \\ \vdots \\ s_1^K, a_1^K,r_2^K,...,s_{T_1}^K
$$

- MC converges to solution with minimum MSE that best fit to the observed returns:

$$
\sum_{k=1}^K\sum_{t=1}^{T_k}(G_t^k-V(S_t^k))^2
$$

- TD(0) converges to solution of MLE of Markov model that best fit the data:

$$
\hat {\mathcal P}_{s,s'}^a=\frac 1{N(s,a)}\sum_{k=1}^K\sum_{t=1}^{T_k}\mathbf 1(s_t^k,a_t^k,s_{t+1}^k=s,a,s') \\ \hat {\mathcal R}_s^a= \frac 1{N(s,a)}\sum_{k=1}^K\sum_{t=1}^{T_k}\mathbf 1(s_t^k, a_t^k=s,a)r_t^k
$$



#### 2.8 MC vs. TD (3)

TD exploits Markov property.

- Usually more efficient in Markov environments.

MC does not exploit Markov property.

- Usually more effective in non-Markov environments. (partially observed)



#### 2.9 Bootstrapping and sampling

- Bootstrapping: update involves an estimate.
  - MC does not bootstrap.
  - DP & TD bootstrap.
- Sampling: update samples an expectation.
  - DP does not sample.
  - MC & TD samples.



#### 2.10 Unified view of policy evaluation

|                          MC backup                           |                          TD backup                           |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|           $V(S_t)\larr V(S_t) +\alpha(G_t-V(S_t))$           | $V(S_t)\larr V(S_t)+\alpha (R_{t+1}+\gamma V(S_{t+1})-V(S_t))$ |
| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 4_MC_TD.assets/Screenshot 2020-06-23 at 13.10.33.png" style="zoom:33%;" /> | <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 4_MC_TD.assets/Screenshot 2020-06-23 at 13.10.51.png" style="zoom:33%;" /> |
|                        **DP backup**                         |                       **Unified view**                       |
|    $V(S_t)\larr \mathbb E_\pi[R_{t+1}+\gamma V(S_{t+1})]$    |                  Bootstrapping and sampling                  |
| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 4_MC_TD.assets/Screenshot 2020-06-23 at 13.10.55-2914525.png" style="zoom:33%;" /> | <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 4_MC_TD.assets/Screenshot 2020-06-23 at 13.16.30.png" style="zoom:33%;" /> |
|        **Fig 4.2** Unified view of policy evaluation         |                                                              |



### 3. TD($\lambda$)

#### 3.1 n-Step prediction

We can let TD target look *n* steps into the future.

| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 4_MC_TD.assets/Screenshot 2020-06-23 at 13.32.50.png" style="zoom:67%;" /> |
| :----------------------------------------------------------: |
|                    **Fig 4.3** n-step TD                     |



#### 3.2 n-Step return

Consider the *n*-step returns for $n=1,2,\infty$:

- n=1 (TD): $G_t^{(1)}=R_{t+1}+\gamma V(S_{t+1})$
- n=2: $G_t^{(2)}=R_{t+1}+\gamma R_{t+2}+\gamma^2 V(S_{t+2})$
- n=$\infty$ (MC): $G_t^{(\infty)}=R_{t+1}+\gamma R_{t+2}+ ...+ \gamma ^{T-1}R_T$

We can define the *n*-step return:
$$
G_t^{(n)}=R_{t+1}+\gamma R_{t+2}+...+ \gamma^{n-1}R_{t+n}+\gamma^nV(S_{t+n})
$$
The n-step temporal-difference learning updates:
$$
V(S_t)\larr V(S_t)+\alpha(G_t^{(n)}-V(S_t))
$$
where $G_t^{(n)}$ is the *n*-step estimate of the current state.



#### 3.3 $\lambda$-return

We can average *n*-step returns over different *n* to combine information from different time-steps.

The $\lambda$-return $G_t^\lambda$ combines **all** *n*-step returns $G_t^{(n)}$:
$$
G_t^\lambda = (1-\lambda)\sum_{n=1}^\lambda\lambda^{n-1}G_t^{(n)}
$$
where $(1-\lambda)\lambda^{n-1}$ is the geometricly decayed weight for each $\lambda$-return.

- Geometric weighting is used for less memory usage.

| <img src="Lecture 4_MC_TD.assets/Screenshot 2020-06-25 at 07.19.00.png" style="zoom:60%;" /> |
| :----------------------------------------------------------: |
| **Fig 4.4** Geometric decay of weighting function of TD($\lambda$) |



#### 3.4 Forward-view TD($\lambda$)

Like MC, forward-view TD($\lambda$):

- Update value function towards the $\lambda$-return.
- Looks into the **future** to compute $G_t^\lambda$.
- Can only be computed from **complete** episodes.

To achieve properties of temporal-difference learning, we use **backward-view** TD($\lambda$):

- Provides **mechanism** than theory.
- Update online every step.
- Can be computed from incomplete sequences.



#### 3.5 Eligibility traces

Credit assignment problem: Did bell or light cause shock?

| <img src="Lecture 4_MC_TD.assets/Screenshot 2020-06-25 at 07.28.50.png" style="zoom:80%;" /> |
| :----------------------------------------------------------: |
|            **Fig 4.5** Credit assignment problem             |



- **Frequency** heuristic: Assign credit to most frequent states.
- **Recency** heuristic: Assign credit to most recent states.

Eligibility traces combine both  heuristics:
$$
\begin{align} E_0(s) &=0 \\ E_t(s) &=\gamma\lambda E_{t-1}(s)+\mathbf 1(S_t=s) \end{align}
$$


| <img src="Lecture 4_MC_TD.assets/Screenshot 2020-06-25 at 07.33.14.png" style="zoom:67%;" /> |
| :----------------------------------------------------------: |
|           **Fig 4.6** Eligibility trace of a state           |



#### 3.6 Backward-view TD($\lambda$)

- Keep an eligibility trace for every state *s*.
- Update value $V(s)$ for every state *s*.
- In proportion to TD-error $\delta_t$ and eligibility trace $E_t(s)$:

$$
\begin{align} \delta_t&=R_{t+1}+\gamma V(S_{t+1})-V(S(t)) \\ V(s)&\larr V(s)+\alpha\delta_tE_t(s) \end{align}
$$



| <img src="Lecture 4_MC_TD.assets/Screenshot 2020-06-25 at 07.40.23.png" style="zoom:67%;" /> |
| :----------------------------------------------------------: |
|  **Fig 4.7** Backward-view TD update with eligibility trace  |

When $\lambda=0$, only the current state is updated:
$$
\begin{align}E_t(s)&=\mathbf 1(S_t=s) \\ V(s) &\larr V(s)+\alpha\delta_tE_t(s) \end{align}
$$

- This is exactly equivalent to TD(0) update.

When $\lambda=1$, credit is deferred until end of episode.

- For episodic environments with offline updates, the total update for TD(1) is the same as MC.

**Theorem**:

The sum of offline/ online updates is identical for forward-view and backward-view TD($\lambda$).
$$
\sum_{t=1}^T\alpha\delta_tE_t(s)=\sum_{t=1}^T\alpha(G_t^\lambda-V(S_t))\mathbf 1(S_t=s)
$$


#### 3.7 Summary of forward and backward TD($\lambda$)



|               | $\lambda=0$ |  $\lambda \in(0,1)$   | $\lambda =1$ |
| ------------- | :---------: | :-------------------: | :----------: |
| Backward view |    TD(0)    |     TD($\lambda$)     |    TD(1)     |
| Forward view  |    TD(0)    | Forward TD($\lambda$) |      MC      |
| Exact online  |    TD(0)    |  Exact TD($\lambda$)  | Exact TD(1)  |

