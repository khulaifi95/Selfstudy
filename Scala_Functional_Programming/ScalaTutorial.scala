calaScala
// Install Scala on Mac : Install Java VM, Install Homebrew,
// In terminal type: brew install scala

// Scala is the perfect choice if you want to explore functional
// programming without disregarding OOP
// Scala runs on the JVM which provides a ton of libraries

// File ends with the scala extension

// How to import library functions
import scala.io.StdIn.{readLine,readInt}
import scala.math._
import scala.collection.mutable.ArrayBuffer
import java.io.PrintWriter
import scala.io.Source

/*
You can execute commands directly in the terminal
REPL : Read Evaluate Print Loop
Type scala in terminal to start and :q to quit

// Creates a variable of the correct type
10 + 3 * 5 / 2

// You only use semicolons in Scala if you have multiple statements per line

// You can use that variable in the code that follows
"Your answer " + res0

// Define your own variable
var myName = "Derek"

// Define your own constant variable
val myAge = 40

// You can define the type
val lastName: String = "Banas"

// ---------- DATA TYPES ----------

// All datatypes in Scala are objects and they include
// (Get the max value with MaxValue)
// Byte : -128 to 127
// Boolean : true or false
// Char : unsigned max value 65535
// Short : -32768 to 32767
// Int : -2147483648 to 2147483647
// Long : -9223372036854775808 to 9223372036854775807
// Float : -3.4028235E38 to 3.4028235E38
// Double : -1.7976931348623157E308 to 1.7976931348623157E308

// A Double will only hold precision up to 15 digits
val num13 = 1.999999999999999

// Create a BigInt
val lgPrime = BigInt("622288097498926496141095869268883999563096063592498055290461")
lgPrime + 1

 Create a BigDecimal
val pi50 = BigDecimal("3.14159265358979323846264338327950288419716939937510")
0.00000000000000000000000000000000000000000000000001 + pi50

var randInt = 100000

// See functions available by typing randInt. (Click Tab)
// randInt.asInstanceOf[Double] casts number to a double
// randInt.isInstanceOf[Int] checks if is of type Int

// ---------- MATH ----------
"5 + 4 = " + (5 + 4)
"5 - 4 = " + (5 - 4)
"5 * 4 = " + (5 * 4)
"5 / 4 = " + (5 / 4)
"5 % 4 = " + (5 % 4)

// Shorthand notation (No randInt++, or randInt--)
randInt += 1
"randInt += 1" + randInt

randInt -= 1
"randInt -= 1" + randInt

randInt *= 1
"randInt *= 1" + randInt

randInt /= 1
"randInt /= 1" + randInt

// Import the math library in the terminal import scala.math._

abs(-8)
cbrt(64) // Cube root a^3 = n (Find a)
ceil(5.45)
round(5.45)
floor(5.45)
exp(1) // Euler's number raised to the power
pow(2, 2) // 2^2
sqrt(pow(2,2) + pow(2,2))
hypot(2, 2) // sqrt(X^2 + y^2)
log10(1000) // = 3 (10 × 10 × 10 = 10^3)
log(2.7182818284590455) // Natural logarithm to the base e
min(5, 10)
max(5, 10)
(random * (11 - 1) + 1).toInt // Random number between 1 and 10
toRadians(90)
toDegrees(1.5707963267948966)

// acos, asin, atan, atan2, cos, cosh, sin, sinh, tan, tanh

// ---------- CONDITIONALS ----------
// if statements are like Java except they return a value like the
// ternary operator

// Conditional Operators : ==, !=, >, <, >=, <=
// Logical Operators : &&, ||, !

var age = 18

val canVote = if (age >= 18) "yes" else "no"

// You have to use { } in the REPL, but not otherwise
if ((age >= 5) && (age <= 6)) {
  println("Go to Kindergarten")
} else if ((age > 6) && (age <= 7)) {
  println("Go to Grade 1")
} else {
  println("Go to Grade " + (age - 5))
}

true || false
!(true)

*/

