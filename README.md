# My Advent of Code 2017 Solutions

My (ad hoc) solutions to the
[Advent of Code 2017](https://adventofcode.com/2017/)
programming challenges.

And yes, the whole import and testing part is very
hackish. This is a very "top-of-the-knee" project.

If I had to do this again, I'd go for less
boilerplate and improve my import/lib use knowledge.

~Work in Progress~: Days Solved: 1-5 of 25

Execute
-------

Install needed pytest and pytest-mock on virtualenv
```
$ make init
```

Run and test (inside virtualenv)
```
$ make run_all
$ make test_all
```

Run and test specific solution (inside virtualenv)
```
$ ./run.py 1 1
$ ./test.py 1
```
Runs day 1, part 1 and tests day 1 (all parts)
