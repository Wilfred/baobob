# Evaluation

A function call in Trifle lisp is written as a list, where the first
item in the list is the function, and the other items are the function
arguments.

For example, `(+ 1 2)` calls the function called `+` with the
arguments `1` and `2`.

### Evaluation order

Lists are evaluated left-to-right. In the form `(a b c)`:

1. `a` is evaluated first (presumably returning a function),
2. then `b` is evaluated,
3. then `c` is evaluated,
4. finally the function is called with the arguments.