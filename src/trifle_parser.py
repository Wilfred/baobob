# There's already a 'parser' in the standard library, so we're forced
# to call this trifle_parser.py.

from trifle_types import List, OpenParen, CloseParen
from errors import ParseFailed


def parse_inner(tokens, top_level):
    parse_tree = List()
    saw_closing_paren = False

    while tokens:
        token = tokens.pop(0)

        if isinstance(token, OpenParen):
            parse_tree.append(parse_inner(tokens, top_level=False))
        elif isinstance(token, CloseParen):
            if top_level:
                raise ParseFailed(u'Closing paren does not have matching open paren.')
            else:
                saw_closing_paren = True
                break
        else:
            parse_tree.append(token)

    if not top_level and not saw_closing_paren:
        raise ParseFailed(u'Open paren was not closed.')

    return parse_tree


def parse(tokens):
    return parse_inner(tokens.values, True)


def parse_one(tokens):
    """Only return the first expression parsed. Useful when parsing short
    code snippets.

    """
    return parse(tokens).values[0]
