# 2 Probability

## 2.1 Introduction

> Probability theory is nothing but common sense reduced to calculation. — Pierre Laplace



### 2.1.1 Interpretations of Probability

- **Frequentist**: Long run frequencies of events.

- **Bayesian**: Quantify uncertainty.
  - Related to *information* rather than repeated trials.
  - **Advantage**: Model uncertainty about events that do not have long term frequencies.



## 2.2 A brief review of probability theory

### 2.2.1 Discrete random variables

Define a discrete random variable $X$, which can take on any value from a finite or countably infinite set $\mathcal X$. 

- #### Binary events:

  - $p(A) + p(\bar A) =1$
  - $A = 1 \rightarrow$ True, $A = 0 \rightarrow$ False.

- #### Probability mass function: $p()$

  Denote the probability of event that $X = x$ as $p(X = x)$ or $p(X)$. 

  - $0 \leq p(x) \leq 1$
  - $\sum_{x \in \mathcal X}p(x) = 1$ 

- #### Binary indicator function: $\mathbb I()$

  Denote a degenerate distribution $p(x) = \mathbb I(x =1)$. (*constant*)

  

### 2.2.2 Fundamental rules

1. #### Probability of a union of two events

   Given two events, $A$ and $B$, we define the probability of $A$ or $B$ as follows:
   $$
   \begin{align}
   p(A \or B) &= p(A) + p(B) - p(A \and B) \\
   &= p(A) + p(B) \ \text {if mutually exclusive}
   \end{align}
   $$
   
2. #### Joint probabilities

   We define the probability of the joint event $A$ and $B$ as follows:
   $$
   p(A, B) = p(A \and B) = p(A|B)p(B)
   $$

   - AKA **product rule**. 

   Given a **joint distribution** on two events $p(A,B)$, we define **marginal distribution** as follows:
   $$
   p(A) = \sum\limits_b p(A,B) = \sum\limits_b p(A|B = b)p(B=b)
   $$
   
   The product rule can be applied multiple times to yield the **chain rule** of probability:
   $$
   p(X_{1:D})=p(X_1)p(X_2|X_1)p(X_3|X_1,X_2)...p(X_D|X_{1:D-1})
   $$
   
   
3. #### Conditional probability

   We define the conditional probability of event $A$, given that event $B$ is true, as follows:

$$
p(A|B) = \frac{p(A,B)}{p(B)} \ \text{if} \ \ p(B) > 0
$$



### 2.2.3 Bayes rule