object ScalaTut {
  def main(args: Array[String]) {

// ---------- LOOPING ----------
// To compile and run in the terminal
// 1. scalac ScalaTut.scala
// 2. scala ScalaTut

    var i = 0

    while (i <= 10) {
      println(i)
      i += 1
    }

    do {
      println(i)
      i += 1
    } while(i <= 20)

    for (i <- 1 to 10){
      println(i)
    }

    // until is often used to loop through strings or arrays
    val randLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for (i <- 0 until randLetters.length){

      // Get the letter in the index of the String
      println(randLetters(i))
    }

    // Used to iterate through a list
    val aList = List(1,2,3,4,5)
    for(i <- aList){
      println("List Item " + i)
    }

    // Store even numbers in a list
    var evenList = for { i <- 1 to 20
      // You can put as many conditons here separated with semicolons
      // as you need
      if (i % 2) == 0
    } yield i

    println("Even List")
    for(i <- evenList)
      println(i)

    // This loop assigns a value to the 1st variable and it retains
    // that value until the 2nd finishes its cycle and then it iterates
    for (i <- 1 to 5; j <- 6 to 10){
      println("i: " + i)
      println("j: " + j)
    }

    // There is no break or continue in Scala
    def printPrimes() {

      val primeList = List(1,2,3,5,7,11)
      for (i <- primeList){

        // Works like break if you return from a function
        if(i == 11){
          return
        }

        // Works like continue
        if (i != 1){
          println(i)
        }

      }

    }

    printPrimes


// ---------- INPUT / OUTPUT ----------

var numberGuess = 0

do{
  print("Guess a number : ")

  // You can also use readInt, readDouble, readByte, readShort, readLong,
  //
  numberGuess = readLine.toInt

  } while(numberGuess != 15)

  printf("You guessed the secret number %d\n", 15)

  // You can use string interpolation
  val name = "Derek"
  val age = 39
  val weight = 175.5
  println(s"Hello $name")

  println(f"I am ${age + 1} and weigh $weight%.2f")

  // printf Style Format Specifiers
  // %c : Characters
  // %d : Integers
  // %f : Floating Point Numbers
  // %s : Strings
  printf("'%5d'\n",5) // Right justify

  printf("'%-5d Hi'\n",5) // Left justify

  printf("'%05d'\n",5) // Zero Fill

  printf("'%.5f'\n",3.14) // 5 decimal minimum & maximum

  printf("'%-5s'\n", "Hi") // Left Justify String

  // Special Characters : \n, \b, \\, \a

// ---------- STRINGS ----------
var randSent = "I saw a dragon fly by"

// Get the 3rd index value
println("3rd Index : " + randSent(3))

// Get String length
println("String length " + randSent.length())

// Concatenate strings
println(randSent.concat(" and explode"))

// Compare strings for equality
println("Are strings equal " + "I saw a dragon".equals(randSent))

// Get index of a match
println("dragon starts at index ", randSent.indexOf("dragon"))

// Convert a string into an array
val randSentArray = randSent.toArray

for (v <- randSentArray)
  println(v)

// ---------- FUNCTIONS ----------
// def funcName (param1:dataType, param2:dataType) : returnType = {
//    function body
//    return valueToReturn
// }

// You can give parameters default values
def getSum( num1:Int = 1, num2:Int = 1) : Int = {
  return num1 + num2
}

println("5 + 4 = " + getSum(5,4))

// you can use named arguments
println("5 + 4 = " + getSum(num2=5, num1=4))

// A function that returns nothing (Procedure)
def sayHi() : Unit = {
  println("Hi how are you doing")
}

sayHi

// Receive variable number of arguments
def getSum2(args: Int*) : Int = {
  var sum : Int = 0
  for(num <- args){
    sum += num
  }
  sum
}

println("getSum2: " + getSum2(1,2,3,4,5))

// Recursion example calculating factorials
def factorial(num : BigInt) : BigInt = {
  if (num <= 1)
    1
  else
    num * factorial(num - 1)
}

// 1st: num = 4 * factorial(3) = 4 * 6 = 24
// 2nd: num = 3 * factorial(2) = 3 * 2 = 6
// 3rd: num = 2 * factorial(1) = 2 * 1 = 2

println("Factorial of 4 = " + factorial(4))

// ---------- ARRAYS ----------
// You'll use arrays when the size is fixed, or an ArrayBuffer for a
// variable size

// Create an array of Ints with a max size of 20
val favNums = new Array[Int](20)

// Create and initialize array in 1 line
val friends = Array("Bob", "Tom")

// Change the value in an array
friends(0) = "Sue"

println("Best Friend " + friends(0))

// Create an ArrayBuffer
val friends2 = ArrayBuffer[String]()

// Add an item to the 1st index
friends2.insert(0, "Phil")

// Add item to the next available slot
friends2 += "Mark"

// Add multiple values to the next available slot
friends2 ++= Array("Susy", "Paul")

// Add items starting at 2nd slot
friends2.insert(1, "Mike", "Sally", "Sam", "Mary", "Sue")

// Remove the 2nd element
friends2.remove(1)

// Remove 2 elements starting at the 2nd index
friends2.remove(1, 2)

// Cycle through and print ArrayList or Array
var friend : String = " "
for(friend <- friends2)
      println(friend)

// Add values to an array with a loop
for (j <- 0 to (favNums.length - 1)){
  favNums(j) = j
  println(favNums(j))
}

// Use yield to multiply all values times 2 and store in a new array
val favNumsTimes2 = for(num <- favNums) yield 2 * num

// Another way to print out values in array
favNumsTimes2.foreach(println)

// You can also store values that match a condition
var favNumsDiv4 = for(num <- favNums if num % 4 == 0) yield num

favNumsDiv4.foreach(println)

// Create a multidimensional array with Array.ofDim
var multTable = Array.ofDim[Int](10,10)

for(i <- 0 to 9){
  for(j <- 0 to 9){
    multTable(i)(j) = i * j
  }
}

for(i <- 0 to 9){
  for(j <- 0 to 9){
    printf("%d : %d = %d\n", i, j, multTable(i)(j))
  }
}

println("Sum : " + favNums.sum)

println("Min : " + favNums.min)

println("Max : " + favNums.max)

// Sort in desending order (Use < for assending)
val sortedNums = favNums.sortWith(_ > _)

// Return an indexed sequence and convert it into a string with commas
println(sortedNums.deep.mkString(", "))

// ---------- MAPS ----------
// Maps are collections of key value pairs

// Create a Map that can't be changed (Immutable)
val employees = Map("Manager" -> "Bob Smith", "Secretary" -> "Sue Brown")

// Get value using the key after checking that it exists
if(employees.contains("Manager"))
  printf("Manager : %s\n", employees("Manager"))

// Create a Mutable map
val customers = collection.mutable.Map(100 -> "Paul Smith",
  101 -> "Sally Smith")

printf("Cust 1 : %s\n", customers(100))

// Change a value using the key
customers(100) = "Tom Marks"

// Add an item
customers(102) = "Megan Swift"

// Output a Map
for((k,v) <- customers)
  printf("%d : %s\n", k, v)

// ---------- TUPLES ----------
// Tuples can hold values of many types, but they are immutable

var tupleMarge = (103, "Marge Simpson", 10.25)

printf("%s owes us $%.2f\n", tupleMarge._2, tupleMarge._3)

// Iterate through a tuple
tupleMarge.productIterator.foreach{ i => println(i)}

// Convert Tuple to String
println(tupleMarge.toString())

// ---------- CLASSES ----------
val rover = new Animal
rover.setName("Rover")
rover.setSound("Woof")
printf("%s says %s\n", rover.getName, rover.getSound)

val whiskers = new Animal("Whiskers", "Meow")
println(s"${whiskers.getName} with id ${whiskers.id} says ${whiskers.getSound}")

println(whiskers.toString)

val spike = new Dog("Spike", "Woof", "Grrrr")

spike.setName("Spike")
println(spike.toString)

val fang = new Wolf("Fang")
fang.moveSpeed = 36.0
println(fang.move)

// ---------- TRAITS ----------
val superman = new Superhero("Superman")
println(superman.fly)
println(superman.hitByBullet)
println(superman.ricochet(2500))

// ---------- HIGHER ORDER FUNCTIONS ----------
// Functions can be passed like any other variable
// You need the _ after the function to state you meant the function
val log10Func = log10 _

println(log10Func(1000))

// You can apply a function to all items of a list with map
List(1000.0,10000.0).map(log10Func).foreach(println)

// You can use an anonymous function with map as well
// Receives an Int x and multiplies every x by 50
List(1,2,3,4,5).map((x : Int) => x * 50).foreach(println)

// Filter will pass only those values that meet a condition
List(1,2,3,4,5,6).filter(_ % 2 == 0).foreach(println)

// Pass different functions to a function
def times3(num : Int) = num * 3
def times4(num : Int) = num * 4

// Define the function parameter type and return type
def multIt(func : (Int) => Double, num : Int ) = {
  func(num)
}

printf("3 * 100 = %.1f)\n", multIt(times3, 100))

// A closure is a function that depends on a variable declared outside
// of the function
val divisorVal = 5
val divisor5 = (num : Double) => num / divisorVal
println("5 / 5 = " + divisor5(5.0))

// ---------- FILE I/O ----------
// Use import java.io.PrintWriter to write to a file
val writer = new PrintWriter("test.txt")
writer.write("Just some random text\nSome more random text")
writer.close()

// Use import scala.io.Source to read from files
val textFromFile = Source.fromFile("test.txt", "UTF-8")

// Iterate through each line in the file and print
val lineIterator = textFromFile.getLines
for(line <- lineIterator){
  println(line)
}
textFromFile.close()

// ---------- EXCEPTION HANDLING ----------

def divideNums(num1 : Int, num2 : Int) = try
{
  (num1 / num2)
} catch {
    case ex: java.lang.ArithmeticException => "Can't divide by zero"
} finally {
  // Clean up after exception here
}

println("3 / 0 = " + divideNums(3,0))

} // ---------- END OF MAIN ----------

// ---------- CLASSES ----------
// Classes are used as blueprints to create objects
// Objects define the attributes (fields) and capabilities (methods) of an
// object

class Animal(var name : String, var sound : String) {
  this.setName(name)

