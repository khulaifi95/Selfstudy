# Reinforcement Learning



## Lecture 6: Value Function Approximation



### 1. Introduction

#### 1.1 Large-scale reinforcement learning

Reinforcement learning can be used to solve *large* problems, e.g.

- Backgammon: $10^{20}$ states.
- Computer Go: $10^{170}$ states.
- Helicopter: continuous state space.

We need to find a way to scale up the model-free methods for *prediction* and *control*.



#### 1.2 Value function approximation

So far we have represented value function by a *lookup table*.

- Every state *s* has an entry $V(s)$.
- Or every state-action pair *s, a* has an entry $Q(s,a)$.

**Problems**:

1. Too many states and/ or actions to store in memory.
2. It is too slow to learn the value of each state individually.

**Solutions**:

- We estimate value function with **function approximation**

$$
\hat v(s,\mathbf w)\approx v_\pi(s) \\ or \ \ \hat q(s,a,\mathbf w) \approx q_\pi(s,a)
$$

- **Generalise** from seen states to unseen states.
- Update parameter $\mathbf w$ using MC or TD learning.



#### 1.3 Type of function approximators

| <img src="Lecture 6_Func_Approx.assets/Screenshot 2020-06-26 at 08.57.20-3158306.png" style="zoom:60%;" /> | <img src="Lecture 6_Func_Approx.assets/Screenshot 2020-06-26 at 08.57.24.png" style="zoom:60%;" /> | <img src="Lecture 6_Func_Approx.assets/Screenshot 2020-06-26 at 08.57.30.png" style="zoom:60%;" /> |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|                                                              |                  **Fig 6.1** 3 types of FA                   |                                                              |



We consider **differentiable** function approximators:

- Linear combinations of features.
- Neural network.

We require a training method that is suitable for **non-stationary, non-iid** data.



### 2. Incremental methods

#### 2.1 Gradient descent

Let $J(w)$ be a differentiable function of parameter vector $\mathbf w$.

- Define the **gradient** of $J(w)$ to be

$$
\nabla_\mathbf wJ(\mathbf w)=\pmatrix{\frac{\partial J(\mathbf w)}{\partial \mathbf w_1} \\ \vdots \\ \frac{\partial J(\mathbf w)}{\partial \mathbf w_n}}
$$

- Optimise to find a local minimum of $J(\mathbf w)$.
- Adjust $\mathbf w$ in direction of $-ve$ gradient

$$
\Delta_w= -\frac12 \alpha \nabla_\mathbf wJ(\mathbf w)
$$

​		where $\alpha$ is a step-size parameter.



#### 2.2 Value function approximation by SGD

- Goal: find parameter vector $\mathbf w$ minimising mean-squared error between approximate value function $\hat v(s,\mathbf w)$ and true value function $v_\pi(s)$, where

$$
J(\mathbf w) = \mathbb E_\pi[(v_\pi(S)-\hat v(S,\mathbf w))^2]
$$

- Gradient descent finds a local minimum

$$
\begin{align}\Delta \mathbf w &= -\frac12\alpha\nabla_\mathbf wJ(\mathbf w) \\&=\alpha \mathbb E_\pi[(v_\pi(S)-\hat v(S,\mathbf w))\nabla_\mathbf w\hat v(S,\mathbf w)] \end{align}
$$

- Stochastic gradient descent **samples** the gradient

$$
\Delta \mathbf w = \alpha(v_\pi(S)-\hat v(S,\mathbf w))\nabla_\mathbf w\hat v(S,\mathbf w)
$$

​		where the **expected** update is equal to full gradient update.



#### 2.3 Linear value function approximation

- We represent state by a **feature vector**

$$
\mathbf x(S) = \pmatrix{\mathbf x_1(S) \\ \vdots\\ \mathbf x_n(S)}
$$

​		e.g. distance of robot to landmarks, trends in the stock market, piece and pawn in chess.

- Represent value function by a **linear combination** of features

$$
\hat v(S,\mathbf w) = \mathbf x(S)^T\mathbf w= \sum_{j=1}^n\mathbf x_j(S)\mathbf w_j
$$

- The objective function $J(\mathbf w)$ is quadratic in parameters $\mathbf w$.
- Thus SGD converges on **global optimum**.
- Update is *step-size* $\times$ *prediction error* $\times$ *feature value*:

$$
\nabla_\mathbf w\hat v(S,\mathbf w) = \mathbf x(S) \\ \Delta \mathbf w = \alpha(v_\pi(S)-\hat v(S,\mathbf w))\mathbf x(S)
$$



