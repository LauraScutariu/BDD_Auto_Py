from pages.login_page import LoginPage
from behave import *

login_page = LoginPage


# click pe butonul de login
# @when('login:I login with credentials')
# def step_impl(context):
# 	login_page.fill_user_input("User Test")
# 	login_page.fill_pass_input("Decembrie93*")
# 	login_page.click_login_button()

@when(u'login: I login with a valid credentials')
def step_impl(context):
    raise NotImplementedError(u'STEP: When login: I login with a valid credentials')

