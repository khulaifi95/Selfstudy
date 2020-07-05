# Reinforcement Learning



## Lecture 7: Policy Gradient



### 1. Introduction

#### 1.1 Policy-based reinforcement learning

In the last lecture, we approximated the **value** or action-value function using parameters $\theta$
$$
V_\theta(s)\approx V^\pi(s) \\ Q_\theta(s,a) \approx Q^\pi(s,a)
$$

- A policy is then generated directly from the value fuction using $\epsilon$-greedy.

In this lecture, we will directly parametrise the **policy**
$$
\pi_\theta(s,a) = \mathbb P[a|s,\theta]
$$

- We will focus again on **model-free** reinforcement learning.



#### 1.2 Value-based and policy-based RL

- Value-based RL:
  - Learnt value function.
  - **Implicit** policy e.g. $\epsilon$-greedy.
- Policy-based RL:
  - No value function.
  - **Learnt** policy.
- Actor-Critic:
  - Learnt value function.
  - Learnt policy.



#### 1.3 Properties of policy-based RL

Advantages:

- Better **convergence** properties.
- Effective in **high-dimensional** or continuous action spaces.
- Can learn **stochastic** policies.

Disadvantages:

- Typically converge to a **local** rather than global optimum.
- **Evaluating** a policy is usually inefficient and high variance.



#### 1.4 Aliased gridworld example



| <img src="Lecture 7_Policy_Gradient.assets/Screenshot 2020-07-03 at 00.30.05.png" style="zoom:50%;" /> | <img src="Lecture 7_Policy_Gradient.assets/Screenshot 2020-07-03 at 00.30.14.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                **Fig 7.1** Aliased gridworld                 |                                                              |

In the aliased gridworld, the agent's goal is to achieve the gold.

- The agent cannot differentiate the grey states.
- Consider features of the following form for all actions N, E, S, W:

$$
\phi(s,a) = \mathbf 1(\text{wall to N, a = move E})
$$

- Compare value-based RL, using an approximate value function

$$
Q_\theta(s,a) = f(\phi(s,a), \theta)
$$

- For policy-based RL, use a parametrised policy

$$
\pi_\theta(s,a) = g(\phi(s,a),\theta)
$$

Consider the policy under aliasing:

- An optimal **deterministic** policy will either move E/ W in both grey states.

  - Either way, it can get stuck and never reach the money.
  - Value-based RL learns a near-deterministic policy.
  - It will traverse the corridor for a long time.

- An optimal **stochastic** policy will randomly move E/ W in grey states:
  $$
  \pi_\theta(\text{wall to N and S, move E}) = 0.5 \\ \pi_\theta(\text{wall to N and S, move W}) = 0.5
  $$

  - It will reach the goal state in a few steps with high probability.
  - Policy-based RL can learn the optimal stochastic policy.



#### 1.5 Policy objective functions

The goal is to find the best parameters $\theta$ given policy $\pi_\theta(s,a)$.

How do we **measure** the quality of a policy $\pi_\theta$?

- In *episodic* environments, we can use the **start value**:

$$
J_1(\theta) = V^{\pi_\theta}(s_1) = \mathbb E_{\pi_\theta}[v_1]
$$

- In *continuing* environments, we can use the **average value**:

$$
J_{avV}(\theta) = \sum_sd^{\pi_\theta}(s)V^{\pi_\theta}(s)
$$

- Or the **average reward** per time-step:

$$
J_{avR}(\theta) = \sum_sd^{\pi_\theta}(s)\sum_a\pi_\theta(s,a)\mathcal R_s^a
$$

​		where $d^{\pi_\theta}(s)$ is **stationary distribution** of Markov chain for $\pi_\theta$.



#### 1.6 Policy optimisation

Policy-based reinforcement learning is an **optimisation** problem.

- Find parameters $\theta$ that maximises objective function $J(\theta)$.
- Approaches do not use gradient:
  - Hill climbing.
  - Simplex/ amoeba/ Nelder Mead.
  - Genetic algorithms.
- Greater efficiency often possible using gradient:
  - **Gradient descent**.
  - Conjugate gradient.
  - Quasi-Newton.

We mainly focus on gradient descent and methods that exploit **sequential** structure.



### 2. Finite difference policy gradient

#### 2.1 Policy gradient

