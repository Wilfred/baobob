# Bytestrings

Trifle supports bytestrings. Bytestrings are sequences of 8-bit
integers without any specific meaning: they may binary data such as
images, encoded text, or any other piece of data. Bytestrings are
mutable.

Bytestring literals consist of printable ASCII characters between double
quotes, e.g. `#bytes("foo")`.

Evaluating a bytestring literal always returns a fresh
bytestring. This ensures you can use literals in function bodies
without creating mutable static variables:

```
> (function empty-bytestring () #bytes(""))
#null
> (append! (empty-bytestring) 66)
#null
> (empty-bytestring) ; Still returns a fresh mutable bytestring
#bytes("")
```

## Bytestring functions

Predicates:

1. [bytestring?](Bytestrings-BytestringPredicate.md)
2. [empty?](Sequences-EmptyPredicate.md)

Creating a new bytestring:

1. [rest](Sequences-Rest.md)
2. [map](Sequences-Map.md)
3. [filter](Sequences-Filter.md)
4. [empty](Sequences-Empty.md)
5. [copy](Sequences-Copy.md)
6. [join](Sequences-Join.md)

Converting:

1. [decode](Bytestrings-Decode.md)

Accessing:

1. [get-index](Sequences-GetIndex.md)
2. [length](Sequences-Length.md)
3. [first](Sequence-First.md)
4. [second](Sequences-Second.md)
5. [third](Sequences-Third.md)
6. [fourth](Sequences-Fourth.md)
7. [fifth](Sequences-Fifth.md)
8. [last](Sequences-Last.md)

Modifying:

1. [set-index!](Sequences-SetIndex.md)
2. [insert!](Sequences-Insert.md)
3. [append!](Sequences-Append.md)
4. [push!](Sequences-Push.md)
5. [join!](Sequences-JoinMutate.md)
