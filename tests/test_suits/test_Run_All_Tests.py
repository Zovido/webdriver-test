import unittest
from tests.test_cases.LoginTest import LoginTest
from tests.test_cases.CreateUseCasesTest import CreateUseCasesTest
from tests.test_cases.EditUseCases import EditUseCasesTest

# get all tests from LoginValidationTest and CreateUseCasesTest class
login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
create_use_cases_test = unittest.TestLoader().loadTestsFromTestCase(CreateUseCasesTest)
edit_use_cases_test = unittest.TestLoader().loadTestsFromTestCase(EditUseCasesTest)

# create a test suite combining login and create_use_case
test_suite = unittest.TestSuite([login_test, create_use_cases_test, edit_use_cases_test])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)