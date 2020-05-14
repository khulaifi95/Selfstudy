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

   - We define the probability of the joint event $A$ and $B$ as follows:

   $$
   p(A, B) = p(A \and B) = p(A|B)p(B)
   $$

   ​		AKA **product rule**. 

   - Given a **joint distribution** on two events $p(A,B)$, we define **marginal distribution** as

   $$
   p(A) = \sum\limits_b p(A,B) = \sum\limits_b p(A|B = b)p(B=b)
   $$

   ​		AKA **sum rule**.

   - The product rule can be applied multiple times to yield the **chain rule** of probability:

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

  - $X\perp Y|Z $ iff there exist function $g$ and $h$ such that:
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

​		is the number of ways to divide a set of size $n=\sum_{k=1}^Kx_k$ into subsets with sizes $x_1$ to $x_K$.

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



### 2.3.3 Poisson distribution

We say that $X \in \{0,1,2,...\}$ has a **Poisson** distribution with parameter $\lambda >0$, written as $X \sim Poi(\lambda)$. The *pmf* is
$$
Poi(x| \lambda) = e^{-\lambda}\frac {\lambda^x}{x!}
$$
The first term is the **normalisation** constant, required to ensure the distribution sums to 1. 

The Poisson distribution is often used as a model for **counts of rare events** like radioactive decay and traffic accident.



### 2.3.4 Empirical measure

Given a set of data $D = \{x_1, ..., x_N\}$, we define the empirical distribution/ measure as follows:
$$
P_{emp}(A)\triangleq\frac 1 N \sum\limits_{i=1}^N\delta_{x_i}(A)
$$
where $\delta_x(A)$ is the **Dirac measure**, defined by
$$
\delta_x(A) = \cases {0   \ \ \ \ \ \ \ \ \ \ \ \ x \notin A \\ 1   \ \ \ \ \ \ \ \ \ \ \ \ x \in A}
$$
In general, we can associate *weights* with each sample:
$$
p(x) = \sum\limits_{i=1}^Nw_i\delta_{x_i}(x)
$$
where we require $0\leq w_i \leq 1$ and $\sum_{i=1}^N w_i=1$.

This can be considered as a histogram, with *spikes* at the data points $x_i$, where $w_i$ determines the height of spike $i$. Any point not in the data set are assigned 0 by the distribution.



## 2.4 Common continuous distributions

This section presents some commonly used univariate (one-dimensional) continuous probability distributiions.

### 2.4.1 Gaussian (normal) distribution

The most widely used distribution in statistics and machine learning is the Gaussian or normal distribution. The *pdf* is given by
$$
\mathcal N(x|\mu, \sigma^2) \triangleq \frac 1 {\sqrt{2\pi\sigma^2}}e^{-\frac 1 {2\sigma^2}(x-\mu)^2}
$$
$\mu = \mathbb E[X]$ is the mean, and $\sigma^2=var [X]$ is the variance. $\sqrt{2\pi\sigma^2}$ is the normalisation constant needed to ensure the density integrates to 1.



1. **Standard normal distribution** 

If $X \sim \mathcal N(0,1)$, we say $X$ follows a **standard normal** distribution. This is also called the **bell curve**. 

2. **Precision**

The precision of a Gaussian is defined by the **inverse variance**: $\lambda = 1/\sigma^2$. A high precision means a narrow distribution centred on $\mu$.

3. **Cumulative distribution function**

The *cdf* of the Gaussian is defined as
$$
\Phi(x;\mu,\sigma^2)\triangleq\int_{-\infty}^x \mathcal N(z|\mu, \sigma^2)dz
$$
where the integral has no closed form expression. In particular, we can compute it in terms of the **error function** *erf*:
$$
\Phi(x;\mu, \sigma) = \frac 1 2[1+\text {erf}(z/\sqrt 2)]
$$
where $z = (x-\mu)/\sigma$ and:
$$
\text {erf}(x)\triangleq \frac 2 {\sqrt\pi} \int_0^x e^{-t^2}dt
$$


Several reasons make the Gaussian distribution the most widely used in statistics:

- The two parameters are easy to interpret and capture some of most basic properties of a distribution - **mean** and **variance**.
- The **central limit theorem** says that sums of indepent random variables have an approximately Gaussian distribution, making it a good choice for modelling residual **errors** or **noise**.
- It makes the least number of assumptions, e.g. *has maximum entropy*, subject to the constraint of having a specified mean and variance.
- A simple mathematical form makes it easy to implement but also highly effective.



### 2.4.2 Degenerate pdf

