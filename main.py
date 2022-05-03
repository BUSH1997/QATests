import unittest
from signin.signin import SignIn
from signup.signup import Signup


def suite():
    suite = unittest.TestSuite()
    suite.addTest(SignIn('test_signin_positive'))
    suite.addTest(SignIn('test_signin_empty_field'))
    suite.addTest(SignIn('test_signin_no_user'))
    suite.addTest(SignIn('test_signin_incorrect_password'))
    suite.addTest(SignIn('test_signin_short_password'))
    suite.addTest(SignIn('test_signin_redirect_to_signup'))
    suite.addTest(Signup('test_signup_positive'))
    suite.addTest(Signup('test_signup_empty_field'))
    suite.addTest(Signup('test_signup_user_exists'))
    suite.addTest(Signup('test_signup_passwords_not_match'))
    suite.addTest(Signup('test_signup_wrong_email_wrong'))
    suite.addTest(Signup('test_signup_redirect_to_signin'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
