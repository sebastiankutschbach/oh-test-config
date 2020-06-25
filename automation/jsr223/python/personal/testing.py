
import behave
from behave.__main__ import main as behave_main
from core.log import logging
from core.rules import rule
from core.triggers import when
from core.testing import run_test

reload(behave)

@rule("Execute gherkin tests")
@when("Item Run_Tests changed to ON")
def gherkin_tests(event):
    return_code = behave_main('./features')
    gherkin_tests.log.info('all tests passed') if return_code != 0 else gherkin_tests.log.warn('there were test failures')
