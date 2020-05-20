# References card



Parentheses for functions, brackets for indexing positions.



## 1. Miscellaneous

```R
q(): quit
<-: assign
INSTALL package1: install package1 
m1[,2]: column 2 of matrix m1
m1[,2:5] or m1[,c(2,3,4,5)]: columns 2–5 
m1$a1: variable a1 in data frame m1
NA: missing data
is.na: true if data missing
library(mva): load (e.g.) the mva package
```



## 2. Help

```R
help(command1): get help with command1
help.start(): start browser help 
help(package=mva): help with (e.g.) package mva apropos("topic1"): commands relevant to topic1 example(command1): examples of command1
```



## 3. Input and output

```R
source("file1"): run the commands in file1
read.table("file1"): read in data from file1 
data.entry(): spreadsheet
scan(x1): read a vector x1
download.file(url1): from internet 
url.show(url1), read.table.url(url1): remote input
sink("file1"): output to file1, until sink() 
write(object, "file1"): writes an object to file1 
write.table(dataframe1,"file1"): writes a table
```



## 4. Managing variables and objects
```R
attach(x1): put variables in x1 in search path 
detach(x1): remove from search path
ls(): lists all the active objects.
rm(object1): removes object1
dim(matrix1): dimensions of matrix1 
dimnames(x1): names of dimensions of x1 
length(vector1): length of vector1
1:3: the vector 1,2,3
c(1,2,3): creates the same vector 
rep(x1,n1): repeats the vector x1 n1 times 
cbind(a1,b1,c1), rbind(a1,b1,c1): binds columns or rows into a matrix 
merge(df1,df2): merge data frames 
matrix(vector1,r1,c1): make vector1 into a matrix with r1 rows and c1 columns 
data.frame(v1,v2): make a data frame from vectors v1 and v2
as.factor(), as.matrix(), as.vector(): conversion
is.factor(), is.matrix(), is.vector(): what it is
t(): switch rows and columns
which(x1==a1): returns indices of x1 where x1==a1
```



## 5. Control flow
```R
for (i1 in vector1): repeat what follows 
if (condition1) ...else ...: conditional
```



## 6. Arithmetic

```R
%*%: matrix multiplication
%/%, ^: integer division, power
%%, sqrt(): modulus, square root
```



## 7. Statistics
```R
max(), min(), mean(), median(), sum(), var(): as named
summary(data.frame): prints statistics 
rank(), sort(): rank and sort
ave(x1,y1): averages of x1 grouped by factor y1 
by(): apply function to data frame by factor 
apply(x1,n1,function1): apply function1 
tapply(x1,list1,function1): apply function to x1 by list1
table(): make a table 
tabulate(): tabulate a vector
```



## 8. basic statistical analysis

```R
aov(), lm(), glm(): linear and nonlinear models
anova(): anova
t.test(): t test
prop.test(), binom.test(): sign test 
chisq.test(x1): chi-square test on matrix x1 
fisher.test(): Fisher exact test
cor(a): show correlations
cor.test(a,b): test correlation 
friedman.test(): Friedman test
```



## 9. Some statistics in mva package

```R
prcomp(): principal components 
kmeans(): kmeans cluster analysis 
factanal(): factor analysis 
cancor(): canonical correlation
```



## 10. Graphics
```R
plot(), barplot(), boxplot(), stem(), hist(): basic plots
matplot(): matrix plot
pairs(matrix): scatterplots
coplot(): conditional plot
stripplot(): strip plot
qqplot(): quantile-quantile plot
qqnorm(), qqline(): fit normal distribution
```

