# Copyright 2014 Wilfred Hughes. See docs/Licensing.md.
#
# Licensed under the Apache Licence, Version 2.0 <Licence-Apache.txt or
# http://www.apache.org/licenses/LICENSE-2.0> or the MIT licence
# <Licence-MIT.txt or http://opensource.org/licenses/MIT>, at your
# option. This file may not be copied, modified, or distributed
# except according to those terms.

import sys
import os

from rpython.rtyper.module.ll_os_environ import getenv_llimpl

from interpreter.lexer import lex
from interpreter.trifle_parser import parse
from interpreter.evaluator import evaluate_all, is_thrown_exception
from interpreter.environment import fresh_environment
from interpreter.errors import error


def get_contents(filename):
    """Return the contents of this filename, as a unicode object. Assumes
    the file is UTF-8 encoded.

    """
    fp = os.open(filename, os.O_RDONLY, 0777)

    program_contents = ""
    while True:
        read = os.read(fp, 4096)
        if len(read) == 0:
            break
        program_contents += read
    os.close(fp)

    return program_contents.decode('utf-8')


def env_with_prelude():
    """Return a fresh environment where the prelude has already been
    evaluated.

    """
    # todo: document TRIFLEPATH
    # todo: should we inline the prelude, so changing TRIFLEPATH doens't break this?
    trifle_path = getenv_llimpl("TRIFLEPATH") or "."
    prelude_path = os.path.join(trifle_path, "prelude.tfl")
    
    # Trifle equivalent of PYTHONPATH.
    try:
        code = get_contents(prelude_path)
    except OSError:
        # TODO: work out which error occurred (not found/wrong
        # permissions/other) and be more helpful.
        print "Could not find prelude.tfl. Have you set TRIFLEPATH?"
        raise

    # TODO: either of these could return errors, and we should handle that.
    lexed_tokens = lex(code)
    parse_tree = parse(lexed_tokens)

    env = fresh_environment()
    result = evaluate_all(parse_tree, env)

    assert not is_thrown_exception(result, error), "Error when evaluating prelude: %s" % result

    return env


USAGE = """Usage:
./trifle -i <code snippet>
./trifle <path to script>"""


def entry_point(argv):
    """Either a file name:
    $ ./trifle ~/files/foo.tfl

    A code snippet:
    $ ./trifle -i '1 2'

    """
    if len(argv) == 2:
        # open the file
        filename = argv[1]

        if not os.path.exists(filename):
            print 'No such file: %s' % filename
            return 2

        try:
            env = env_with_prelude()
        except OSError:
            return 2
        code = get_contents(filename)
        lexed_tokens = lex(code)

        if is_thrown_exception(lexed_tokens, error):
            print u'Uncaught error: %s: %s' % (
                lexed_tokens.exception_type.name,
                lexed_tokens.message)
            return 1

        parse_tree = parse(lexed_tokens)
        try:
            result = evaluate_all(parse_tree, env)

            if is_thrown_exception(result, error):
                # TODO: a proper stack trace.
                print u'Uncaught error: %s: %s' % (result.exception_type.name,
                                          result.message)
                return 1
        except SystemExit:
            return 0
        return 0
    
    elif len(argv) == 3:
        if argv[1] == '-i':
            try:
                env = env_with_prelude()
            except OSError:
                return 2
            code_snippet = argv[2].decode('utf-8')
            lexed_tokens = lex(code_snippet)

            if is_thrown_exception(lexed_tokens, error):
                print u'Uncaught error: %s: %s' % (
                    lexed_tokens.exception_type.name,
                    lexed_tokens.message)
                return 1
            
            parse_tree = parse(lexed_tokens)

            try:
                result = evaluate_all(parse_tree, env)

                if is_thrown_exception(result, error):
                    # TODO: a proper stack trace.
                    print u'Uncaught error: %s: %s' % (result.exception_type.name,
                                              result.message)
                    return 1
                else:
                    print result.repr().encode('utf-8')
                
            except SystemExit:
                return 0
            return 0
            
    print USAGE
    return 1


def target(*args):
    return entry_point, None


if __name__ == '__main__':
    entry_point(sys.argv)
