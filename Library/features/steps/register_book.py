from behave import *


use_step_matcher("parse")

@when('I enter "/all_books"')
def step_imp(context):
    context.browser.visit(context.get_url('/all_books'))