Combining the definition of **conditional probability** with the **product** and sum rules yields **Bayes Theorem**:
$$
p(X =x|Y=y) = \frac{p(X=x, Y=y)}{p(Y=y)}=\frac{p(X=x)p(Y=y|X=x)}{\sum_{x'}p(X=x')p(Y=y|X=x')}
$$
simplified as:
$$
p(X|Y) = \frac{p(X)p(Y|X)}{p(Y)}
$$



- #### Example I: medical diagnosis

  A woman is having medical diagnosis for breast cancer. The test has a **sensitivity** of 80%, which means, if you have cancer, the test will successfully test positive with probability 0.8:
  $$
  p(x=1|y=1)=0.8
  $$
  where $x=1$ is the event that cancer is tested positive, and $y=1$ is the event you have breast cancer. This does not mean you are 80% likely to have cancer. 

  

  Ignoring the **prior** is called **base rate fallacy**. The prior probability of having breast cancer is low:
  $$
  p(y=1)=0.004
  $$
  We also need to take into account the probability of a **false positive**:
  $$
  p(x=1|y=0)=0.1
  $$
  Combining these three terms using Bayes rule:
  $$
  \begin{align}
  p(y=1|x=1) &= \frac {p(x=1|y=1)p(y=1)}{p(x=1|y=1)p(y=1)+p(x=1|y=0)p(y=0)} \\
  &= \frac{0.8 \times 0.004}{0.8 \times 0.004 + 0.1 \times 0.996} = 0.031
  \end{align}
  $$
  
  
- #### Example II. generative classifiers

  We can generalise the last example to classify feature vectors $\mathbf x$ of arbitrary type as follows:
  $$
  p(y=c|\mathbf x, \mathbf\theta) = \frac{p(y=c|\theta)p(\mathbf x|y=c,\theta)}{\sum_{c'} p(y=c'|\theta)p(\mathbf x|y=c', \theta)}
  $$
  where $p(\mathbf x |y=c)$ is the **class-conditional density**, $p(y=c)$ is the **class prior**.

  Another approach is to fit a class posterior $p(y=c|\mathbf x)$, known as a **discriminative classifier**.



### 2.2.4 Independence and conditional independence

- We say $X$ and $Y$ are **unconditionally/ marginally independent**, denoted as $X \perp Y$, if we can represent the joint as the **product** of the two marginals, i.e.:

$$
X \perp Y \iff p(X,Y) = p(X)p(Y)
$$



| <img src="2 Probability.assets/Screenshot from 2020-04-30 15-45-41.png" alt="Screenshot from 2020-04-30 15-45-41" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
| **Fig 2.2** Computing $p(x,y) = p(x)p(y)$, where $X\perp Y$  |

- However, most variables can influence most other variables. Usually this influence is mediated via other variables rather than being direct. We therefore say $X$ and $Y$ are **conditionally independent**(CI) given $Z$ if the conditional joint can be written as a product of conditional marginals:
  $$
  X \perp Y|Z \iff p(X,Y|Z) = p(X|Z)p(Y|Z)
  $$

  - Intuitively, this is because $Z$ *causes* both $X$ and $Y$, so if we know $Z$, we don't need to know about $Y$ for predicting $X$ or vice versa.

  - Another characterisation of CI is:
    $$
    p(x,y|z) = g(g,x)h(y,z)
    $$
     for all $x,y,z$ such that $p(z) > 0$.

  - CI assumptions allow us to build large probabilistic models from small pieces.



### 2.2.5 Continuous random variables

Suppose $X$ is some uncertain continuous quantity. The probability that $X$ lies in any interval $a \leq X\leq b$ can be computed as follows. Define the events $A = (X\leq a)$, $B = (X\leq b)$ and $W = (a\leq X \leq b)$. We have that $B = A \or W$, and since $A$ and $W$ are mutually exclusive, we have:
$$
p(B) = p(A) + p(W)
$$
and hence
$$
p(W) = p(B) - p(A)
$$


Define the **cumulative distribution function**(cdf) of $X$: $F(q) \triangleq p(X\leq q)$, we have:
$$
p(a<X\leq b) = F(b) - F(a)
$$


Now define the **probability density function**(pdf) $f(x) = \frac d {dx}F(x)$. Given a pdf, we can compute the probability of a continuous variable being in a finite interval as follows:
$$
P(a<X\leq b) = \int_a^b f(x)dx
$$
As the size of the interval gets smaller, we can write:
$$
P(x\leq X \leq x+dx) \approx p(x)dx
$$

- We require $p(x)\geq 0$, but it is possible for $p(x)>1$, so long as the density integrates to 1.

- #### Uniform distribution: $\text {Unif}\ (a,b)$

  $$
  \text{Unif}(x|a,b) = \frac 1 {b-a}\mathbb I(a\leq x\leq b)
  $$

  If we set $a=0$ and $b=\frac 1 2$, we have $p(x) = 2$ for any $x \in [0, \frac 1 2]$.

| <img src="2 Probability.assets/Screenshot from 2020-03-08 15-33-14.png" alt="Screenshot from 2020-03-08 15-33-14" style="zoom:50%;" /> | <img src="2 Probability.assets/Screenshot from 2020-03-08 15-33-23.png" alt="Screenshot from 2020-03-08 15-33-23" style="zoom:50%;" /> |
| :----------------------------------------------------------: | ------------------------------------------------------------ |
|        **Fig 2.3** (a) **cdf** for $\mathcal N(0,1)$         | (b) **pdf** for $\mathcal N(0,1)$                            |



### 2.2.6 Quantiles

Since the **cdf** function $F$ is a monotonically increasing function, it has an inverse $F^{-1}$, e.g. $F^{-1}(\alpha)$ is the value of $x_\alpha$ such that $P(X\leq x_\alpha) = \alpha$. This is called the $\alpha$ **quantile** of $F$.

[^F]: A monotonic function must have an inverse function with the same monotone.

- The value $F^{-1}(0.5)$ is the **median** of the distribution. 

- The value $F^{-1}(0.25)$ and $F^{-1}(0.75)$ are the lower and upper quantiles.

- Use $F^{-1}$ to compute **tail area probabilities**:

  If we set $\alpha =0.05$, the distribution is $\mathcal N(\mu, \sigma^2)$, then the central 95% interval is covered by:
  $$
  (\Phi^{-1}(0.025), \Phi^{-1}(0.975)) = (\mu - 1.96\sigma, \mu + 1.96\sigma)
  $$
  sometimes approximated as: $\mu \pm 2\sigma$.



### 2.2.7 Mean and variance

- #### Mean / Expected value: $\mu$

  - For discrete RVs: $\mathbb E[X] \triangleq \sum_{x\in \mathcal X} x\ p(x)$.
  - For continuous RVs: $\mathbb E[X] \triangleq \int_{\mathcal X} x\ p(x)dx$.
  - If the integral is not finite, the mean is not defined.

- #### Variance: $\sigma^2$

  The variance is a measure of the *spread* of a distribution. It is defined as follows:
  $$
  \begin {align}
  var[X] &\triangleq \mathbb E[(X-\mu)^2] = \int(x-\mu)^2p(x)dx \\
  &= \int x^2p(x)dx + \mu^2\int p(x)dx - 2\mu\int xp(x)dx = \mathbb E[X^2]- \mu^2
  \end {align}
  $$
  from which we derive the useful result:
  $$
  \mathbb E[X^2] = \mu^2 + \sigma^2
  $$

- #### Standard deviation:

  $$
  std[X] \triangleq \sqrt{var[X]}
  $$

  It is useful since it has the **same units** as $X$ itself.



## 2.3 Common discrete distributions

#### **Table 2.1** : Commonly used probability distributions

| Distribution    | Probability density function                                 | Mean              | Variance              |
| --------------- | ------------------------------------------------------------ | ----------------- | --------------------- |
| Binomial        | $Pr(X=k)={n \choose k}p^k(1-p)^{n-k}$                        | $np$              | $np(1-p)$             |
| Geometric       | $Pr(X=k)=(1-p)^{k-1}p$                                       | $\frac 1 p$       | $\frac {1-p} {p^2}$   |
| Normal          | $f(x|\mu, \sigma^2)=\frac 1 {\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu^2)}{2\sigma^2}}$ | $\mu$             | $\sigma^2$            |
| Uniform (cont.) | $f(x|a,b)= \cases {\frac 1 {b-1} & for a <= x <= b \\ 0 & for x < a or x >b}$ | $\frac {a+b} 2$   | $\frac {(b-a)^2}{12}$ |
| Exponential     | $f(x|\lambda)=\lambda e^{-\lambda x}$                        | $\frac 1 \lambda$ | $\frac 1 {\lambda^2}$ |



### 2.3.1 Binomial and Bernoulli distributions

1. Suppose we toss a coin $n$ times. Let $X \in \{0, ..., n\}$ be the number of heads. If the probability of head is $\theta$, then we say $X$ has a **binomial** distribution, written as $X \sim Bin(n, \theta)$. The *pmf* is given by

$$
Bin(k|n,\theta) \triangleq {n \choose k} \theta^k(1-\theta)^{n-k}
$$

​		where
$$
{n \choose k} \triangleq \frac {n!}{(n-k)!k!}
$$
​		**Binomial coefficient**:  the number of ways to choose $k$ items from $n$.

- Mean: $\theta$
- Variance: $n\theta(1-\theta)$



2. Now suppose we toss a coin only **once**. Let $X \in \{0,1 \}$ be a binary random variable, with probability of “heads” of $\theta$. We say that $X$ has a **Bernoulli** distribution, written as $X \sim Ber(\theta)$, where the *pmf* is defined as

$$
Ber(x|\theta)=\theta^{\mathbb I(x=1)}(1-\theta))^{\mathbb I(x=0)}
$$

​		In other words,
$$
Ber(x|\theta) = \cases {\theta & x= 1 \\
1-\theta & x=0}
$$
​		**Bernoulli** distribution is a special case of a **Binomial** distribution with $n=1$.



### 2.3.2 Multinomial and multinoulli distributions

In extension to the model of the outcomes of coin tosses, we can use the **multinomial** distribution to model the outcomes of tossing $K$-sided die.

1. Let $\mathbf x = (x_1, ..., x_K)$ be a random vector, where $x_j$ is the number of times side $j$ of the die occurs. Then $\mathbf x $ has the following *pmf*:

$$
Mu(\mathbf x|n, \theta) \triangleq {n \choose x1, ..., x_K} \prod \limits_{j=1}^K \theta^{x_j}_j
$$

​		where $\theta_j$ is the probability that side $j$ occurs, and the **multinomial coefficient**:
$$
{n \choose x_1, ...,x_K} \triangleq \frac {n!}{x_1!x_2!...x_K!}
$$


2. Suppose $n=1$, where only rolling the dice once, then $\mathbf x$ will be a vector of 0s and only a 1. We can think of $x$ as a scalar categorical random variable with $K$ states, and $\mathbf x$ is its **dummy encoding** or **one-hot encoding**, which is $\mathbf x = [\mathbb I(x=1), ..., \mathbb I(x=K)]$ of length $K$. In this case, the *pmf* becomes:

$$
Mu(\mathbf x |1, \theta) = \prod\limits_{j=1}^K \theta_j^{\mathbb I(x_j=1)}
$$

​		This is commonly known as a **categorical** or **discrete** distribution. 

​		The notation used in this case is **multinoulli distribution**:
$$
Cat(x|\theta)\triangleq Mu(x|1, \theta)
$$


#### 	**Table 2.2** Summary of the multinomial and related distributions

| Name        | n    | K    | x                                                   |
| ----------- | ---- | ---- | --------------------------------------------------- |
| Multinomial | -    | -    | $\mathbf x \in \{0,1,...,n\}^K,\sum_{k=1}^K x_k =n$ |
| Multinoulli | 1    | -    | $\mathbf x \in \{0, 1\}^K, \sum_{k=1}^K x_k=1$      |
| Binomial    | -    | 1    | $x \in \{0,1,...,n\}$                               |
| Bernoulli   | 1    | 1    | $x \in \{0, 1\}$                                    |