Policy gradient algorithms search for a *local* maximum in any policy objective function $J(\theta)$ by **ascending** the gradient of the policy *w.r.t.* parameters $\theta$
$$
\Delta\theta=\alpha\nabla_\theta J(\theta)
$$
where $\nabla_\theta J(\theta)$ is the **policy gradient** and $\alpha$ is a step-size parameter.



#### 2.2 Computing gradients by finite differences

To evaluate policy gradient of $\pi_\theta(s,a)$,

- For each dimension $k\in[1,n]$, estimate *k*-th partial derivative *w.r.t.* $\theta$:
  - Perturbing $\theta$ of small amount $\epsilon$ in *k*-th dimension

$$
\frac{\partial J(\theta)}{\partial \theta_k}\approx \frac{J(\theta+\epsilon \mathbf u_k)-J(\theta)}{\epsilon}
$$

​				where $\mathbf u_k$ is the **unit vector** with 1 in *k*-th component, 0 elsewhere.

- Uses $n$ evaluations to compute policy gradient in $n$ dimensions.

This method is simple, noisy and inefficient, but sometimes effective.

- Can work for arbitrary policies, even if policy is not differentiable.



### 3. Monte-Carlo policy gradient

#### 3.1 Likelihood ratios

We now compute the policy gradient **analytically**. 

Assume that:

- Policy $\pi_\theta$ is differentiable whenever it is non-zero.
- The gradient is known $\nabla_\theta\pi_\theta(s,a)$.

**Likelihood ratios** exploit the following identity:
$$
\begin{align} \nabla_\theta\pi_\theta(s,a) &= \pi_\theta(s,a)\frac{\nabla_\theta\pi_\theta(s,a)}{\pi_\theta(s,a)} \\ &= \pi_\theta(s,a)\cdot\nabla_\theta \log\pi_\theta(s,a) \end{align}
$$
where $\nabla_\theta\log\pi_\theta(s,a)$ is the **score function**.



#### 3.2 Softmax policy

We can use a softmax policy as an example.

- **Weight** actions using linear combination of features $\phi(s,a)^T\theta$.
- Probability of action is proportional to exponentiated weight

$$
\pi_\theta(s,a) \propto e^{\phi(s,a)^T\theta}
$$

- The score function is :

$$
\nabla_\theta\log\pi_\theta(s,a) = \phi(s,a)-\mathbb E_{\pi_\theta}[\phi(s,\cdot)]
$$



#### 3.3 Gaussian policy

In continuous action spaces, a Gaussian policy is natural.

- **Mean** is a linear combination of state features $\mu(s)= \phi(s)^T\theta$.
- **Variance** may be fixed $\sigma^2$, can also be parametrised.
- The policy is a Gaussian distribution $\sim\mathcal N(\mu(s),\sigma^2)$.
- The score function is:

$$
\nabla_\theta\log\pi_\theta(s,a) = \frac{(a-\mu(s))\phi(s)}{\sigma^2}
$$



#### 3.3 Policy gradient theorem

We use likelihood ratios to compute the policy gradient.

- In a simple class of **one-step** MDPs:

$$
\begin{align} J(\theta) &= \mathbb E_{\pi_\theta}[r] \\ &= \sum_{s\in\mathcal S}d(s)\sum_{a\in\mathcal A}\pi_\theta(s,a)\mathcal R_s^a \\ \nabla_\theta J(\theta) &= \sum_{s\in\mathcal S}d(s)\sum_{a\in\mathcal A}\pi_\theta(s,a)\nabla_\theta\log\pi_\theta(s,a)\mathcal R_s^a \\ &= \mathbb E_{\pi_\theta}[\nabla_\theta\log\pi_\theta(s,a)r] \end{align}
$$

The **policy gradient theorem** generalises the likelihood ratio approach to full MDPs.

- Replaces instantaneous reward $r$ with long-term value $Q^\pi(s,a)$.
- It applies to start state, average reward and average value objectives.

**Theorem**:

For any differentiable policy $\pi_\theta(s,a),$ any of the policy objective functions $J = J_1, J_{avR}, \frac1{1-\gamma}J_{avV}$, the policy gradient is given as:
$$
\nabla_\theta J(\theta) = \mathbb E_{\pi_\theta}[\nabla_\theta\log\pi_\theta(s,a)Q^{\pi_\theta}(s,a)]
$$

#### 3.4 Monte-Carlo policy gradient