  // Any code that follows the class name is executed each time an
  // object is created as part of the Primary Constructor

  // This function is defined in the Animal companion object below
  val id = Animal.newIdNum

  // You must initialize all fields
  // protected means the field can only be accessed directly by methods
  // defined in the class or by subclasses
  // private fields can't be accessed by subclasses of Animal
  // public fields can be accessed directly by anything

  // protected var name = "No Name"
  // protected var sound = "No Sound"

  // Getters and setters are used to protect data
  def getName() : String = name
  def getSound() : String = sound
  def setName(name : String){
    // Check if the String contains numbers and if so don't allow
    if(!(name.matches(".*\\d+.*")))

      // this allows us to refer to any object without knowing its name
      this.name = name
    else
      this.name = "No Name"
  }
  def setSound(sound : String) {
    this.sound = sound
  }

  // Subclasses can't call this constructor unlike with Java
  def this (name : String){

    // This calls the primary constructor defined on the class line
    this("No Name", "No Sound")
    this.setName(name)
  }

  def this (){
    // This calls the primary constructor defined on the class line
    this("No Name", "No Sound")
  }

  // You can override any other method
  override def toString() : String = {

    // How to format Strings
    return "%s with the id %d says %s".format(this.name, this.id, this.sound)
  }

}

// The companion object for a class is where you'd define static class
// variables and functions in Java
object Animal {
  private var idNumber = 0
  private def newIdNum = { idNumber += 1; idNumber }
}

// ---------- INHERITANCE ----------
// A class that inherits from another gains all its fields and methods
// A class declared final can't be extended
class Dog (name : String, sound : String, growl : String) extends
Animal(name, sound){

  def this (name : String, sound : String){
    this("No Name", sound, "No Growl")
    this.setName(name)
  }

  def this (name : String){
    this("No Name", "No Sound", "No Growl")
    this.setName(name)
  }

  def this (){
    this("No Name", "No Sound", "No Growl")
  }

  // You can override any other method
  override def toString() : String = {
    return "%s with the id %d says %s or %s".format(
      this.name, this.id, this.sound, this.growl)
  }
}

// ---------- ABSTRACT CLASS ----------
// An abstract class can't be instantiated. It is made up of both abstract
// and non-abstract methods and fields

abstract class Mammal(val name : String){
  // An abstract field has no initial value
  var moveSpeed : Double

