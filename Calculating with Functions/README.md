## Calculating with Functions ##

<a href="https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39"><img src="https://www.codewars.com/packs/assets/logo.61192cf7.svg" height="64" width="64" ></a>

This time we want to write calculations using functions and get the results. Let's have a look at some examples:
```
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
```
##### Requirements:

* There must be a function for each number from 0 ("zero") to 9 ("nine")
* There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
* Each calculation consist of exactly one operation and two numbers
* The most outer function represents the left operand, the most inner function represents the right operand
* Division should be integer division. For example, this should return ``2``, not ```2.666666...```:
```
eight(divided_by(three()))
```