| REINFORCE                                                    |
| ------------------------------------------------------------ |
| **Initialise** $\theta$ arbitrarily                          |
| **For** each episode $\{s_1,a_1,r_2,...,s_{T-1},a_{T-1},r_{T}\} \sim \pi_\theta$ do |
| **For** $t=1 \to T-1$ do                                     |
| $\theta \larr \theta+\alpha\nabla_\theta\log\pi_\theta(s_t,a_t)v_t$ |
| **End for**                                                  |
| **End for**                                                  |
| **End**                                                      |

- Update parameters by stochastic gradient descent.
- Use policy gradient theorem.
- Use return $v_t$ as an **unbiased** sample of $Q^{\pi_\theta}(s_t,a_t)$.



### 4. Actor-Critic

#### 4.1 Reducing variance using a critic

Since Monte-Carlo policy gradient still has high **variance**, we use a **critic** to estimate the action-value function
$$
Q_w(s,a)\approx Q^{\pi_\theta}(s,a)
$$
Actor-Critic algorithms maintain two sets of parameters:

- **Critic**: Updates action-value function parameters $w$.
- **Actor**: Updates policy parameters $\theta$, in direction suggested by critic.

Actor-Critic algorithms follow an **approximate** policy gradient
$$
\nabla_\theta J(\theta) \approx \mathbb E_{\pi_\theta}[\nabla_\theta\log\pi_\theta(s,a)\ Q_w(s,a)] \\ \Delta_\theta = \alpha\nabla_\theta \log\pi_\theta(s,a)\ Q_w(s,a)
$$


#### 4.2 Estimating the action-value function

The critic is solving a familiar problem of policy evaluation.

Solutions were explored in previous lectures, e.g.:

- Monte-Carlo policy evaluation.
- Temporal-difference learning (TD($\lambda$)).
- Least-squares policy evaluation.



#### 4.3 Action-value Actor-Critic

**QAC** is a simple Actor-Critic algorithm based on action-value critic.

It uses linear value function approximation: $Q_w(s,a)=\phi(s,a)^Tw$.

- **Critic**: Updates $w$ by linear TD(0).
- **Actor**: Updates $\theta$ by policy gradient.



| QAC                                                          |
| ------------------------------------------------------------ |
| **Initialise** $s,\theta$                                    |
| Sample $a\sim \pi_\theta$                                    |
| **For** each step do                                         |
| Sample reward $r=\mathcal R_s^a$; sample transition $s'\sim \mathcal P_s^a$ |
| Sample action $a'\sim\pi_\theta(s',a')$                      |
| $\delta = r+\gamma Q_w(s',a')-Q_w(s,a)$                      |
| $\theta = \theta +\alpha\nabla_\theta\log\pi_\theta(s,a)Q_w(s,a)$ |
| $w\larr w+\beta\delta\phi(s,a)$                              |
| $a\larr a', s\larr s'$                                       |
| **End for**                                                  |
| **End**                                                      |



#### 4.4 Bias in Actor-Critic algorithms

- Approximating the policy gradient introduces **bias**.
- A biased policy gradient may not find the right solution.

- If we **choose** value function approximator carefully, we can avoid introducing any bias.
- i.e. We can still follow the **exact** policy gradient.



#### 4.5 Compatible function approximation

**Theorem**:

If the following two conditions are satisfied:

1. Value function approximator is ***compatible*** to the policy

$$
\nabla_wQ_w(s,a)=\nabla_\theta\log\pi_\theta(s,a)
$$

2. Value function parameters $w$ minimise the mean-squared error

$$
ε = \mathbb E_{\pi_\theta}[(Q^{\pi_\theta}(s,a)-Q_w(s,a))^2]
$$

Then the policy gradient is **exact**, i.e.
$$
\nabla_\theta J(\theta) = \mathbb E_{\pi_\theta}[\nabla_\theta\log\pi_\theta(s,a)Q(s,a)]
$$
**Proof**:

If $w$ is chosen to minimise the mean-squared error, gradient of $ε$ *w.r.t.* $w$ must be zero:
$$
\begin{align}\nabla_wε&=0 \\ \mathbb E_{\pi_\theta}[(Q^\theta(s,a)-Q_w(s,a))\nabla_wQ_w(s,a)]&=0 \\ \mathbb E_{\pi_\theta}[(Q^\theta(s,a)-Q_w(s,a))\nabla_\theta \log\pi_\theta(s,a)]&=0 \\ \mathbb E_{\pi_\theta}[Q^\theta(s,a)\nabla_wQ_w(s,a)]&=\mathbb E_{\pi_\theta}[Q_w(s,a)\nabla_wQ_w(s,a)] \end{align}
$$
Thus $Q_w(s,a)$ can be substituted directly into the policy gradient:
$$
\nabla_\theta J(\theta) = \mathbb E_{\pi_\theta}[\nabla_\theta\log\pi_\theta(s,a)Q_w(s,a)]
$$