  // An abstract method has no body
  def move : String

}

class Wolf(name : String) extends Mammal(name){
  // You don't use override when defining abstract fields
  var moveSpeed = 35.0;

  def move = "The wolf %s runs %.2f mph".format(this.name, this.moveSpeed)

}

// ---------- TRAITS ----------
// A trait is a like a Java interface in that a class can extend more then 1
// Unlike Java interfaces traits can provide concrete methods and fields
trait Flyable {
  def fly : String

}

trait Bulletproof {
  def hitByBullet : String

  // You can define concrete methods in traits
  def ricochet(startSpeed : Double) : String = {
    "The bullet ricochets at a speed of %.1f ft/sec".format(startSpeed * .75)
  }
}

// The first trait starts with extends and then with for each other
class Superhero(val name : String) extends Flyable with Bulletproof{
  def fly = "%s flys through the air".format(this.name)

  def hitByBullet = "The bullet bounces off of %s".format(this.name)
}

} // ---------- End of object ScalaTut ----------
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
// Install Scala on Mac : Install Java VM, Install Homebrew,
// In terminal type: brew install scala
 
// Scala is the perfect choice if you want to explore functional
// programming without disregarding OOP
// Scala runs on the JVM which provides a ton of libraries
 
// File ends with the scala extension
 
// How to import library functions
import scala.io.StdIn.{readLine,readInt}
import scala.math._
import scala.collection.mutable.ArrayBuffer
import java.io.PrintWriter
import scala.io.Source
 