In the limit that $\sigma^2 \rightarrow 0$, the Gaussian becomes an *infinitely* tall and thin 'spike', centred at $\mu$:
$$
\lim_{\sigma^2\rightarrow0}\mathcal N(x|\mu, \sigma^2)=\delta(x-\mu)
$$
where $\delta$ is the **Dirac delta function** defined as:
$$
\delta(x) = \cases {\infty & if  x = 0 \\  0 & if  x !=0}
$$
such that:
$$
 \int_{-\infty}^\infty\delta(x)dx=1
$$
As a distribution, the Dirac delta function is a **linear functional** that maps every function to its value at **zero**.



1. **Sifting property**

The delta functions are very useful when selecting out a single term from a sum or integral since the integrand is only non-zero when $x-\mu=0$:
$$
\int_{-\infty}^{\infty}f(x)\delta(x-\mu)dx=f(\mu)
$$

2. **Student t-distribution**

The Gaussian distribution is too sensitive to outliers, since the log-probability only decays quadratically with distance from the centre.

A more robust distribution is the Student t-distritbution with *pdf*:
$$
\mathcal T(x|\mu, \sigma^2, v) \propto [1+\frac 1 v (\frac{x-\mu}{\sigma})^2]^{-(\frac{v+1}{2})}
$$
where $\mu$ is the mean, $\sigma^2 >0$ is the **scale** parameter, and $v >0$ is the **degrees of freedom**. 

- mean=$\mu$

- mode=$\mu$

- var= $v\sigma^2/{(v-2)}$

  

- The variance is only defined if $v>2$, the mean is only defined when $v >1$.

- When dealing with outliers, the Student distribution is robuster than the Gaussian for small degree of freedom.
- If $v=1$, the distribution is known as the **Cauchy/ Lorentz** distribution.
- Commonly, to ensure finite variance,  we require $v>2$. It is common to use $v=$ **4**. For $v=5$, it approaches a Gaussian distribution rapidly.

| <img src="2 Probability.assets/Screenshot 2020-05-05 at 20.00.32-8705323.png" alt="Screenshot 2020-05-05 at 20.00.32" style="zoom:50%;" /> | <img src="2 Probability.assets/Screenshot 2020-05-05 at 20.00.40-8705323.png" alt="Screenshot 2020-05-05 at 20.00.40" style="zoom:50%;" /> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                **Fig 2.4**   (a) No outliers                 |                      (b) With outliers                       |



### 2.4.3 Laplace distribution

Another distribution with **heavy tails** is the Laplace distribution, a.k.a. the **double sided exponential** distribution. This has the following *pdf*:
$$
Lap(x|\mu, b) \triangleq \frac 1 {2b} \exp(-\frac{|x-\mu|}{b})
$$
where $\mu$ is a location parameter and $b>0$ is a scale parameter. 

- mean = $\mu$
- mode = $\mu$
- var = $2b^2$

It is robust to outliers, but also puts more probability density at 0 than the Gaussian. It is a useful way to **encourage sparsity** in a model.



### 2.4.4 Gamma distribution

The gamma distribution is a flexible distribution for **positive real valued** rv's, $x>0$. It is defined in terms of two parameters: the **shape** $a>0$ and the **rate** $b>0$:
$$
Ga(T|\text{shape}=a, \text{rate}=b) \triangleq \frac {b^a}{\Gamma(a)}T^{a-1}e^{-Tb}
$$
where $\Gamma(a)$ is the gamma function:
$$
\Gamma(x) \triangleq \int_0^\infty u^{x-1}e^{-u}du
$$
The Gamma function is an extension of the **factorial function** to the complex numbers. For all natural numbers, it says $\Gamma(n+1)=n!$.

- mean = $a/b$
- mode = $(a-1)/b$
- var = $a/b^2$

Several well-known distributions are special cases of the Gamma:

1. **Exponential distribution**

Defined by $\text{Expon}(x|\lambda)\triangleq Ga(x|1, \lambda)$, where $\lambda$ is the rate parameter. It describes the times between events in a **Poisson process**, i.e. a process in which events occur continuously and independently at a constant average rate $\lambda$.

2. **Erlang distribution**

It is the same the Gamma where $a$ is an integer, commonly fixed to 2. The resulting one-parameter Erlang distribution is $\text{Erlang}(x|\lambda) = Ga(x|2, \lambda)$.

3. **Chi-squared distribution**

This distribution is defined by 
$$
\mathcal X^2(x|v) \triangleq Ga(x|\frac v 2, \frac1 2)
$$
Which is the distribution of the **sum of squared** Gaussian random variables. More precisely, if $Z_i \sim \mathcal N(0,1), \text{and} \ S = \sum_{i=1}^vZ_i^2$, then $S \sim \mathcal X^2_v$.

