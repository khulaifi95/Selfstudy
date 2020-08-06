# Reinforcement Learning



## Lecture 10: Classic Games



### 1. State of the art

#### 1.1 Why study classic games?

- Simple rules, deep concepts.
- Studied by humans for hundreds or thousands of years.
- Meaningful IQ test for comparing humans and AI.
- *Drosophila* of artificial intelligence.
- Microcosms encapsulating real world issues.
- Games are fun!



#### 1.2 RL in games

| Program    | Level of play | RL program to achieve |
| ---------- | ------------- | --------------------- |
| Checkers   | Superhuman    | *Chinook*             |
| Chess      | Superhuman    | *KnightCap / Meep*    |
| Go         | Superhuman    | *AlphaGo*             |
| Backgammon | Superhuman    | *TG-Gammon*           |
| Poker      | Superhuman    | *SmooCT*              |



### 2. Game theory

#### 2.1 Optimality in games

What is the optimal policy $\pi^i$ for i-th player?

- **Best response** $\pi_*^i(\pi^{-i})$ is optimal policy against other policies if all other players fix their policies $\pi^{-i}$.
- **Nash equilibrium** is a joint policy for all players

$$
\pi^i=\pi^i_*(\pi^{-i}) \ \forall  \ i
$$

​		such that every player's policy is a best response, i.e. no player would choose to deviate from Nash.

- In this course, we only consider the class of games where there is always a single Nash equilibrium.



#### 2.2 SIngle-agent and self-play RL

Best response is solution to single-agent RL problem where:

- Other players become part of the **environment**.
- Game is reduce to a MDP.
- Best response is the optimal policy for this MDP.

Nash equilibrium is **fixed-point** of self-play RL.

- Experience is generated by playing games between agents

$$
a_1 \sim \pi^1, a_2 \sim \pi^2,...
$$

- Each agent learns best response to other players.
- One player's policy determines another player's environment.
- All players are adapting to each other.



#### 2.3 Two-player zero-sum games

We focus on a special class of games that:

- A **perfect information** game is fully observed by all players.
  - Chess, Go have perfect information.
  - Poker, Scrabble have imperfect information (hidden state).

- A **two-player** game has two alternate players.
  - Player 1 - black, player 2 - white.
- A **zero-sum** game has equal and opposite rewards for black and white

$$
R^1+R^2=0
$$

We consider **methods** for finding Nash equilibria in perfect information, two-player zero-sum games:

- Game tree search, i.e. **planning**
- Self-play reinforcement learning



### 3. Minimax search

#### 3.1 Minimax

A value function defines the expected total reward given joint policies $\pi=\left\langle\pi^1,\pi^2\right\rangle$
$$
v_\pi(s)=\mathbb E_\pi [G_t |S_t=s]
$$
A **minimax** value function maximises white's expected return while minimising black's expected return
$$
\begin{align}v_*(s) &= \max_{\pi^1}\min_{\pi^2}v_\pi(s) \\&=\min_{\pi^2}\max_{\pi^1}v_\pi(s)\end{align}
$$
A **minimax policy** is a joint policy $\pi_*=\left\langle\pi_*^1,\pi_*^2\right\rangle$ that achieves the minimax values $v_{\pi_*}(s)=v_*(s)$.

- There is a unique minimax value function for this class of games.
- A minimax policy is a Nash equilibrium.



#### 3.2 Minimax search

Minimax values can be found by depth-first game-tree search.

| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 10_Games.assets/Screenshot 2020-06-22 at 09.32.39.png" style="zoom:33%;" /> |
| :----------------------------------------------------------: |
|               **Fig 10.1** Minimax search tree               |



#### 3.3 Value function in minimax search

- Search tree grows exponentially.
- Impractical to search to the end of the game.

We instead use value function approximator $v(s,\mathbf w)\approx v_*(s)$, aka. evaluation function or heuristic function.

- Use value function to estimate minimax value at leaf nodes.
- Minimax search run to fixed depth with respect to leaf values.



### 4. Self-play reinforcement learning

#### 4.1 Self-play learning methods

We apply value-based RL algorithms to games of self-play.

- **MC**: update value function towards the return $G_t$