/*
You can execute commands directly in the terminal
REPL : Read Evaluate Print Loop
Type scala in terminal to start and :q to quit
 
// Creates a variable of the correct type
10 + 3 * 5 / 2
 
// You only use semicolons in Scala if you have multiple statements per line
 
// You can use that variable in the code that follows
"Your answer " + res0
 
// Define your own variable
var myName = "Derek"
 
// Define your own constant variable
val myAge = 40
 
// You can define the type
val lastName: String = "Banas"
 
// ---------- DATA TYPES ----------
 
// All datatypes in Scala are objects and they include
// (Get the max value with MaxValue)
// Byte : -128 to 127
// Boolean : true or false
// Char : unsigned max value 65535
// Short : -32768 to 32767
// Int : -2147483648 to 2147483647
// Long : -9223372036854775808 to 9223372036854775807
// Float : -3.4028235E38 to 3.4028235E38
// Double : -1.7976931348623157E308 to 1.7976931348623157E308
 
// A Double will only hold precision up to 15 digits
val num13 = 1.999999999999999
 
// Create a BigInt
val lgPrime = BigInt("622288097498926496141095869268883999563096063592498055290461")
lgPrime + 1
 
 Create a BigDecimal
val pi50 = BigDecimal("3.14159265358979323846264338327950288419716939937510")
0.00000000000000000000000000000000000000000000000001 + pi50
 
var randInt = 100000
 
// See functions available by typing randInt. (Click Tab)
// randInt.asInstanceOf[Double] casts number to a double
// randInt.isInstanceOf[Int] checks if is of type Int
 
// ---------- MATH ----------
"5 + 4 = " + (5 + 4)
"5 - 4 = " + (5 - 4)
"5 * 4 = " + (5 * 4)
"5 / 4 = " + (5 / 4)
"5 % 4 = " + (5 % 4)
 
// Shorthand notation (No randInt++, or randInt--)
randInt += 1
"randInt += 1" + randInt
 
randInt -= 1
"randInt -= 1" + randInt
 
randInt *= 1
"randInt *= 1" + randInt
 
randInt /= 1
"randInt /= 1" + randInt
 
// Import the math library in the terminal import scala.math._
 
abs(-8)
cbrt(64) // Cube root a^3 = n (Find a)
ceil(5.45)
round(5.45)
floor(5.45)
exp(1) // Euler's number raised to the power
pow(2, 2) // 2^2
sqrt(pow(2,2) + pow(2,2))
hypot(2, 2) // sqrt(X^2 + y^2)
log10(1000) // = 3 (10 × 10 × 10 = 10^3)
log(2.7182818284590455) // Natural logarithm to the base e
min(5, 10)
max(5, 10)
(random * (11 - 1) + 1).toInt // Random number between 1 and 10
toRadians(90)
toDegrees(1.5707963267948966)
 
// acos, asin, atan, atan2, cos, cosh, sin, sinh, tan, tanh
 
// ---------- CONDITIONALS ----------
// if statements are like Java except they return a value like the
// ternary operator
 
// Conditional Operators : ==, !=, >, <, >=, <=
// Logical Operators : &&, ||, !
 
var age = 18
 
val canVote = if (age >= 18) "yes" else "no"
 
// You have to use { } in the REPL, but not otherwise
if ((age >= 5) && (age <= 6)) {
  println("Go to Kindergarten")
} else if ((age > 6) && (age <= 7)) {
  println("Go to Grade 1")
} else {
  println("Go to Grade " + (age - 5))
}
 
true || false
!(true)
 
*/
 
