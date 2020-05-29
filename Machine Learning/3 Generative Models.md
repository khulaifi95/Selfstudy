# 3 Generative Models for Discrete Data



## 3.1 Introduction

We discussed how to classify a feature vector $\mathbf x$ by applying Bayes' rule to a generative classifier of the form:
$$
p(y=c|\mathbf x,\boldsymbol \theta) \propto p(\mathbf x|y=c, \boldsymbol \theta)p(y=c|\boldsymbol \theta)
$$

- The key to using such models is specifying a suitable form for the **class-conditional density**

$$
p(\mathbf x|y=c, \boldsymbol \theta)
$$

​		which defines what kind of data expected in each class.



## 3.2 Bayesian concept learning

