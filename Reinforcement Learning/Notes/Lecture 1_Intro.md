# Reinforcement Learning

---



## Lecture 1: Introduction

### 1. About RL

Q: What makes RL different from other ML problems?

- No supervisor, only a ***reward*** signal.
- Delayed **feedback**, not instantaneous.
- **Time** really matters, i.e. sequential, non i.i.d data.
- **Agent's** actions affect the data it receives.



### 2. The RL problem

#### 2.1 Rewards

A reward $R_t$ is a **scalar** feedback signal which indicates how well agent is doing at step $t$. 

The agent's job is to **maximise** cumulative reward, based on the *reward hypothesis*:

> All goals can be described by the maximisation of expected cumulative reward.

##### Examples(+/-):

- fly as desired / crash
- winning / losing a game
- investment reward for each $
- produce power / exceed safety thresholds
- forward motion / fall over
- increasing / decreasing game score



#### 2.2 Sequential decision making

- Goal: select actions to maximise total future reward.
- Actions may have long term consequences.
- Reward may be delayed.
- It may be better to sacrifice immediate reward to gain in long-term.



#### 2.3 Agent and environment

1. At each step $t$ the agent:

- Executes action $A_t$
- Receives observation $O_t$
- Receives scalar reward $R_t$

2. The environment:

- Receives action $A_t$
- Emits observation $O_{t+1}$
- Emits scalar reward $R_{t+1}$

3. Time $t$ increments at every step.



| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 1_Intro.assets/Screenshot 2020-05-12 at 04.13.54-9253295.png" alt="Screenshot 2020-05-12 at 04.13.54" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
| **Fig 1.1** Interaction between the environment and the agent |



#### 2.4 History and state

1. The history is the sequence of observations, actions, rewards

$$
H_t = A_1, O_1, R_1, ..., A_t, O_t, R_t
$$

which are all observable variables up to time $t$ of a robot or embodied agent.

- what happens next depends on the **history**:
  - The agent selects actions.
  - The environment selects observations/ reward.

2. **State** is the information used to determine what happens next

$$
S_t = f(H_t)
$$



#### 2.5 Environment state

The environment state $S_t^e$ is the environment's *private* representation.

- the data the environment uses to pick the next observation/ reward
- usually **invisible** to the agent
- may contain **irrelevant** information if visible



#### 2.6 Agent state

The agent state $S_t^a$ is the agent's internal representation.

- the information the agent uses to pick the next action
- the data used by RL algorithms
- can be any function of history:

$$
S_t^a = f(H_t)
$$



#### 2.7 Information state

An information state (Markov state) contains all useful information from the history.

A state $S_t$ is **Markov** if and only if
$$
\mathbb P[S_{t+1}|S_t] = \mathbb P[S_{t+1}|S_1, ...,S_t]
$$

- The *future* is independent of the *past* given the *present*:

$$
H_{1:t} \rightarrow S_t \rightarrow H_{t+1:\infty}
$$

- Once the *state* is known, the *history* may be thrown away.
- The *state* is a **sufficient** statistic of the future.

##### Example:

- The environment state $S_t^e$ is Markov.
- The history $H_t$ is Markov.



| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 1_Intro.assets/Screenshot 2020-05-12 at 04.12.20.png" alt="Screenshot 2020-05-12 at 04.12.20" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|                  **Fig 1.2** Rat experiment                  |

- Agent state?
  - last 3 items - killed
  - counts for lights, bells and levers - cheese
  - Complete sequence - ?



#### 2.8 Fully observable environments

**Full observability** is when agent *directly* observes environment state as it is
$$
O_t=S_t^a=S_t^e
$$
This is a Markov decision process (**MDP**).



#### 2.9 Partially observable environments

**Partial observability** is when agent *indirectly* observes environment. This is a partially observable Markov decision process where agent state $\neq$ environment state.

Agent constructs its own state representation $S_t^a$ with:

- complete history: $S_t^a=H_t$
- **beliefs** of environment state: $S_t^a=(\mathbb P[S_t^e=s^1],...,\mathbb P[S^e_t=s^n])$
- RNN: $S_t^a=\sigma(S_{t-1}^aW_s+O_tW_0)$ as linear combination



### 3. Inside an RL agent

#### 3.1 Major components

An RL agent may include one or more of these components:

- Policy: agent's *behaviour* function
- Value function: how good is each state and / or action
- Model: agent's representation of the environment



#### 3.2 Policy

A policy is the agent's behaviour which is a **map** from state to action.

- deterministic policy: $a=\pi(s)$
- stochastic policy: $\pi(a|s) = \mathbb P[A=a|S=s]$



#### 3.3 Value function

Value function is a prediction of future reward to evaluate the goodness/ badness of states.

- To select between actions:

$$
v_\pi(s) = \mathbb E_\pi[R_t+\gamma R_{t+1} + \gamma^2 R_{t+2}+...|S_t=s]
$$



#### 3.4 Model

A model predicts what the environment will do next.

- Transitions: $\mathcal P$ predicts the next state (i.e. dynamics).
- Rewards: $\mathcal R$ predicts the next immediate reward.

$$
P_{SS'}^a = \mathbb P[S'=s'|S=s, A=a]\\
R_S^a = \mathbb E[R|S=s, A=a]
$$



#### 3.5 Maze example



| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 1_Intro.assets/Screenshot 2020-05-12 at 04.43.45.png" style="zoom:35%;" /> | <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 1_Intro.assets/Screenshot 2020-05-12 at 04.43.58.png" style="zoom:25%;" /> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|      Reward: -1/step, Actions: N/E/S/W, State: location      |              Policy $\pi(s)$ for each state $s$              |
| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 1_Intro.assets/Screenshot 2020-05-12 at 04.44.08.png" style="zoom:25%;" /> | <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 1_Intro.assets/Screenshot 2020-05-12 at 04.44.20.png" style="zoom:30%;" /> |
|              Value $v_\pi(s)$ of each state $s$              | Model of transition $\mathcal P^a_{SS'}$ and next reward $\mathcal R^a_S$ |
|                       **Fig 1.3** Maze                       |                                                              |



#### 3.6 Categorizing RL agents

- Value based

  - no ~~policy~~
  - value function

- Policy based

  - policy
  - no ~~value function~~

- Actor critic

  - policy
  - value function

  

- Model free

  - policy and/or value function
  - no ~~model~~

- Model based

  - policy and/or value function
  - model



| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 1_Intro.assets/Screenshot 2020-05-12 at 04.58.03.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|                **Fig 1.4** RL agent taxonomy                 |



### 4. Problems within RL

#### 4.1 Learning as planning

Two fundamental problems in sequential decision making.

- Learning:
  - environment initially **unknown**
  - agent interacts with environment
  - agent improves its policy
- Planning:
  - model of the environment **known**
  - agent performs computations with its model
  - agent improves its policy



#### 4.2 Exploration and exploitation

Reinforcement learning is like *trial-and-error* learning where the agent should discover a **good policy** from its experiences of the environment without **losing** too much **reward** along the way.

- *Exploration*: finds more information about the environment.
- *Exploitation*: utilises known information to maximise reward.
- It is usually equally important to do both.



#### 4.3 Prediction and control

- Prediction: evaluate the future given a policy.
- Control: optimise the future to find the best policy.