#### 4.6 Reducing variance using a baseline

We can substract a baseline function $B(s)$ from the policy gradient.

This reduces variance, without changing expectation:
$$
\begin{align} \mathbb E_{\pi_\theta} [\nabla_\theta\log\pi_\theta(s,a)B(s)] &= \sum_{s\in\mathcal S}d^{\pi_\theta}(s)\sum_a\nabla_\theta\pi_\theta(s,a)B(s) \\ &= \sum_{s\in\mathcal S}d^{\pi_\theta}B(s)\nabla_\theta\sum_{a\in\mathcal A}\pi_\theta(s,a)\\ &= 0   \end{align}
$$

- A good baseline is the state value function: $B(s)=V^{\pi_\theta}(s)$.

We can rewrite the policy gradient using the **advantage function** $A^{\pi_\theta}(s,a)$:
$$
A^{\pi_\theta}(s,a) = Q^{\pi_\theta}(s,a)-V^{\pi_\theta}(s) \\ \nabla_\theta J(\theta) = \mathbb E_{\pi\theta}[\nabla_\theta\log\pi_\theta(s,a)\ A^{\pi_\theta}(s,a)]
$$


#### 4.7 Estimating the advantage function

The advantage function can significantly **reduce variance** of policy gradient.

- The **critic** should in fact estimate the advantage function.
- e.g. By estimating **both** $V^{\pi_\theta}\ \text{and}\ Q^{\pi_\theta}$.

Using two function approximators and two parameter vectors,
$$
\begin{align} V_v(s) &\approx V^{\pi_\theta}(s) \\ Q_w(s,a) &\approx Q^{\pi_\theta}(s) \\ A(s,a) &= Q_w(s,a)-V_v(s) \end{align}
$$
Update **both** value functions by e.g. TD learning.

- For the true value function $V^{\pi_\theta}(s)$, the TD error

