import unittest
from signin.signin import SignIn
from signup.signup import Signup
from basket.basket import Basket
from profile.profile import Profile


def suite():
    suite = unittest.TestSuite()
    # suite.addTest(SignIn('test_signin_positive'))
    # suite.addTest(SignIn('test_signin_empty_field'))
    # suite.addTest(SignIn('test_signin_no_user'))
    # suite.addTest(SignIn('test_signin_incorrect_password'))
    # suite.addTest(SignIn('test_signin_short_password'))
    # suite.addTest(SignIn('test_signin_redirect_to_signup'))
    # suite.addTest(Signup('test_signup_positive'))
    # suite.addTest(Signup('test_signup_empty_field'))
    # suite.addTest(Signup('test_signup_user_exists'))
    # suite.addTest(Signup('test_signup_passwords_not_match'))
    # suite.addTest(Signup('test_signup_wrong_email_wrong'))
    # suite.addTest(Signup('test_signup_redirect_to_signin'))
    # suite.addTest(Basket('test_basket'))
    # suite.addTest(Basket('test_basket_count'))
    # suite.addTest(Basket('test_basket_refresh'))
    # suite.addTest(Basket('test_basket_delete_product'))
    # suite.addTest(Basket('test_basket_empty'))
    # suite.addTest(Basket('test_basket_increase_in_basket'))
    # suite.addTest(Basket('test_basket_change_sum_of_one_product'))
    # suite.addTest(Basket('test_basket_change_sum_many_products'))
    # suite.addTest(Basket('test_basket_selector'))
    # suite.addTest(Basket('test_success_order'))
    suite.addTest(Profile('test_profile_update_button'))
    suite.addTest(Profile('test_profile_update_notification'))
    suite.addTest(Profile('test_update_name'))
    suite.addTest(Profile('test_update_surname'))
    suite.addTest(Profile('test_update_email'))
    suite.addTest(Profile('test_update_sex'))
    suite.addTest(Profile('test_update_birthday'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
