# DeepMind x UCL Lectures 



## Lecture 6. Sequences and Recurrent Networks



### 1. Motivation

- Sequences are ollections of elements where:
  - elements can be **repeated**
  - **order** matters
  - of **variable** length

- Sequences are widespread across machine learning applications.

- Not all machine learning models can handle sequential data.



### 2. Fundamentals

Modeling probabilities of sequences scales badly given the non-independent structure of their elements.



#### 2.1 Model scheme comparison with machine learning

|              | Supervised learning                                          | Sequence modeling                                            |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Data         | $\{x, y\}_i$                                                 | $\{x\}_i$                                                    |
| Model        | $y\approx f_\theta(x)$                                       | $p(x)\approx f_\theta(x)$                                    |
| Loss         | $\mathcal L(\theta) = \sum\limits_{i=1}^N l(f_\theta(x_i), y_i)$ | $\mathcal L(\theta) = \sum\limits_{i=i}^N\log p(f_\theta(x_i))$ |
| Optimisation | $\theta^* = \arg\min\limits_\theta\mathcal L(\theta)$        | $\theta^* = \arg\max\limits_\theta\mathcal L(\theta)$        |



#### 2.1 Simplest model

Assuming independence of words, the probability of a sentence $\mathbb x$ given $t$ words:
$$
p(\mathbb x) = \prod_{t=1}^T p(x_t)
$$
However, independence assumption does not match **sequential strcture** of language.



#### 2.2 Realistic model

Assuming conditional dependence of words on previous context:
$$
p(x_T) = p(x_T|x_1, \dots, x_{T-1})
$$
**Scalability issues** exist to include full context of the corpus.

-  Probability of larger contexts will grow with number of words exponentially.



#### 2.3 N-grams

Only condition on $N$ previous words:
$$
p(\mathbb x) = \prod_{t=1}^T p(x_t|x_{t-N-1}, \dots, x_{t-1})
$$
Downsides of using N-grams:

- Does not take into account words that are more than $N$ words away.

- Data table is still very, very large.



### 3. Learning to model word probabilities

#### 3.1 Vectorising the context

The model $f_\theta$ summarises the context in ***h*** such that:
$$
p(x_t|x_1, \dots, x_{t-1})\approx p(x_t|h)
$$

| <img src="Lecture 6.assets/Screenshot_20201115_232424.png" style="zoom:60%;" /> |
| :----------------------------------------------------------: |
|    **Fig 6.1** Vectorising the context with summarisation    |

Desirable properties for $f_\theta$:

- order matters
- variable length
- differentiable
- individual changes can have large effects



#### 3.2 Properties of N-grams as model

|                     |    N-gram    |   Addition   |
| ------------------- | :----------: | :----------: |
| order matters       | $\checkmark$ |   $\times$   |
| variable length     |   $\times$   | $\checkmark$ |
| differentiable      |   $\times$   | $\checkmark$ |
| pairwise encoding   | $\checkmark$ |   $\times$   |
| perserves long-term |   $\times$   | $\checkmark$ |



#### 3.3 Modeling conditional probabilities

Desirable properties for $g_\theta$:

- Individual changes can have large effects
- returns a probability distribution

| <img src="Lecture 6.assets/Screenshot_20201115_233658.png" style="zoom:60%;" /> |
| :----------------------------------------------------------: |
|        **Fig 6.2** Modeling conditional probabilities        |



### 4. Recurrent neural networks

Persistent state variable $\mathbf h$ stores information from the context observed so far:
$$
h_t = tanh(\mathbf W_h\mathbf h_{t-1} + \mathbf W_x\mathbf x_t)
$$
RNNs predict the target $\mathbf y$ (the next word) from the state $\mathbf h$: 
$$
p(\mathbf y_{t+1}) = softmax(\mathbf W_y\mathbf h_t)
$$
Then input the next word in sentence $x_1$, etc.

- Weights are shared over time steps.

| <img src="Lecture 6.assets/Screenshot_20201115_234700.png" style="zoom:60%;" /> |
| :----------------------------------------------------------: |
|             **Fig 6.3** RNN rolled out over time             |