- Additionally, if $X \sim Ga(a,b)$, then one can show that $\frac 1X \sim IG(a,b)$, where $IG$ is the **inverse gamma** distribution defined by:

$$
IG(x|shape = a, scale=b) \triangleq \frac {b^a}{\Gamma(a)}x^{-(a+1)}e^{-b/x}
$$



| <img src="2 Probability.assets/Screenshot 2020-05-06 at 01.59.10.png" style="zoom:50%;" /> | <img src="2 Probability.assets/Screenshot 2020-05-06 at 01.59.20.png" style="zoom:50%;" /> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|                **Fig 2.5**   (a) $Ga(a, b=1)$                |              (b) fitting Gamma to empirical pdf              |



### 2.4.5 Beta distribution

The beta distribution has support over the interval [0,1] and is defined as:
$$
Beta(x|a, b) = \frac 1 {B(a,b)}x^{a-1}(1-x)^{b-1}
$$
where $B(p,q)$ is the beta function:
$$
B(a,b) \triangleq \frac {\Gamma (a)\Gamma (b)}{\Gamma(a+b)}
$$
where $\Gamma(a)$ is the Gamma function. We require $a,b>0$ to ensure the distribution is *integrable*. 

- a=b=1: uniform distribution
- a<1, b<1: bimodal distribution
- a>1, b>1: unimodal distribution

The distribution has following properties:

- mean = $a/(a+b)$
- mode = $(a-1)/(a+b-2)$
- var = $ab/(a+b)^2(a+b+1)$

| <img src="2 Probability.assets/Screenshot 2020-05-06 at 03.42.39.png" alt="Screenshot 2020-05-06 at 03.42.39" style="zoom:50%;" /> |
| :----------------------------------------------------------: |
|                **Fig 2.6** Beta distributions                |



### 2.4.6 Pareto distribution

The Pareto distribution is used to model the distribution of quantities that exhibit **long tails** or **heavy tails**. It is often observed that the most frequent word used in English are twice as often as the second word. This power law is known as **Zipf's law**. The Pareto *pdf* is defined as follow:
$$
Pareto(x|k,m) = km^kx^{-(k+1)}\mathbb I(x\geq m)
$$
This density asserts that x must be greater than some constant m, but not too much greater, as $k \rightarrow \infty$, the distribution approaches $\delta(x-m)$. 

If the distribution is plotted on a log scale, it forms a straight line, of the form $\log p(x) = a\log x+c$.

- mean = km/(k-1)
- mode = m
- var = $m^2k/(k-1)^2(k-2)$ if $k >2$

| <img src="2 Probability.assets/Screenshot 2020-05-06 at 03.43.42.png" alt="Screenshot 2020-05-06 at 03.43.42" style="zoom:50%;" /> | <img src="2 Probability.assets/Screenshot 2020-05-06 at 03.45.56.png" style="zoom:50%;" /> |
| ------------------------------------------------------------ | :----------------------------------------------------------: |
| **Fig 2.7** (a) $Pareto(x|m,k) $for m =1                     |                  (b) pdf on a log-log scale                  |



## 2.5 Joint probability distributions

The problem of building joint probability distributions on multiple related random variables will be a central topic in this book.

A **joint probability distribution** has the form $p(x_1,...,x_D)$ for a set of $D>1$ variables, and models the *stochastic* relationships between the variables.

If all the variables are **discrete**, we can represent the joint distribution as a big multi-dimensional array, with one variable per dimension. However, the number of parameters needed to define such a model is $O(K^D)$, where K is the number of states for each variable.

We can use fewer parameters to define high dimensional joint distributions by making *conditional indepenence* assumptions. In the case of continuous distributions, an alternative approach is to restrict the form of the pdf to certain functional forms, some of which we will examine below.



### 2.5.1 Covariance and correlation

The **covariance** between two random variables $X, \ Y$ measures the degree to which $X$ and $Y$ are (*linearly*) related. It is defined as
$$
cov[X,Y] \triangleq \mathbb E[(x-\mathbb E[X])(y-\mathbb E[Y])] = \mathbb E[XY] - \mathbb E[Y]\mathbb E[Y]
$$

1. If $\mathbf x$ is a $d$-dimensional random vector, then its **covariance matrix** is defined as the following *symmetric*, positive definite matrix:

$$
cov[\mathbf x] \triangleq \mathbb E[(\mathbf x- \mathbb E[\mathbf x])(\mathbf x - \mathbb E[\mathbf x])^T]
\\ \ 
\\ = \pmatrix {var[X_1], \ cov[X_1, X_2],\ ...,\ cov[X_1, X_d]
\\ \
\\ ... \ \ \ \ \ \ \ \ \ \ \ \ \ \ ... \ \ \ \ \ \ \ \ \ \ \ \ \ \ ... \ \ \ \ \ \ \ \ \ \ \ \ \ \ ...
\\ \
\\ \ cov[X_d, X_1], \ cov[X_d, X_2],\ ..., \ var[X_d]}
$$

