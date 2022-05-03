import unittest
from signin.signin import PythonOrgSearch


def suite():
    suite = unittest.TestSuite()
    suite.addTest(PythonOrgSearch('test_signin_positive'))
    suite.addTest(PythonOrgSearch('test_signin_empty_field'))
    suite.addTest(PythonOrgSearch('test_signin_no_user'))
    suite.addTest(PythonOrgSearch('test_signin_incorrect_password'))
    suite.addTest(PythonOrgSearch('test_signin_short_password'))
    suite.addTest(PythonOrgSearch('test_signin_redirect_to_signup'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
