# Diablo-Python
## Python code library

Diablo-Python is a boring simple library of reusable functions and utilities that can be reused in various projects. Diablo-Python probably isn't of much interest to the public as it's really just a personal library of repurposable code.

## Installation

This package is pip installable. Eiter of the following commands should work depending on what kind of an environment you're working in.
```
pip install git+https://github.com/bbusenius/Diablo-Python.git#egg=diablo_python
```
or 

```
pip3 install -e git+https://github.com/bbusenius/Diablo-Python.git#egg=diablo_python 
```

pass the -e flag to retain the editable source.

## The following packages are included in Diablo-Python

### simple_math 

A library of really simple math and personl finance functions. Below is a simple example using two of the functions to demonstrate how to calculate take home pay and savings rate based according to [Mr. Money Mustache](http://www.mrmoneymustache.com/2012/01/13/the-shockingly-simple-math-behind-early-retirement/).

```
from simple_math import take_home_pay, savings_rate

gross_pay = 5013.18
employer_match = 125.33
taxes_and_fees = 861.17

takehomepay = take_home_pay(gross_pay, employer_match, [taxes_and_fees])
savings = 2175.73
spending = takehomepay - savings
savingsrate = savings_rate(takehomepay, spending)

print('Your savings rate is: ')
print(savingsrate) 
```

*Would print*

```
Your savings rate is: 
50.86642633038289
```

[Read the documentation](https://diablo-python.readthedocs.org/en/latest/#module-simple_math)


### file_parsing

A library of functions used for parsing text files. Below are a few arbitrary examples from the library.

**is_numeric**

```
from file_parsing import is_numeric
is_numeric('eight')
is_numeric('32.982')
is_numeric('22')
```

*Returns:*

```
False
True
True
```

**total_hours**
A function used for totaling the hours of time spent on a project.
The function is designed to parse a list of text files formatted like this:

```
Test Project 1
<url:hours.vim> back to hours 

7/30/13
3:00-4:30 kickoff meeting 
1.5 hours
4:45-5:00 analyzed the current security certificate error, fixed a bad link
0.25 hours 
11:00-12:00 met with Alejandra to developed a timeline
1 hour 

8/12/13
10:00-1:15 sketching, brainstorming, looking at examples 
3.25 hours 

8/13/13
9:30-1:30 design comp
4 hours 
2:00-2:15 design comp
.25 hours 

8/14/13
9:30-3:15 design comp, further flushed out outline sketches, met with Alejandra to discuss wireframes
5.75 hours
```

*Example use:*

```
from file_parsing import total_hours
total_hours(['project1_2016.txt', 'project1_2015.txt'])
```
*Might return something like:*

```
89.75
```

[Read the documentation](https://diablo-python.readthedocs.org/en/latest/#module-file_parsing) 


### convert_php

A simple utility for taking a serialized php array and printing a visual representation of it in the console. This is really just for examining a datastructure. The heart of this utility is the translate_array method. It's used like this:

```
import convert_php
data = 'a:3:{i:1;s:6:"elem 1";i:2;s:6:"elem 2";i:3;s:7:" elem 3";}'
cp = convert_php.ConvertPHP()>>> cp.translate_array(data, 'javascript')
```

Returns:

```
var jsObject = {
   1 : {
      elem 1
   },
   2 : {
      elem 2
   },
   3 : {
      elem 3
   },
}
```

[Read the documentation](https://diablo-python.readthedocs.org/en/latest/#module-convert_php)