$$
\delta^{\pi_\theta} = r+\gamma V^{\pi_\theta}(s')-V^{\pi_\theta}(s)
$$

- This is an unbiased estimate of the advantage function

$$
\begin{align} \mathbb E_{\pi_\theta}[\delta^{\pi_\theta}|s,a] &= \mathbb E_{\pi_\theta}[r+\gamma V^{\pi_\theta}|s,a] - V^{\pi_\theta}(s) \\ &= Q^{\pi_\theta}(s,a) - V^{\pi_\theta}(s) \\ &= A^{\pi_\theta}(s,a) \end{align}
$$

- So we can directly **use the TD error** to compute the policy gradient

$$
\nabla_\theta J(\theta) = \mathbb E_{\pi_\theta}[\nabla_\theta\log\pi_\theta(s,a)\delta^{\pi_\theta}]
$$

- In practice, we can use an approximate TD error

$$
\delta_v = r+\gamma V_v(s') -V_v(s)
$$

- This approach only requires **one** set of critic parameters $v$.



#### 4.8 Critics at different time-scales

Critics can estimate value function $V_\theta(s)$ from many targets at different time-scales.

- For MC, the target is the return $v_t$

$$
\Delta\theta = \alpha(v_t-V_\theta(s))\phi(s)
$$

- For TD(0), the target is the TD target $r+\gamma V(s')$

$$
\Delta\theta=\alpha(r+\gamma V(s')-V_\theta(s))\phi(s)
$$

- For forward-view TD($\lambda$), the target is the $\lambda$-return $v_t^\lambda$

$$
\Delta\theta = \alpha(v_t^\lambda-V_\theta(s))\phi(s)
$$

- For backward-view TD($\lambda$), we use eligibility traces

$$
\begin{align} \delta_t &= r_{t+1}+\gamma V(S_{t+1})-V(S_t) \\ e_t &= \gamma\lambda e_{t-1} +\phi(s_t) \\ \Delta\theta &= \alpha\delta_t e_t \end{align}
$$



#### 4.9 Actors at different time-scales

The policy gradient can also be estimated at many time-scales.
$$
\nabla_\theta J(\theta) = \mathbb E_{\pi_\theta}[\nabla_\theta\log\pi_\theta(s,a)\ A^{\pi_\theta}(s,a)]
$$

- Monte-Carlo policy gradient uses error from complete return

$$
\Delta\theta = \alpha(v_t-V_v(s_t))\nabla_\theta\log\pi_\theta(s_t,a_t)
$$

- Actor-Critic policy gradient uses the one-step TD error

$$
\Delta\theta=\alpha(r+\gamma V_v(s_{t+1})-V_v(s_t))\nabla_\theta\log\pi_\theta(s_t,a_t)
$$

- Like forward-view TD($\lambda$), we can mix over time-scales:

$$
\Delta\theta=\alpha(v_t^\lambda-V_v(s_t))\nabla_\theta\log\pi_\theta(s_t,a_t)
$$

​		where $v_t^\lambda-V_v(s_t)$ is a biased estimate of advantage function.

- Like backward-view TD($\lambda$), we can also use eligibility traces.
  - Equivalent to TD($\lambda$), substituting $\phi(s)=\nabla_\theta\log\pi_\theta(s,a)$.
  - Can be updated **online** to **incomplete** sequences.

$$
\begin{align} \delta &= r_{t+1}+\gamma V_v(s_{t+1})-V_v(s_t) \\ e_{t+1} &= \lambda e_t+\nabla_\theta\log\pi_\theta(s,a) \\ \Delta\theta &= \alpha\delta e_t \end{align}
$$



#### 4.10 Alternative policy gradient directions

- Gradient descent algorithms can follow **any** ascent direction.

- A good ascent direction can significantly speed up convergence.
- A policy can often be **reparametrised** without changing action probability.
  - e.g. Increasing score of all actions in a softmax policy.
- The vanilla gradient is sensitive to these reparametrisations.



#### 4.11 Natural policy gradient 

The natural policy gradient is **parametrisation independent**.

It finds ascent direction that is closest to vanilla gradient, when changing policy by a **small**, **fixed** amount:
$$
\nabla^{nat}_\theta\pi_\theta(s,a) = G^{-1}_\theta\nabla_\theta\pi_\theta(s,a)
$$
where $G_\theta$ is the **Fisher information matrix**:
$$
G_\theta = \mathbb E_{\pi_\theta}[\nabla_\theta\log\pi_\theta(s,a)\nabla_\theta\log\pi_\theta(s,a)^T]
$$


#### 4.12 Natural Actor-Critic

- Using compatible function approximation,

$$
\nabla_wA_w(s,a)= \nabla_\theta\log\pi_\theta(s,a)
$$

- The natural policy gradient simplifies as:

$$
\begin{align} \nabla_\theta J(\theta) &= \mathbb E_{\pi_\theta} [\nabla_\theta\log\pi_\theta(s,a)A^{\pi_\theta}(s,a)] \\ &=\mathbb E_{\pi_\theta}[\nabla_\theta\log\pi_\theta(s,a)\nabla_\theta\log\pi_\theta(s,a)^Tw] \\ &= G_\theta w    \end{align}
$$

- i.e. Update actor parameters in direction of critic parameters.



### 5. Summary

The policy gradient has many equivalent forms:
$$
\begin{align} \nabla_\theta J(\theta) &= \mathbb E_{\pi_\theta}[\nabla_\theta\log\pi_\theta(s,a) \ v_t]  & \text{REINFORCE}\\ &= \mathbb E_{\pi_\theta}[\nabla_\theta\log\pi_\theta(s,a) \ Q_w(s,a)]  & \text{Q Actor-Critic} \\ &= \mathbb E_{\pi_\theta}[\nabla_\theta\log\pi_\theta(s,a) \ A_w(s,a)]  & \text{Advantage Actor-Critic} \\ &= \mathbb E_{\pi_\theta}[\nabla_\theta\log\pi_\theta(s,a) \ \delta]  & \text{TD Actor-Critic} \\ &= \mathbb E_{\pi_\theta}[\nabla_\theta\log\pi_\theta(s,a) \ \delta e]  & \text{TD(λ) Actor-Critic} \\ G_\theta^{-1}\nabla_\theta J(\theta) &= w & \text{Natural Actor-Critic}   \end{align}
$$

- Each leads to a stochastic gradient ascent algorithm.
- Critic uses **policy evaluation** to estimate $Q^\pi(s,a), A^\pi(s,a)\ or \ V^\pi(s,a)$.

