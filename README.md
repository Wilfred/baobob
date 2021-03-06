# Trifle Lisp [![Build Status](https://img.shields.io/travis/Wilfred/trifle/master.svg)](https://travis-ci.org/Wilfred/trifle) [![Coverage Status](http://img.shields.io/coveralls/Wilfred/trifle/master.svg)](https://coveralls.io/r/Wilfred/trifle) [![Requirements Status](https://requires.io/github/Wilfred/trifle/requirements.svg?branch=master)](https://requires.io/github/Wilfred/trifle/requirements/?branch=master) [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Wilfred/trifle/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Wilfred/trifle/?branch=master) [![Code Health](https://landscape.io/github/Wilfred/trifle/master/landscape.png)](https://landscape.io/github/Wilfred/trifle/master)

*A sweet and friendly lisp*

Current status: Only a basic interpreter implemented. Please see
[the docs](docs/Introduction.md) to see what's available.

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc/generate-toc again -->
**Table of Contents**

- [Trifle Lisp](#trifle-lisp)
    - [Goals](#goals)
        - [Prototypes to Products](#prototypes-to-products)
        - [Modular](#modular)
        - [Iterating](#iterating)
        - [Self-documenting](#self-documenting)
        - [Documented](#documented)
        - [Expressive](#expressive)
        - [Re-Examined](#re-examined)
        - [Accessible](#accessible)
        - [Friendly](#friendly)
        - [Human Focused Performance](#human-focused-performance)
        - [Missing Features](#missing-features)
    - [Release History](#release-history)
        - [v0.11](#v011)
        - [v0.10](#v010)
        - [v0.9](#v09)
        - [v0.8](#v08)
        - [v0.7](#v07)
        - [v0.6](#v06)
        - [v0.5](#v05)
        - [v0.4](#v04)
        - [v0.3](#v03)
        - [v0.2](#v02)
        - [v0.1](#v01)

<!-- markdown-toc end -->

## Goals

Trifle is:

### Prototypes to Products

Trifle will let users write a quick and dirty script that uses global
variables and mutable state everywhere. Trifle will also let users unit
test, lint, type check and add contracts to their code. Users will be
able to choose how much safety they want.

### Modular

Trifle actively avoids including a standard library. Instead, it opts
for including a package manager so that each package can evolve
separately. Packages use [semantic versioning](http://semver.org/) and
declare their dependencies.

Trifle takes an 'open implementation' approach. Wherever possible,
functionality is built on top of the core, to encourage
experimentation and to minimise the amount of non-Trifle code users
must read. Where non-essential functions are written in RPython for
performance, an equivalent Trifle implementation will be included.

In spite of encouraging libraries to live outside of the core, the
Trifle community will promote a set of defaults, so new users have a
standard set of tools to get started with.

Influences: Scheme's small core, CLOS as a library, npm, Smalltalk

### Iterating

The Trifle standard is not set in stone. Major versions may break
backwards compatibility. The featureset will change over time to
maximise readability and expressiveness.

Influences: Python 3 cleaning up semantics

### Self-documenting

Trifle seeks to make code understandable, when looking at both
individual pieces of code or the high-level overview. Trifle supports
docstrings and cross-references to package documentation.

Names are chosen to be clear, self-explanatory and minimally
abbreviated. Code should be concise through well-chosen abstraction
instead of very short names.

Influences: Python's readability, Python doctests, Elisp docstrings

### Documented

Trifle seeks to be clearly and thoroughly documented. Documentation
should include examples wherever possible. Each page in the
documentation should have a small and well-defined purpose, with each
function on a separate page. Users should be able to leave comments on
the documentation for later readers.

Influences: PHP docs, clojuredocs

### Expressive

Trifle features closures, unhygenic macros and reader macros.

Influences: Common Lisp

### Re-Examined

Trifle re-considers traditional lisp features. There is no built-in
Cons cell (lists are vectors). Some common functions have been renamed
(car) and others have different behaviours to other lisps (last
returns the last element in a list). Trailing parentheses are
encouraged to aid readability.

Influences: Clojure

### Accessible

Trifle places a high value on code readability for users who have
programmed in other languages but are new to Trifle (or lisps in
general). It tries to use familiar terminology and avoids
abbreviations.

### Friendly

The Trifle community strives to be friendly and helpful. We have a
code of conduct that applies to all official Trifle communication
channels.

The language and its libraries are developed in the open on
GitHub. The package manager allows different forks of libraries to
coexist.

Influences: Rust/CoffeeScript on GitHub

### Human Focused Performance

When Trifle features have to decide between helping the user and
helping the machine, Trifle sides with the user every time.

That said, Trifle seeks to provide a fast implementation for this
human-focused feature set. We do this by implementing the intepreter
in RPython, giving us a JIT with little work. The language provides
also provides opt-in TCO.

Influences: Pypy, Scheme

### Missing Features

A new programming language should really have a good answer to 'how do
I run it in the browser?', 'how do I scale it to multiple cores?' and
'how do I interface with C code?'. Since this is an experimental
language, we are cheerfully ignoring these questions for now.

## Release History

### v0.12 (not yet released)

Fixed `VERSION` which hadn't been updated since version 0.9.

### v0.11

Added hashmaps, e.g. `{1 2, 3 4}`. Please see the docs for a full
description. Added the functions `hashmap?`, `get-key`, `get-items`
and `set-key!`.

It's now an error to repeat parameters (e.g. calling
`(lambda (x x) #null)`) in a function or macro.

Commas are now treated as whitespace, so `(1, 2, 3)` is a valid list
literal.

Fixed equality bugs in fractions and keywords. Fixed an equality bug
with booleans returned from `defined?`.

### v0.10

Fractions: Fraction numerator and denominators are now arbitrary size
and never overflow. They were previously limited to 32 bits.

Integers: Integers are now arbitrary size and never overflow. They
were also previously limited to 32 bits. Note that indexing into
sequences above 2 ** 32 will not yet work.

Parsing: Fixed a bug with `parse` where it sometimes returned a list
of one error instead of throwing an error on invalid input.

### v0.9

Shell: Added a pure Trifle shell program: `shell.tfl`. The interpreter
itself now only accepts file paths or `-i` snippets.

Exceptions: Added the function `exception-type`. Fixed a bug where
`arity-error` or `stack-overflow` couldn't be caught if thrown by a
built-in function or macro.

[Emacs mode](https://github.com/Wilfred/.emacs.d/blob/gh-pages/user-lisp/trifle-mode.el):
trifle-mode now understand how to indent Trifle code.

Sequences: Added a separate docs page for sequences. Added the
function `sequence?`.

Evaluation: Fixed an interpreter crash on evaluating an empty list.

Macros: Fixed an interpreter crash on throwing exception during macro
expansion.

Literals: Repeatedly evaluating list, string and bytestring literals
now returns a fresh copy every time. This fixes programs like the
following:

```
(function empty-string () "")
(set! x (empty-string))
(append! x 'a')
(empty-string) ; Used to return "a"!
```

File handles: Added the function `flush!`.

Symbols: `_` is now a legal symbol. Symbols may now include uppercase
characters. Added the function `symbol?`.

Strings: Added the constant `VERSION`.

Loops: Added the macro `loop` for infinite loops.

Generic functions: Added the function `printable`.

### v0.8

Exceptions: Added an exception system. All errors thrown by all
built-ins are now exceptions. Added the special expression `try` and
the built-in functions `throw` and `message`. Defined the built-in
exceptions `error` (the base exception), `stack-overflow`, `no-such-variable`, `parse-failed`, `lex-failed`,
`value-error`, `wrong-type`, `wrong-argument-number`,
`division-by-zero`, `file-not-found`, and `changing-closed-handle`.

Sample programs: Added a factorial program.

Errors messages: Improved wording on calling non-callables. Arity
errors now include more information on the number of arguments
received.

Booleans: `if` now always requires three arguments. Added `when` for
when users don't care about else. `unless` was renamed to `when-not`.

Bytestrings: The lexer now understand all legal escapes in bytestring
literals. Fixed a lexing bug with consecutive bytestring literals.

Numbers: `>`, `>=`, `<` and `<=` now work with fractions too.

Stack: Overflowing the stack now raises an error rather than crashing
the interpreter.

### v0.7

Bytestrings: Added the function `bytestring?`.

Sequences: Added the functions `empty`, `empty?`, `copy`, `join!` and
`join`.

Booleans: Removed `truthy?`. `if` and `while` now require booleans for
their conditions, instead of just truthy values.

Docs: Added a 'generic functions' section.

Generic functions: Added `identity`.

Numbers: Added a fraction type. Added support for fractions to `+`,
`-`, `*` and `/`.

Errors: Various minor improvements to error messages to be more
consistent and helpful.

### v0.6

Installation: It's now possible to do `make install` and `make
uninstall` to install a Trifle interpreter.

Prelude: The interpreter is now more helpful when it can't find the
prelude (instead of crashing).

Escape sequences: Trifle now supports backslash escape sequences in
strings and characters, so `'\''` and `"they said \"hello\""` are now
legal literals.

Booleans: Added short-circuiting macros `and` and `or`.

Numbers: Added the functions `>`, `>=` and `<=`.

Equality: Fixed a bug where character equality considered characters
to not be `equal?` if they are not `same?`. Identical characters are
now equal, so `(equal? 'a' a')` is `#true`.

Lists: Added the built-in function `insert!`. `append!` and `push!` have been
rewritten as Trifle functions in the prelude. Added the function `filter`.

Special expressions: Special expressions are no longer first class
values. You can no longer do things like `(set! foo if)` or
`((lambda (f x y) (f x y)) if #true 1)`. This is intended to make
static analysis more tractable.

### v0.5

Strings: Strings are now sequences of characters and all sequence
functions (`get-index`, `set-index!`, `append!`, `push!`, `length`,
`map`, `rest`, `first`, `second`, `third`, `fourth`, `fifth`, and
`last`) can be called on them. Also added a `string?` function.

Character: Added a character datatype. Added a `character?` function.

Errors: Fixed error messages in `length` and `parse` which incorrectly
stated the expected type.

Docs: Fixed some minor mistakes.

### v0.4

Bytestrings: 'Bytes' are now called bytestrings, and literal
bytestrings are recognised by the interpreter
(e.g. `#bytes("abc")`). Bytestrings are now mutable.

Sequences: Trifle now has the concept of a 'sequence', which is a
mutable ordered datatype. Lists and bytestrings are both
sequences. The expressions `length`, `get-index`, `set-index!`,
`first`, `second`, `third`, `fourth`, `fifth`, `append!` and `map` now
handle sequences. Added the function `last`. The macro `for-each` now
handles sequences.

Lists: Added the functions `list?`, `rest` and `range`.

Booleans: The literal boolean syntax has changed to `#true` and
`#false`. Added the macros `unless` and `case`. `truthy?` has moved to
the prelude. The values `""`, `#bytes("")` and `0.0` are now considered
to be falsey.

Null: The literal null syntax has changed to `#null`.

Strings: `print` is now `print!`.

Numbers: Added the functions `zero?`, `mod` and `div`.

Errors: `get-index`, `set-index!` and `push!` now use arity errors and value
errors where appropriate. Fixed some error wording issues with `open`.

IO: Added an `exit!` function.

Evaluation: `quote` is now much stricter about arguments passed to
`unquote` and `unquote*` instead of silently ignoring them. `call` can
now handle macros as well as functions.

Interpreter: When given the path to a function, the result of the
program is no longer automatically printed. Use `print!` in your
program instead.

Editing: There is now an Emacs major mode available, see
[Getting Started](docs/Getting-Started.md).

Sample programs: Added [hello world](sample_programs/hello_world.tfl),
[fibonacci](sample_programs/fibonacci.tfl) and
[fizzbuzz](sample_programs/fizzbuzz.tfl) sample programs.

Licensing: Trifle is now dual-licensed under MIT and Apache 2.0. This
will not change again.

### v0.3

File handles: Added a file handle datatype, and added the functions
`open`, `close`, `read` and `write!`.

Bytes: Added a bytes datatype, and added the function `decode`.

Strings: Fixed many unicode bugs. Added the function `encode`.

Equality: Added the function `equal?`. `same?` no longer treats
numbers specially, so it's now possible for two numbers to be `equal?`
but not `same?`. `same?` now throws ArityError if given the wrong
number of arguments.

Built-in functions: String representations have been improved.

Docs: The documentation has been grouped into more logical sections,
and datatypes have been separated from other documentation pages.

### v0.2

Numbers: This release adds floats, and makes parsing stricter. `123foo`
was previously a symbol, it is now a syntax error. The function `/`
and macro `dec!` have been added.

Evaluation: The functions `call`, `parse`, `eval` and `defined?` have
been added.

Macros: Fixed a bug with `macro` where it reported the
wrong argument as incorrect. Macros now always require a body.

Errors: Many built-in functions have had their error messages
improved, and raise an arity error (not a type error) on the wrong
number of arguments.

Documentation: Docs have been improved, and `function` and `let` have
gained docmentation. We've cleared up the difference between functions
(arguments always evaluated) and special expressions (does not
evaluate some arguments).

I/O: The function `input` (read a line from stdin) has been added.

Workflow: We now use coveralls to measure code coverage on Python code
for every checkin. Note we don't have any facility for measuring
coverage on Trifle code yet.

### v0.1

This release includes integers, lists, booleans, strings (though you
can do little with strings currently), symbols, loops, functions,
closures and macros.
