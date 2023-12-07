from pages.books_page import BooksPage
from behave import *

books_page = BooksPage

 #click pe butonul de login
# @when('books:I click login button')
# def step_impl(context):
# 	books_page.click_login_button()

@when(u'books: I click login button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When books: I click login button')

# @then('books:I should land on books page')
# def step_impl(context):
# 	books_page.validate_correct_url()

@then(u'books: I should land on books page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then books: I should land on books page')