2. It is more convenient to work with a normalised measure, with a finite upper bound. The Pearson **correlation coefficient** between $X$ and $Y$ is defined as

$$
corr[X, Y] \triangleq \frac {cov[X,Y]}{\sqrt{var[X]var[Y]}}
$$

​		A **correlation matrix** has the form
$$
\mathbf R = \pmatrix {corr[X_1, X_1], \ corr[X_1, X_2], \ ..., \ corr[X_1, X_d]
\\ \
\\ ... \ \ \ \ \ \ \ \ \ \ \ \ \ \ ... \ \ \ \ \ \ \ \ \ \ \ \ \ \ ... \ \ \ \ \ \ \ \ \ \ \ \ \ \ ...
\\ \
\\ corr[X_d, X_1], \ corr[X_d, X_2], \ ..., \ corr[X_d, X_d]
}
$$
**Properties**:

- $-1\leq corr[X,Y] \leq 1$, hence each entry in a correlation matrix on the diagonal is 1, while the others are between -1 and 1.
- $corr[X,Y]=1$ *iff* $Y= aX+b$ for some parameters $a,b$. (linear)
- The correlation coefficient can be better considered as a *degree of linearity*.

- Independent pairs of variables have $corr[X,Y]=0$ , but **uncorrelated** does not imply **independent**.
  - A more general measure: mutual information.



### 2.5.2 The multivariate Gaussian

The **multivariate Gaussian/ normal** is the most widely used joint probability density function for continuous variables. The *pdf* of a **MVN** in $D$ dimensions is defined by the following:
$$
\mathcal N(\mathbf x|\mu, \mathbf\Sigma) \triangleq \frac1{(2\pi)^{D/2}|\mathbf\Sigma|^{1/2}}\exp[-\frac12(x-\mu)^T\mathbf\Sigma^{-1}(x-\mu)]
$$
where $\mathbf\mu=\mathbb E[x] \in \mathbb R^D$ is the mean vector, $\mathbf\Sigma = cov[x]$ is the $D \times D$ covariance matrix. The normalisation constant ensures that the *pdf* integrates to 1. A **precision matrix** is the inverse covariance matrix: $\mathbf \Lambda=\mathbf\Sigma^{-1}$.

- A full covariance matrix has $D(D+1)/2$ parameters.

- A diagonal covariance matrix has $D$ parameters on the diagonal.
- An **isotropic** covariance $\mathbf \Sigma=\sigma^2\mathbf I_D$ has one free parameter.



|                  (a) Full MVN - elliptical                   |               (b) Diagonal MVN - axis aligned                |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| <img src="/Users/kevinxu95/Selfstudy/Machine Learning/2 Probability.assets/Screenshot 2020-05-14 at 07.45.58.png" style="zoom:50%;" /> | <img src="/Users/kevinxu95/Selfstudy/Machine Learning/2 Probability.assets/Screenshot 2020-05-14 at 07.46.05.png" style="zoom:50%;" /> |
|                 (c) Isotropic MVN - circular                 |                    (d) 3d surface of (c)                     |
| <img src="/Users/kevinxu95/Selfstudy/Machine Learning/2 Probability.assets/Screenshot 2020-05-14 at 07.46.19-9438851.png" style="zoom:50%;" /> | <img src="/Users/kevinxu95/Selfstudy/Machine Learning/2 Probability.assets/Screenshot 2020-05-14 at 07.46.27.png" style="zoom:50%;" /> |
|                   **Fig 2.8** 2d Gaussians                   |                                                              |



### 2.5.3 Multivariate Student t distribution

A more robust alternative to the MVN is the **multivariate Student t** distribution, whose *pdf* is
$$
\mathcal T(\mathbf x|\mu, \mathbf \Sigma, v) = \frac{\Gamma(v/2+D/2)}{\Gamma(v/2)}|\pi\mathbf V|^{-1/2}\times[1+(\mathbf x - \mathbf\mu)^T\mathbf V^{-1}(\mathbf x-\mu)]^{-(\frac{v+D}{2})}
$$
where $\mathbf V=v\mathbf \Sigma$. It returns fatter tails than the Gaussian. 

The smaller $v$ is, the fatter the tails. As $v \rightarrow \infty$, the distribution tends towards a Gaussian.

- mean = $\mu$
- mode = $\mu$
- Cov = $\frac {v}{v-2}\mathbf\Sigma$



### 2.5.4 Dirichlet distribution

