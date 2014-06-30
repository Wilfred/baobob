# Hashmaps

Trifle supports hashmaps. A hashmap is a mutable mapping of keys to
values.

Hashmap literals are written as an even number of items between curly
brackets, e.g. `{1 2 3 4}`. Values are evaluated, so `{(+ 1 2) 3}` is
the same as `{3 3}`. Commas are treated as whitespace, so `{1 2, 3 4}`
is the same as `{1 2 3 4}`. Hashmap literals are read left-to-right,
so duplicate keys get overwritten, e.g. `{1 2, 1 3}` is the same as
`{1 3}`.

## Hashmap functions

None yet.