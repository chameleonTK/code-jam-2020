
# Google Code Jam Qualification 2020 
Here are how I approached each problem. 

**Reminder**: I am a big fan of `Python` so all things below will base on and only `Python`.


## Vesitigium
This problem is all about basic knowledge of array and for-loop. But one thing should be noticed here is that the test data is too small so you should not be borthered to optimize. If you code still run within O(n^2).

Hint: you can use `set()` to check whether a row/column has duplicated members. 

```python

col = [1,2,2,4]
colset = set(col)
if len(col) > len(colset) :
  return True
else:
  return False
```

## Nesting Depth
It looks like a problem that you need to use stack but it really is not have to.

The key idea of the problem is to keep track when level you are. 

* When you add `(`, you add one level
* When you add `)`, you remove one level

So when you get a list of numbers. Just iterate for each number then change the level to correspond to the number you currently have.

```python

num = [3,2,2,4]

level = 0
for n in num:
    if n > level:
        parens += ("("*(n-level))
    elif n < level:
        parens += (")"*(level-n))
        
    level = n
    parens += str(n)

# At the end; don't forget to close all parenthesis.
if level > 0:
    parens += (")"*(level))
```


## Parenting Partnering Returns
At first glance, it remined me of a meeting room problem that I learned when I was undergrad but this one is much more simpler than that. I saw a nice article writing about this problem [link](http://blog.gainlo.co/index.php/2016/07/12/meeting-room-scheduling-problem).  

The key idea is sorting the schedule by starting time and use a greedy approach. It was proved to give you an optimal solution (the least number of meeting room you need).

**Note**: The examples in the problem description seems a bit tricky. It gives you just a sorted list but you need to make sure that they are sorted and **IMPORTANTLY** you must return your outputs in the order that they are given by the problem.

The funny part is that I struggled with a way to check that two intevals are overlapped or not. My solution is list all possible cases and use `assert` to make sure that I do it right.

```python

def overlap(taska, taskb):
    start_a, end_a, i = taska
    start_b, end_b, j = taskb

    if (start_b == start_a) and (end_a == end_b):
        return True
    if start_a < start_b < end_a:
        return True
    if start_a < end_b < end_a:
        return True
    if start_b < start_a < end_b:
        return True
    if start_b < end_a < end_b:
        return True
    return False
    
assert (overlap((0, 100, 0), (100, 200, 1)) == False)
assert (overlap((0, 100, 0), (50, 200, 1)) == True)
assert (overlap((0, 100, 0), (50, 60, 1)) == True)
assert (overlap((0, 100, 0), (0, 50, 1)) == True)
assert (overlap((0, 100, 0), (0, 100, 1)) == True)
assert (overlap((0, 100, 0), (0, 200, 1)) == True)
assert (overlap((50, 100, 0), (0, 20, 1)) == False)
assert (overlap((50, 100, 0), (0, 50, 1)) == False)
assert (overlap((50, 100, 0), (0, 70, 1)) == True)
assert (overlap((50, 100, 0), (0, 100, 1)) == True)
assert (overlap((50, 100, 0), (0, 160, 1)) == True)

```
I'm sure this can be more optimised but I'm just little paranoid.

## ESAb ATAd (database)
Admittedly, this is the most annoying problem in this round but also the most fun. I spent 7 hours just to finish it but still isn't enough for the biggest testcase 😭.

The question is to get data which can be gathered through queries but the tricky part is the data can be changed -- they said because of `quantum ... fuzzy fuzzy word`.
So I approached this problem by finding a way to detect the changes.

Let's see all possible changes it can have.

````bash
# Nothing
000111100001 => 000111100001

# Complement
000111100001 => 111000011110

# Reverse
000111100001 => 100001111000

# Complement and Reverse
000111100001 => 011110000111 
````

First thing comes to my mind about detecting reverse is to find a pair of bits one the opposite ends e.g. (bit[0], bit[-1]). if they have different values, you can check whether the `reverse` occured by probing one of them.
But it will be confused when `complement` comes into play.

To go further, I found that two pair of bits one with the different and the same bits work. Let's see.

Consider A, B is a binary bit with its pair on the opposite end. which A has a couple with the same bit but B has a couple with different bit. So your data will look like this where `...` is any data in between but the number of data is symetry because of how these pair are chosen from.
````bash
...A...B...B'...A...
````

when changes occur, this is what happend.
````bash
# Complement
...A'...B'...B...A'...

# Reverse
...A...B'...B...A...

# Complement and Reverse
...A'...B...B'...A'...
````

So you can distinguish what was happended just by probing A and B again. This only use 2 queries to detect the changes. But the real issue is how to find these pairs -- this limited me to get the last test correctly which I almost make it but I don't.

My troble is to optimise the number of queries or to gleam as much information as possible through each query Which is really hard!!! 🔥🔥🔥 Maybe during finding the pairs you could get some information that can be used later; idk.

**Note**
To run this interactive chanllange in your local machine is also challanging. 3 hours was wasted by trying to understand how it works. If you working with online editor they have, it takes crazilly long time to test your code especially when you need to wait it to time out. Because if you write something wrong, you need to call `sys.exit(0)` manually. If not, your code will be stucked. So frustrating. Here is my tip.

Find these two files `interactive_runner.py` and `local_testing_tool.py` then run this command.

```bash
python interactive_runner.py python .\local_testing_tool.py <n> -- python <code>

```

where `<n>` is a test index; [0, 1, 2] and `<code>`is path to your python file.

If it stucks, open Task Manager and kill your python process.


## Indicium 
Crazy problem. Even now, I cannot come up with the effective solution.

This problem is asking you to construct a square NxN matrix that 
* all rows/columns has all numbers from [1-N]
* Sum of all diagnal elements ` sum([matrix[i][i] for i in range(N)])` == given K

It is not that hard for the first condition but I have no clue to the second.

My approach is using recursive and backtracking to contruct all possible matrix that satisfy both conditions but the time complexity is getting crazy. It works just for N < 5. Even when N==5, it goes dumps from time to time, especially when given K that is impossible to contruct a matrix, the programe has to finish all recursive then answer `IMPOSSIBLE`. Which is also impossible to run in a proper time limit. My stump idea is to run all the possible query and save it as a json then put it in my submitted code. So I made it!! Funny O(1) solution.

The second attempt is to construct one simple matrix and use row/column swapping to get a satisfying K but it didn't work. Only a few number of K can be constructed in this way.

Before I give up, I wrote another code which I started with getting diagonal values then use them to limit the options in recursive fuction but it is still not enough.

I am looking forward to an effecient solution to this problem. People sais it might be about `bipartite matching` but I'm still clueless about that word.