$$
\Delta \mathbf w = \alpha(G_t-v(S_t, \mathbf w))\nabla_{\mathbf w}v(S_t,\mathbf w)
$$

- **TD(0)**: update value function towards successor value $v(S{t+1})$

$$
\Delta \mathbf w = \alpha(v(S_{t+1}, \mathbf w)-v(S_t, \mathbf w))\nabla_{\mathbf w}v(S_t, \mathbf w)
$$

- **TD($\lambda$)**: update value function towards the $\lambda$-return $G_t^\lambda$

$$
\Delta \mathbf w = \alpha(G_t^\lambda-v(S_t, \mathbf w))\nabla_{\mathbf w}v(S_t, \mathbf w)
$$



#### 4.2 Policy Improvement with Afterstates

For **deterministic** games, it is sufficient to estimate $v_*(s)$.

This is because we can efficiently evaluate the **afterstate**
$$
q_*(s,a) = v_*(succ(s,a))
$$

- Rules of the game define the successor state $succ(s,a)$.
- Actions are selected e.g. by min/maximising afterstate value:

$$
A_t = \arg\max_a v_*(succ(S_t, a)) \ \ \ \ \ \ \text{for white} \\ A_t = \arg\min_a v_*(succ(S_t, a)) \ \ \ \ \ \ \ \text{for black}
$$

This improves joint policy for both players.



#### 4.3 TD-Gammon

TD-Gammon is an outstanding application of self-play TD learning in Backgammon.

- Neural network initialised with random weights.
- Trained by games of self-play.
- Using non-linear temporal-difference learning

$$
\delta_t = v(S_{t+1}, \mathbf w)-v(S_t,\mathbf w) \\ \Delta\mathbf w = \alpha\delta_t\nabla_\mathbf wv(S_t, \mathbf w)
$$

- Greedy policy improvement without exploration.
  - Dice roll provides enough stochastic property and a smooth value function.
- Algorithm always converged in practice, not true for other games.



### 5. Combining RL and minimax search

#### 5.1 Simulation-based search

Self-play reinforcement learning can replace search procedure.

- Idea: simulate games of self-play from root state $S_t$, i.e. **now**.

We then apply RL to simulated experience.

- Monte-Carlo control $\rightarrow$ Monte-Carlo tree search.
- Most effective variant: UCT algorithm.
  - Balance exploration and exploitation in each node using UCB.
- Self-play UCT converges on minimax values.



#### 5.2 Performance of MCTS

Monte-Carlo tree search is the best performing method in many challenging games.

- Go
- Hex

In many games, simple Monte-Carlo search is enough.

- Scrabble
- Backgammon



#### 5.3 Game-tree search in imperfect information games

Players have different information states and therefore **separate** search trees.

- One node for each information state summarising what a player knows.
- Many real states may share the same information state.
- Can aggregate states e.g. with similar value.

Information-state game tree may be solved by:

- Iterative forward-search methods
  - Counterfactual regret minimisation
- Self-play reinforcement learning
  - Smooth UCT



| <img src="/Users/kevinxu95/Selfstudy/Reinforcement Learning/Notes/Lecture 10_Games.assets/Screenshot 2020-06-22 at 11.25.55.png" style="zoom:75%;" /> |
| :----------------------------------------------------------: |
|        **Fig 10.2** Separate search trees for players        |



#### 5.4 Successful recipe for RL in games



| Program    | Input features           | Value function | RL            | Training         | Search             |
| ---------- | ------------------------ | -------------- | ------------- | ---------------- | ------------------ |
| Chess      | Binary: pieces           | Linear         | TreeStrap     | Self-play/expert | $\alpha\beta$      |
| Checkers   | Binary: pieces           | Linear         | TD leaf       | Self-play        | $\alpha\beta$      |
| Othello    | Binary: disc configs     | Linear         | MC            | Self-play        | $\alpha\beta$      |
| Backgammon | Binary: # checkers       | NN             | TD($\lambda$) | Self-play        | $\alpha\beta$ / MC |
| Go         | Binary: stone patterns   | Linear         | TD            | Self-play        | MCTS               |
| Scrabble   | Binary: letters on rack  | Linear         | MC            | Self-play        | MC search          |
| Hold'em    | Binary: card abstraction | Linear         | MCTS          | Self-play        | MCTS               |
