"""
The master checkit module.
"""
from MWSyntaxChecker import Checks

def check_it(test_name, test_text):
    """Check a single rule."""
    test = getattr(Checks, test_name, None)
    if test is None:
        raise ValueError("The test '{}' does not exist.".format(test_name))
    test.run(test_text, console=True)

def check_all(test_text):
    """Check all rules available for text."""
    for check in dir(Checks):
        if not check.startswith('_'):
            check_it(check, test_text)
