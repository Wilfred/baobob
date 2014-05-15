import unittest
from cStringIO import StringIO
from contextlib import contextmanager

from mock import patch

from main import entry_point, USAGE


class TopLevelWithoutArgsTest(unittest.TestCase):
    def test_no_args_return_value(self):
        return_value = entry_point([])
        self.assertNotEqual(return_value, 0)
        
    def test_no_args_prints_usage(self):
        mock_stdout = StringIO()

        with patch('sys.stdout', mock_stdout):
            entry_point([])

        self.assertEqual(mock_stdout.getvalue(), USAGE + '\n')


# TODO: use this for `print!` unit tests too.
@contextmanager
def mock_stdout():
    """Temporarily patch sys.stdout and return the StringIO buffer that
    was written to.

    """
    fake_stdout = StringIO()

    with patch('sys.stdout', fake_stdout):
        yield fake_stdout


class TopLevelSnippetTest(unittest.TestCase):
    def test_snippet(self):
        with mock_stdout() as stdout:
            entry_point(['trifle', '-i', '(+ 1 2)'])

        self.assertEqual(stdout.getvalue(), '3\n')

    def test_snippet_error(self):
        """If given a snippet that throws an error, we should have a non-zero
        return code.

        """
        return_value = entry_point(['trifle', '-i', '(+ 1 i-dont-exist)'])
        self.assertNotEqual(return_value, 0)
