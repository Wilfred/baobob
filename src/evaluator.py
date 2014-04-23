from trifle_types import (List, Bytestring, Character, Symbol,
                          Integer, Float, Fraction,
                          Null, NULL,
                          Function, FunctionWithEnv, Lambda, Macro, Boolean,
                          Keyword, String)
from errors import UnboundVariable, TrifleTypeError, StackOverflow
from almost_python import zip
from environment import Scope, special_expressions
from parameters import is_variable_arity, check_parameters


# TODO: a stack class with push, pop and peek methods so we can call
# StackOverflow at the right time.

class Frame(object):
    def __init__(self, expression):
        # The expression we're evaluating, e.g. (if x y 2)
        self.expression = expression

        # The current point we've executed up to in the expression, e.g. 2.
        self.expression_index = 0

        # Results of parts of the expression that we have evaluated, e.g.
        # [TRUE, Integer(3)]
        self.evalled = []

    def __repr__(self):
        return ("expession: %r, index: %d, evalled: %r" %
                (self.expression, self.expression_index, self.evalled))



def evaluate_all(expressions, environment):
    """Evaluate a trifle List of expressions in the given environment.

    """
    result = NULL
    
    for expression in expressions.values:
        result = evaluate(expression, environment)

    return result


def evaluate(expression, environment):
    """Evaluate the given expression in the given environment.

    """
    stack = [Frame(expression)]

    # We evaluate expressions by pushing them on the stack, then
    # iterating through the elements of the list, evaluating as
    # appropriate. This ensures recursion in the Trifle program does
    # not require recursion in the interpreter.
    while stack:
        frame = stack[-1]
        print frame

        if isinstance(frame.expression, List):
            list_elements = frame.expression.values
            head = list_elements[0]
            raw_arguments = list_elements[1:]
            
            # Handle special expressions.
            if isinstance(head, Symbol) and head.symbol_name in special_expressions:
                special_expression = special_expressions[head.symbol_name]
                result = special_expression.call(raw_arguments, environment, stack)

            else:
                result = evaluate_function_call(frame.expression, environment, stack)

        else:
            result = evaluate_value(frame.expression, environment)

        # Returning None means we have work left to do, but a Triflfe value means
        # we're done with this frame.
        if not result is None:
            stack.pop()

            if stack:
                frame = stack[-1]
                frame.evalled.append(result)
            else:
                # We evaluated a value at the top level, nothing left to do.
                return result


# todo: this would be simpler if `values` was also a trifle List
def build_scope(name, parameters, values):
    """Build a single scope where every value in values (a python list) is
    bound to a symbol according to the parameters List given.

    If the parameters list contains `:rest foo`, any remaining arguments
    are passed a list in the named parameter.

    """
    varargs = is_variable_arity(parameters)

    if varargs:
        # The only negative slice supported by RPython is -1, so we
        # have to do it twice.
        normal_parameters = parameters.values[:-1][:-1]
    else:
        normal_parameters = parameters.values

    # Ensure we have the right number of arguments:
    check_parameters(name, parameters, List(values))

    scope = Scope({})
    for variable, value in zip(normal_parameters, values):
        scope.set(variable.symbol_name,  value)

    # todoc: varargs on macros
    # todo: consistently use the terms 'parameters' and 'arguments'
    if varargs:
        # Create a Trifle list of any remaining arguments.
        remaining_args = List(values[len(normal_parameters):])

        # Assign it to the variable args symbol.
        scope.set(parameters.values[-1].symbol_name, remaining_args)

    return scope


def expand_macro(macro, arguments, environment, stack):
    """Expand the given macro by one iteration. Arguments should be a
    Python list of unevaluated Trifle values.

    """
    # Build a new environment to evaluate with.
    inner_scope = build_scope(macro.name, macro.arguments, arguments)
    macro_env = environment.globals_only().with_nested_scope(inner_scope)

    expression = evaluate_all(macro.body, macro_env, stack)
    return expression


# TODO: allow users to change this at runtime.
MAX_STACK_DEPTH = 100


# todo: error on evaluating an empty list
def evaluate_function_call(expression, environment, stack):
    """Given a List representing a single Trifle function call (not a
    special expression), execute it in this environment.

    """
    frame = stack[-1]
    
    if frame.expression_index < len(expression.values):
        # Evaluate all of the elmenest of this list (we work left-to-right).
        raw_argument = expression.values[frame.expression_index]
        stack.append(Frame(raw_argument))

        frame.expression_index += 1
        return None

    else:
        # We've evaluated the function and its arguments, now call the
        # function with the evalled arguments.
        function = frame.evalled[0]
        arguments = frame.evalled[1:]

        if isinstance(function, Function):
            return function.call(arguments)

        elif isinstance(function, FunctionWithEnv):
            return function.call(arguments, environment)

        elif isinstance(function, Macro):
            assert False, "TODO: macros"

        elif isinstance(function, Lambda):
            # Build a new environment to evaluate with.
            inner_scope = build_scope(u"<lambda>", function.arguments, arguments)

            lambda_env = function.env.with_nested_scope(inner_scope)

            # Evaluate the lambda's body in our new environment.
            # TODO: use the stack
            return evaluate_all(function.body, lambda_env, stack)

        else:
            # todoc: this error
            raise TrifleTypeError(u"%s isn't a function or macro."
                                  % function.repr())


def evaluate_value(value, environment):
    if isinstance(value, Integer):
        # Integers evaluate to themselves
        return value
    elif isinstance(value, Float):
        # Floats evaluate to themselves
        return value
    elif isinstance(value, Fraction):
        # Fractions evaluate to themselves
        return value
    elif isinstance(value, Boolean):
        # Booleans evaluate to themselves
        return value
    elif isinstance(value, Null):
        # Null evaluates to itself
        return value
    elif isinstance(value, Keyword):
        # Keywords evaluate to themselves
        return value
    elif isinstance(value, String):
        # Strings evaluate to themselves
        return value
    elif isinstance(value, Bytestring):
        # Bytestrings evaluate to themselves
        return value
    elif isinstance(value, Character):
        # Characters evaluate to themselves
        return value
    elif isinstance(value, Function):
        # Functions evaluate to themselves
        return value
    elif isinstance(value, Macro):
        # Macros evaluate to themselves
        return value
    elif isinstance(value, Symbol):
        symbol_name = value.symbol_name
        if environment.contains(symbol_name):
            return environment.get(symbol_name)
        else:
            # TODO: suggest variables with similar spelling.
            raise UnboundVariable(u"No such variable defined: '%s'"
                                  % symbol_name)
    else:
        assert False, "I don't know how to evaluate that value: %s" % value