#### 2.4 Table lookup features

Table lookup is a special case of linear value function approximation.

- It uses table lookup features:

$$
\mathbf x^{table}(S) = \pmatrix{\mathbf 1(S=s_1)\\ \vdots \\ \mathbf 1(S=s_n)}
$$

- Parameter vector $\mathbf w$ gives value of each individual state:

$$
\hat v(S,\mathbf w)=\pmatrix{\mathbf 1(S=s_1)\\ \vdots \\ \mathbf 1(S=s_n)}\cdot\pmatrix{\mathbf w_1\\ \vdots \\ \mathbf w_n}
$$



### 3. Incremental prediction

#### 3.1 Incremental prediction algorithms

In the above sections, we have assumed true value function $v_\pi(s)$ given by supervisor.

- In RL, there is no supervisor, only rewards.

In practice, we substitute a **target** for $v_\pi(s)$.

- For MC, the target is the return $G_t$

$$
\Delta \mathbf w=\alpha(G_t-\hat v(S_t, \mathbf w))\nabla_\mathbf w\hat v(S_t, \mathbf w)
$$

- For TD, the target is the TD target $R_{t+1}+\gamma \hat v(S_{t+1}, \mathbf w)$

$$
\Delta \mathbf w=\alpha(R_{t+1}+\gamma \hat v(S_{t+1}, \mathbf w)-\hat v(S_t, \mathbf w))\nabla_\mathbf w\hat v(S_t, \mathbf w)
$$

- For TD($\lambda$), the target is the $\lambda$-return $G_t^\lambda$

$$
\Delta \mathbf w=\alpha(G_t^\lambda-\hat v(S_t,\mathbf w))\nabla_\mathbf w\hat v(S_t, \mathbf w)
$$



#### 3.2 Monte-Carlo with value function approximation

The return $G_t$ is an **unbiased**, **noisy** sample of true value $v_\pi(S_t)$.

- We can therefore apply supervised learning to the online *training data*:

$$
\left\langle S_1, G_1\right\rangle, \left\langle S_2, G_2\right\rangle, ..., \left\langle S_T, G_T\right\rangle
$$

- For example, using linear MC policy evaluation:

$$
\begin{align}\Delta \mathbf w&=\alpha(G_t-\hat v(S_t, \mathbf w))\nabla_\mathbf w\hat v(S_t, \mathbf w) \\ &= \alpha(G_t-\hat v(S_t, \mathbf w))\mathbf x(S_t) \end{align}
$$

- MC evaluation converges to a **local** optimum.
  - Even when using non-linear approximators.



#### 3.3 TD learning with value function approximation

The TD target $R_{t+1}+\gamma \hat v(S_{t+1}, \mathbf w)$ is a **biased** sample of true value $v_\pi(S_t)$.

- We can still apply supervised learning to the online *training data*:

$$
\left\langle S_1, R_2+\gamma \hat v(S_2, \mathbf w)\right\rangle, \left\langle S_2, R_3+\gamma \hat v(S_3, \mathbf w)\right\rangle, ..., \left\langle S_{T-1}, R_T\right\rangle
$$

- For example, using linear TD(0):

