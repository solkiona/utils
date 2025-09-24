""""
R-1.1 Write a short Python function, is_multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.

R-1.2 Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.

R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.

R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.

R-1.5 Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python’s comprehension syntax and the built-in sum function.

R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.

R-1.7 Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function.

R-1.8 Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for in-
dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element? Ans. j = n + k

R-1.9 What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80? Ans. range(50,81,10) i.e. start:end:step;  where start -> 50, end -> 81, step -> 10

R-1.10 What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8? Ans. range(8, -9, -2)

R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

R-1.12 Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module in-
cludes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
"""

def is_multiple(n,m):
    return n % m == 0

def is_even(k):
    even = ['2','4','6', '8', '0']
    k = str(k)
    return  k[-1] in even

def minmax(data):
    min = max = data[0] 
    for num in data:
        if num > max:
            max = num
        if num < min:
            min = num
    return min, max

def sum_of_squares(n):
    return sum([i**2 for i in range(n)])

def sum_of_squares_odd(n):
    li = []
    for i in range(n):
        if  i%2 != 0:
            li.append(i**2)
    return sum(li)

def sum_of_squares_odd_one_line(n):
    return sum([i**2 for i in range(n) if i%2 != 0])


def list_comprehension():
    """R-1.11"""
    return [2**i for i in range(9)]

def choice(seq):
    import random
    """R-1.12"""
    return seq[random.randrange(len(seq))]