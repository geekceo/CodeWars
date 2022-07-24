## The Hashtag Generator ##

<a href="https://www.codewars.com/kata/52449b062fb80683ec000024"><img src="https://www.codewars.com/packs/assets/logo.61192cf7.svg" height="64" width="64" ></a>

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

* It must start with a hashtag (```#```).
* All words must have their first letter capitalized.
* If the final result is longer than 140 chars it must return ```false```.
* If the input or the result is an empty string it must return ```false```.

##### Examples
```
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false