object ScalaTut {
  def main(args: Array[String]) {
 
// ---------- LOOPING ----------
// To compile and run in the terminal
// 1. scalac ScalaTut.scala
// 2. scala ScalaTut
 
    var i = 0
 
    while (i <= 10) {
      println(i)
      i += 1
    }
 
    do {
      println(i)
      i += 1
    } while(i <= 20)
 
    for (i <- 1 to 10){
      println(i)
    }
 
    // until is often used to loop through strings or arrays
    val randLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for (i <- 0 until randLetters.length){
 
      // Get the letter in the index of the String
      println(randLetters(i))
    }
 
    // Used to iterate through a list
    val aList = List(1,2,3,4,5)
    for(i <- aList){
      println("List Item " + i)
    }
 
    // Store even numbers in a list
    var evenList = for { i <- 1 to 20
      // You can put as many conditons here separated with semicolons
      // as you need
      if (i % 2) == 0
    } yield i
 
    println("Even List")
    for(i <- evenList)
      println(i)
 
    // This loop assigns a value to the 1st variable and it retains
    // that value until the 2nd finishes its cycle and then it iterates
    for (i <- 1 to 5; j <- 6 to 10){
      println("i: " + i)
      println("j: " + j)
    }
 
    // There is no break or continue in Scala
    def printPrimes() {
 
      val primeList = List(1,2,3,5,7,11)
      for (i <- primeList){
 
        // Works like break if you return from a function
        if(i == 11){
          return
        }
 
        // Works like continue
        if (i != 1){
          println(i)
        }
 
      }
 
    }
 
    printPrimes
 
 
// ---------- INPUT / OUTPUT ----------
 
var numberGuess = 0
 
do{
  print("Guess a number : ")
 
  // You can also use readInt, readDouble, readByte, readShort, readLong,
  //
  numberGuess = readLine.toInt
 
  } while(numberGuess != 15)
 
  printf("You guessed the secret number %d\n", 15)
 
  // You can use string interpolation
  val name = "Derek"
  val age = 39
  val weight = 175.5
  println(s"Hello $name")
 
  println(f"I am ${age + 1} and weigh $weight%.2f")
 
  // printf Style Format Specifiers
  // %c : Characters
  // %d : Integers
  // %f : Floating Point Numbers
  // %s : Strings
  printf("'%5d'\n",5) // Right justify
 
  printf("'%-5d Hi'\n",5) // Left justify
 
  printf("'%05d'\n",5) // Zero Fill
 
  printf("'%.5f'\n",3.14) // 5 decimal minimum & maximum
 
  printf("'%-5s'\n", "Hi") // Left Justify String
 
  // Special Characters : \n, \b, \\, \a
 
// ---------- STRINGS ----------
var randSent = "I saw a dragon fly by"
 
// Get the 3rd index value
println("3rd Index : " + randSent(3))
 
// Get String length
println("String length " + randSent.length())
 
// Concatenate strings
println(randSent.concat(" and explode"))
 
// Compare strings for equality
println("Are strings equal " + "I saw a dragon".equals(randSent))
 
// Get index of a match
println("dragon starts at index ", randSent.indexOf("dragon"))
 
// Convert a string into an array
val randSentArray = randSent.toArray
 
for (v <- randSentArray)
  println(v)
 
// ---------- FUNCTIONS ----------
// def funcName (param1:dataType, param2:dataType) : returnType = {
//    function body
//    return valueToReturn
// }
 
// You can give parameters default values
def getSum( num1:Int = 1, num2:Int = 1) : Int = {
  return num1 + num2
}
 
println("5 + 4 = " + getSum(5,4))
 
// you can use named arguments
println("5 + 4 = " + getSum(num2=5, num1=4))
 
// A function that returns nothing (Procedure)
def sayHi() : Unit = {
  println("Hi how are you doing")
}
 
sayHi
 
// Receive variable number of arguments
def getSum2(args: Int*) : Int = {
  var sum : Int = 0
  for(num <- args){
    sum += num
  }
  sum
}
 
println("getSum2: " + getSum2(1,2,3,4,5))
 
// Recursion example calculating factorials
def factorial(num : BigInt) : BigInt = {
  if (num <= 1)
    1
  else
    num * factorial(num - 1)
}
 
// 1st: num = 4 * factorial(3) = 4 * 6 = 24
// 2nd: num = 3 * factorial(2) = 3 * 2 = 6
// 3rd: num = 2 * factorial(1) = 2 * 1 = 2
 
println("Factorial of 4 = " + factorial(4))
 
// ---------- ARRAYS ----------
// You'll use arrays when the size is fixed, or an ArrayBuffer for a
// variable size
 
// Create an array of Ints with a max size of 20
val favNums = new Array[Int](20)
 
// Create and initialize array in 1 line
val friends = Array("Bob", "Tom")
 
// Change the value in an array
friends(0) = "Sue"
 
println("Best Friend " + friends(0))
 
// Create an ArrayBuffer
val friends2 = ArrayBuffer[String]()
 
// Add an item to the 1st index
friends2.insert(0, "Phil")
 
// Add item to the next available slot
friends2 += "Mark"
 
// Add multiple values to the next available slot
friends2 ++= Array("Susy", "Paul")
 
// Add items starting at 2nd slot
friends2.insert(1, "Mike", "Sally", "Sam", "Mary", "Sue")
 
// Remove the 2nd element
friends2.remove(1)
 
// Remove 2 elements starting at the 2nd index
friends2.remove(1, 2)
 
// Cycle through and print ArrayList or Array
var friend : String = " "
for(friend <- friends2)
      println(friend)
 
// Add values to an array with a loop
for (j <- 0 to (favNums.length - 1)){
  favNums(j) = j
  println(favNums(j))
}
 
// Use yield to multiply all values times 2 and store in a new array
val favNumsTimes2 = for(num <- favNums) yield 2 * num
 
// Another way to print out values in array
favNumsTimes2.foreach(println)
 
// You can also store values that match a condition
var favNumsDiv4 = for(num <- favNums if num % 4 == 0) yield num
 
favNumsDiv4.foreach(println)
 
// Create a multidimensional array with Array.ofDim
var multTable = Array.ofDim[Int](10,10)
 
for(i <- 0 to 9){
  for(j <- 0 to 9){
    multTable(i)(j) = i * j
  }
}
 
for(i <- 0 to 9){
  for(j <- 0 to 9){
    printf("%d : %d = %d\n", i, j, multTable(i)(j))
  }
}
 
println("Sum : " + favNums.sum)
 
println("Min : " + favNums.min)
 
println("Max : " + favNums.max)
 
// Sort in desending order (Use < for assending)
val sortedNums = favNums.sortWith(_ > _)
 
// Return an indexed sequence and convert it into a string with commas
println(sortedNums.deep.mkString(", "))
 
// ---------- MAPS ----------
// Maps are collections of key value pairs
 
// Create a Map that can't be changed (Immutable)
val employees = Map("Manager" -> "Bob Smith", "Secretary" -> "Sue Brown")
 
// Get value using the key after checking that it exists
if(employees.contains("Manager"))
  printf("Manager : %s\n", employees("Manager"))
 
// Create a Mutable map
val customers = collection.mutable.Map(100 -> "Paul Smith",
  101 -> "Sally Smith")
 
printf("Cust 1 : %s\n", customers(100))
 
// Change a value using the key
customers(100) = "Tom Marks"
 
// Add an item
customers(102) = "Megan Swift"
 
// Output a Map
for((k,v) <- customers)
  printf("%d : %s\n", k, v)
 
// ---------- TUPLES ----------
// Tuples can hold values of many types, but they are immutable
 
var tupleMarge = (103, "Marge Simpson", 10.25)
 
printf("%s owes us $%.2f\n", tupleMarge._2, tupleMarge._3)
 
// Iterate through a tuple
tupleMarge.productIterator.foreach{ i => println(i)}
 
// Convert Tuple to String
println(tupleMarge.toString())
 
// ---------- CLASSES ----------
val rover = new Animal
rover.setName("Rover")
rover.setSound("Woof")
printf("%s says %s\n", rover.getName, rover.getSound)
 
val whiskers = new Animal("Whiskers", "Meow")
println(s"${whiskers.getName} with id ${whiskers.id} says ${whiskers.getSound}")
 
println(whiskers.toString)
 
val spike = new Dog("Spike", "Woof", "Grrrr")
 
spike.setName("Spike")
println(spike.toString)
 
val fang = new Wolf("Fang")
fang.moveSpeed = 36.0
println(fang.move)
 
// ---------- TRAITS ----------
val superman = new Superhero("Superman")
println(superman.fly)
println(superman.hitByBullet)
println(superman.ricochet(2500))
 
// ---------- HIGHER ORDER FUNCTIONS ----------
// Functions can be passed like any other variable
// You need the _ after the function to state you meant the function
val log10Func = log10 _
 
println(log10Func(1000))
 
// You can apply a function to all items of a list with map
List(1000.0,10000.0).map(log10Func).foreach(println)
 
// You can use an anonymous function with map as well
// Receives an Int x and multiplies every x by 50
List(1,2,3,4,5).map((x : Int) => x * 50).foreach(println)
 
// Filter will pass only those values that meet a condition
List(1,2,3,4,5,6).filter(_ % 2 == 0).foreach(println)
 
// Pass different functions to a function
def times3(num : Int) = num * 3
def times4(num : Int) = num * 4
 
// Define the function parameter type and return type
def multIt(func : (Int) => Double, num : Int ) = {
  func(num)
}
 
printf("3 * 100 = %.1f)\n", multIt(times3, 100))
 
// A closure is a function that depends on a variable declared outside
// of the function
val divisorVal = 5
val divisor5 = (num : Double) => num / divisorVal
println("5 / 5 = " + divisor5(5.0))
 
// ---------- FILE I/O ----------
// Use import java.io.PrintWriter to write to a file
val writer = new PrintWriter("test.txt")
writer.write("Just some random text\nSome more random text")
writer.close()
 
// Use import scala.io.Source to read from files
val textFromFile = Source.fromFile("test.txt", "UTF-8")
 
// Iterate through each line in the file and print
val lineIterator = textFromFile.getLines
for(line <- lineIterator){
  println(line)
}
textFromFile.close()
 
// ---------- EXCEPTION HANDLING ----------
 
def divideNums(num1 : Int, num2 : Int) = try
{
  (num1 / num2)
} catch {
    case ex: java.lang.ArithmeticException => "Can't divide by zero"
} finally {
  // Clean up after exception here
}
 
println("3 / 0 = " + divideNums(3,0))
 
} // ---------- END OF MAIN ----------
 
// ---------- CLASSES ----------
// Classes are used as blueprints to create objects
// Objects define the attributes (fields) and capabilities (methods) of an
// object
 
class Animal(var name : String, var sound : String) {
  this.setName(name)
 
