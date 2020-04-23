# 1. Input and Evaluation

At the R prompt we type expressions. The <- symbol is the assignment operator.

```R
> x <- 1
> print(x)
[1] 1
> x
[1] 1
> msg <- "hello"
```

The [1] indicates that $x$ is a vector and 1 is the first element.

```R
> x <- ## incomplete
```

The **#** character indicates a comment.

```R
> x <- 1:20
```

The **:** operator is used to create integer sequences.



# 2. Data Types

### 2.1 Objects

R has five atomic classes of objects:

- character
- numeric - real numbers
- integer
- complex
- logical - True/ False

```Vector``` is the most basic object:

- A vector can only contain objects of the same class.
- ```list```is represented as a vector but can contain objects with different classes.



### 2.2 Numbers

- Treated as numeric objects i.e. double precision real numbers.
- Use $L$ suffix for explicit integer.
- ```Inf``` for infinity.
- ```NaN``` for undefined value.



### 2.3 Attributes

R objects can have attributes:

- names, dimnames
- dimensions
- class
- length
- user-defined attributes / metadata

Attributes of an object can be accessed using ```attributes()``` function.



### 2.3 Vectors

##### 2.3.1 Creating vectors

The ```c()``` function can be used to **concatenate** vectors of objects:

``````R
> x <- c(0.5, 0.6)			## numeric
> x <- c(T, F)				## logical
> x <- c("a", "b", "c")		## character
> x <- 9:29					## sequence of integer
> x <- c(1+0i, 2+4i)			## complex
``````

Using the ```vector()``` function:

``` R
> x <- vector(“numeric”, length=10)		## default to zero
> x
 [1] 0 0 0 0 0 0 0 0 0 0
```



##### 2.3.2 Mixing objects

When different objects are mixed in a vector, *coercion* occurs so that every element in the vector is of the same class.