$$
\begin{align}\Delta \mathbf w&=\alpha(R+\gamma \hat v(S', \mathbf w)-\hat v(S, \mathbf w))\nabla_\mathbf w\hat v(S, \mathbf w) \\ &= \alpha\delta\mathbf x(S)\end{align}
$$

- Linear TD(0) converges **close** to global optimum.



#### 3.4 TD($\lambda$) with value function approximation

The $\lambda$-return $G_t^\lambda$ is also a **biased** sample of true value $v_\pi(s)$.

- We can again apply supervised learning to the online *training data*:

$$
\left\langle S_1, G_1^\lambda\right\rangle, \left\langle S_2, G_2^\lambda\right\rangle, ..., \left\langle S_{T-1}, G_{T-1}^\lambda\right\rangle
$$

- Forward-view linear TD($\lambda$):

$$
\begin{align}\Delta \mathbf w&=\alpha(G_t^\lambda-\hat v(S_t, \mathbf w))\nabla_\mathbf w\hat v(S_t, \mathbf w) \\ &= \alpha(G_t^\lambda-\hat v(S_t, \mathbf w))\mathbf x(S_t) \end{align}
$$

- Backward-view linear TD($\lambda$):

$$
\begin{align}\delta_t&=R_{t+1}+\gamma\hat v(S_{t+1}, \mathbf w)-\hat v(S_t, \mathbf w) \\ E_t&=\gamma \lambda E_{t-1}+\mathbf x(S_t) \\ \Delta\mathbf w&= \alpha\delta_tE_t \end{align}
$$

Forward and backward view linear TD($\lambda$) are **equivalent**.



#### 3.5 Convergence of prediction algorithms

- TD does not follow the gradient of **any** objective function.
- That is the reason why TD can diverge when off-policy or using non-linear approximators.
- **Gradient TD** follows true gradient of projected Bellman error.

| On/off-policy  |  Algorithm  | Table lookup |    Linear    |  Non-linear  |
| :------------: | :---------: | :----------: | :----------: | :----------: |
|                |     MC      | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| **On-policy**  |     TD      | $\checkmark$ | $\checkmark$ |   $\times$   |
|                | Gradient TD | $\checkmark$ | $\checkmark$ | $\checkmark$ |
|                |     MC      | $\checkmark$ | $\checkmark$ | $\checkmark$ |
| **Off-policy** |     TD      | $\checkmark$ |   $\times$   |   $\times$   |
|                | Gradient TD | $\checkmark$ | $\checkmark$ | $\checkmark$ |



### 4. Incremental control

#### 4.1 Control with value function approximation

| <img src="Lecture 6_Func_Approx.assets/Screenshot 2020-06-26 at 10.49.05.png" style="zoom:67%;" /> |
| :----------------------------------------------------------: |
|    **Fig 6.2** Control with value function approximation     |

From general policy iteration,

- Policy evaluation: **Approximate** policy evaluation, $\hat q(\cdot,\cdot, \mathbf w)\approx q_\pi$.
- Policy improvement: $\epsilon$-greedy policy improvement.



#### 4.2 Aciton-value function approximation

We can also approximate the action-value function
$$
\hat q(S,A,\mathbf w)\approx q_\pi(S,A)
$$

- Minimise mean-squared error between approximate action-value function $\hat q(S,A,\mathbf w)$ and true action-value function $q_\pi(S,A)$:

$$
J(\mathbf w) = \mathbb E_\pi[(q_\pi(S,A)-\hat q(S,A,\mathbf w))^2]
$$

- SGD finds a local minimum:

$$
-\frac12\nabla_\mathbf wJ(\mathbf w)=(q_\pi(S,A)-\hat q(S,A,\mathbf w))\nabla_\mathbf w\hat q(S,A,\mathbf w) \\ \Delta\mathbf w =\alpha(q_\pi(S,A)-\hat q(S,A,\mathbf w))\nabla_\mathbf w\hat q(S,A,\mathbf w)
$$



#### 4.3 Linear action-value function approximation

- We represent **state and action** by a feature vector

$$
\mathbf x(S,A) = \pmatrix{\mathbf x_1(S,A) \\ \vdots \\ \mathbf x_n(S,A)}
$$

- Represent action-value function by linear combination of features:

$$
\hat q(S,A,\mathbf w) = \mathbf x(S,A)^T\mathbf w= \sum_{j=1}^n\mathbf x_j(S,A)\mathbf w_j
$$

- SGD updates:

$$
\nabla_\mathbf w\hat q(S,A,\mathbf w) = \mathbf x(S,A) \\ \Delta\mathbf w =\alpha(q_\pi(S,A)-\hat q(S,A,\mathbf w))\mathbf x(S,A)
$$



#### 4.4 Incremental control algorithms

Like prediction, we must substitute a **target** for $q_\pi(S,A)$.

- For MC, the target is the return $G_t$

$$
\Delta \mathbf w=\alpha(G_t-\hat q(S_t, A_t, \mathbf w))\nabla_\mathbf w\hat q(S_t, A_t, \mathbf w)
$$

- For TD(0), the target is the TD target $R_{t+1}+\gamma Q(S_{t+1}, A_{t+1})$

$$
\Delta \mathbf w=\alpha(R_{t+1}+\gamma \hat q(S_{t+1}, A_{t+1}, \mathbf w)-\hat q(S_t, A_t, \mathbf w))\nabla_\mathbf w\hat q(S_t, A_t, \mathbf w)
$$

- For forward-view TD($\lambda$), the target is the action-value $\lambda$-return

$$
\Delta \mathbf w=\alpha(q_t^\lambda-\hat q(S_t, A_t, \mathbf w))\nabla_\mathbf w\hat q(S_t, A_t, \mathbf w)
$$

- For backward-view TD($\lambda$), equivalent update is

$$
\begin{align}\delta_t&=R_{t+1}+\gamma\hat q(S_{t+1}, A_{t+1}, \mathbf w)-\hat q(S_t, A_t, \mathbf w) \\ E_t&=\gamma \lambda E_{t-1}+\nabla_\mathbf w\hat q(S_t, A_t, \mathbf w) \\ \Delta\mathbf w&= \alpha\delta_tE_t \end{align}
$$



#### 4.5 Study of $\lambda$: should we bootstrap?

Empirically, tests across different environments show that there is often a sweet spot of $\lambda=0.9$ between TD and MC methods.

| <img src="Lecture 6_Func_Approx.assets/Screenshot 2020-06-26 at 11.17.22.png" style="zoom:67%;" /> |
| :----------------------------------------------------------: |
|          **Fig 6.3** Sweet spots between MC and TD           |



#### 4.6 Convergence of control algorithms

| Algorithm           | Table lookup |     Linear     | Non-linear |
| :------------------ | :----------: | :------------: | :--------: |
| Monte-Carlo Control | $\checkmark$ | $(\checkmark)$ |  $\times$  |
| Sarsa               | $\checkmark$ | $(\checkmark)$ |  $\times$  |
| Q-learning          | $\checkmark$ |    $\times$    |  $\times$  |
| Gradient Q-learning | $\checkmark$ |  $\checkmark$  |  $\times$  |

where $(\checkmark)$ means the result chatters around near-optimal value function.



### 5. Batch methods

- Gradient descent is simple and appealing but it is not **sample efficient**.
- Batch methods seek to find the best fitting value function given the agent's **experience**.



#### 5.1 Least squares prediction

- Given value function approximation $\hat v(s,\mathbf w)\approx v_\pi(s)$.

- And **experience** $\mathcal D$ i.e. empirical distribution consisting of $\left\langle state, value\right\rangle$ pairs:

$$
\mathcal D = \{\left\langle s_1,v_1^\pi\right\rangle, \left\langle s_2,v_2^\pi\right\rangle, ..., \left\langle s_T,v_T^\pi\right\rangle\}
$$

**Least squares** algorithms find parameters $\mathbf w$ minimising sum-squared error between $\hat v(s_t, \mathbf w)$ and target values $v_t^\pi$:
$$
LS(\mathbf w) = \sum_{t=1}^T(v_t^\pi-\hat v(s_t,\mathbf w))^2 \\ = \mathbb E_\mathcal D[(v^\pi - \hat v(s,\mathbf w))^2]
$$



#### 5.2 SGD with experience replay

We can utilise the agent's experience of past states to find least squares solution.

- Given experience consisting of $\left\langle state, value\right\rangle$ pairs

$$
\mathcal D = \{\left\langle s_1,v_1^\pi\right\rangle, \left\langle s_2,v_2^\pi\right\rangle, ..., \left\langle s_T,v_T^\pi\right\rangle\}
$$

Repeat:

1. Sample state, value from experience

$$
\left\langle s, v^\pi\right\rangle \sim \mathcal D
$$

2. Apply stochastic gradient descent update

$$
\Delta \mathbf w= \alpha(v^\pi-\hat v(s,\mathbf w))\nabla_\mathbf w\hat v(s,\mathbf w)
$$

Converges to least squares solution:
$$
\mathbf w^\pi = \arg\min_\mathbf wLS(\mathbf w)
$$



#### 5.3 Experience replay in DQN

Deek Q-Networks use experience replay and **fixed Q-targets**.

- Take action $a_t$ according to $\epsilon$-greedy policy.
- Store transition $(s_t,a_t,r_{t+1}, s_{t+1})$ in **replay memory** $\mathcal D$.
- Sample random **mini-batch** of transitions $(s,a,r,s')$ from $\mathcal D$.
- Compute Q-learning targets *w.r.t.* **fixed** old parameters $w^-$.
- Optimise MSE between Q-network and Q-learning targets

$$
\mathcal L_i(w_i) = \mathbb E_{s,a,r,s'\sim \mathcal D}\Bigg[\Big(r+\gamma \max_{a'}Q(s',a';w_i^-)-Q(s,a;w_i)\Big)^2\Bigg]
$$

- Using variants of SGD.



#### 5.4 DQN in Atari game

- End-to-end learning of values $Q(s,a)$ from pixels *s*.
- **Input** state *s* is stack of raw pixels from last 4 frames.
- **Output** is $Q(s,a)$ for 18 joystick/ button positions.
- **Reward** is change in score for that step.

Note: Network architecture and hyperparameters are fixed across all games.

It shows that experience replay with fixed Q target gives the best result.

| <img src="Lecture 6_Func_Approx.assets/Screenshot 2020-06-27 at 20.01.08.png" style="zoom:67%;" /> |
| :----------------------------------------------------------: |
|       **Fig 6.4** Network architecture of DQN in Atari       |



#### 5.5 Linear least squares prediction

- Experience replay finds least squares solution, but it may take many iterations.
- Using **linear** value function approximation, we can solve the least squares solution directly.

$$
\hat v(s,\mathbf w) = \mathbf x(s)^T\mathbf w
$$

-  At minimum of $LS(\mathbf w)$, the expected update must be zero:

$$
\begin{align}\mathbb E_\mathcal D[\Delta\mathbf w]&=0 \\ \alpha\sum_{t=1}^T\mathbf x(s_t)(v_t^\pi-\mathbf x(s_t)^T\mathbf w)&=0 \\ \sum_{t=1}^T\mathbf x(s_t)v_t^\pi &= \sum_{t=1}^T\mathbf x(s_t)\mathbf x(s_t)^T\mathbf w \\ \mathbf w &= \Big(\sum_{t=1}^T\mathbf x(s_t)\mathbf x(s_t)^T \Big)^{-1}\sum_{t=1}^T\mathbf x(s_t)v_t^\pi \end{align}
$$

- For N features, direct solution time is $O(N^3)$.
- Incremental solution time is $O(N^2)$ using Shermann-Morrison.



#### 5.6 Linear least squares prediction algorithms

In practice, we do not know true values $v_t^\pi$. The *training data* must use noisy or biased samples of $v_t^\pi$.

- LSMC:

$$
0 = \sum_{t=1}^T\alpha(G_t-\hat v(S_t, \mathbf w))\mathbf x(S_t) \\ \mathbf w = \Big(\sum_{t=1}^T\mathbf x(S_t)\mathbf x(S_t)^T\Big)^{-1}\sum_{t=1}^T\mathbf x(S_t)G_t
$$

- LSTD:

$$
0 = \sum_{t=1}^T\alpha(R_{t+1}+\gamma \hat v(S_{t+1},\mathbf w)-\hat v(S_t, \mathbf w))\mathbf x(S_t) \\ \mathbf w = \Big(\sum_{t=1}^T\mathbf x(S_t)(\mathbf x(S_t)-\gamma \mathbf x(S_{t+1}))^T\Big)^{-1}\sum_{t=1}^T\mathbf x(S_t)R_{t+1}
$$



- LSTD($\lambda$):

$$
0 = \sum_{t=1}^T\alpha\delta_tE_t \\ \mathbf w = \Big(\sum_{t=1}^T E_t(\mathbf x(S_t)-\gamma \mathbf x(S_{t+1}))^T\Big)^{-1}\sum_{t=1}^TE_tR_{t+1}
$$

- LSTD has better convergence over TD with linear function approximation.



#### 5.7 Least squares policy iteration

| <img src="Lecture 6_Func_Approx.assets/Screenshot 2020-06-27 at 20.19.57.png" style="zoom:67%;" /> |
| :----------------------------------------------------------: |
|          **Fig 6.5** Least squares policy iteration          |

- Policy evaluation: least squares Q-learning.
- Policy improvement: greedy policy improvement.



#### 5.8 Least squares control

To evaluate $q_\pi(S,A)$, we must learn **off-policy**.

- For policy evaluation, we want to efficiently use all experience.
- For control, we also want to improve the policy.
- Thus the experience is generated from **many policies**.

We use the same idea as Q-learning:

- Use experience generated by old policy $(s,a,r,s')\sim \pi_{old}$.
- Consider alternative successor action $A'=\pi_{new}(S_{t+1})$.
- Update $\hat q(S_t,A_t,\mathbf w)$ towards value of alternative action $R_{t+1}+\gamma\hat q(S_{t+1}, A',\mathbf w).$



#### 5.9 Least squares policy iteration algorithm

- Least squares Q-learning algorithm (LSTDQ) solves for total update equals  to zero.
- Least squares policy iteration algorithm re-evaluated experience $\mathcal D$ with **different policies**.
- LSPI converges to **near-optimal** value function.

**LSPI-TD($\mathcal D, \pi_0$)**:

> $\pi'\larr \pi_0$
>
> **Repeat**
>
> ​		$\pi \larr \pi'$
>
> ​		$Q\larr LSTDQ(\pi,\mathcal D)$
>
> ​		**for all** $s\in\mathcal S$ **do**
>
> ​				$\pi'(s)\larr \arg\max\limits_{a\in \mathcal A}Q(s,a)$
>
> ​		**end for**
>
> **Until** ($\pi\approx \pi'$)