  // Any code that follows the class name is executed each time an
  // object is created as part of the Primary Constructor
 
  // This function is defined in the Animal companion object below
  val id = Animal.newIdNum
 
  // You must initialize all fields
  // protected means the field can only be accessed directly by methods
  // defined in the class or by subclasses
  // private fields can't be accessed by subclasses of Animal
  // public fields can be accessed directly by anything
 
  // protected var name = "No Name"
  // protected var sound = "No Sound"
 
  // Getters and setters are used to protect data
  def getName() : String = name
  def getSound() : String = sound
  def setName(name : String){
    // Check if the String contains numbers and if so don't allow
    if(!(name.matches(".*\\d+.*")))
 
      // this allows us to refer to any object without knowing its name
      this.name = name
    else
      this.name = "No Name"
  }
  def setSound(sound : String) {
    this.sound = sound
  }
 
  // Subclasses can't call this constructor unlike with Java
  def this (name : String){
 
    // This calls the primary constructor defined on the class line
    this("No Name", "No Sound")
    this.setName(name)
  }
 
  def this (){
    // This calls the primary constructor defined on the class line
    this("No Name", "No Sound")
  }
 
  // You can override any other method
  override def toString() : String = {
 
    // How to format Strings
    return "%s with the id %d says %s".format(this.name, this.id, this.sound)
  }
 
}
 
// The companion object for a class is where you'd define static class
// variables and functions in Java
object Animal {
  private var idNumber = 0
  private def newIdNum = { idNumber += 1; idNumber }
}
 
// ---------- INHERITANCE ----------
// A class that inherits from another gains all its fields and methods
// A class declared final can't be extended
class Dog (name : String, sound : String, growl : String) extends
Animal(name, sound){
 
  def this (name : String, sound : String){
    this("No Name", sound, "No Growl")
    this.setName(name)
  }
 
  def this (name : String){
    this("No Name", "No Sound", "No Growl")
    this.setName(name)
  }
 
  def this (){
    this("No Name", "No Sound", "No Growl")
  }
 
  // You can override any other method
  override def toString() : String = {
    return "%s with the id %d says %s or %s".format(
      this.name, this.id, this.sound, this.growl)
  }
}
 
// ---------- ABSTRACT CLASS ----------
// An abstract class can't be instantiated. It is made up of both abstract
// and non-abstract methods and fields
 
abstract class Mammal(val name : String){
  // An abstract field has no initial value
  var moveSpeed : Double
 
  // An abstract method has no body
  def move : String
 
}
 
class Wolf(name : String) extends Mammal(name){
  // You don't use override when defining abstract fields
  var moveSpeed = 35.0;
 
  def move = "The wolf %s runs %.2f mph".format(this.name, this.moveSpeed)
 
}
 
// ---------- TRAITS ----------
// A trait is a like a Java interface in that a class can extend more then 1
// Unlike Java interfaces traits can provide concrete methods and fields
trait Flyable {
  def fly : String
 
}
 
trait Bulletproof {
  def hitByBullet : String
 
  // You can define concrete methods in traits
  def ricochet(startSpeed : Double) : String = {
    "The bullet ricochets at a speed of %.1f ft/sec".format(startSpeed * .75)
  }
}
 
// The first trait starts with extends and then with for each other
class Superhero(val name : String) extends Flyable with Bulletproof{
  def fly = "%s flys through the air".format(this.name)
 
  def hitByBullet = "The bullet bounces off of %s".format(this.name)
}
 
} // ---------- End of object ScalaTut ----------