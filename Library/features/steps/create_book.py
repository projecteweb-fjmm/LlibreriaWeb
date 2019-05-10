from behave import *
import operator
from functools import reduce
from django.db.models import Q

use_step_matcher("parse")

@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, email='username@username.com', password=password)

@given('I login as user "{username}" with password "{password}"') #PASS
def step_impl(context,username,password):
    context.browser.visit(context.get_url('/accounts/login/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('login').first.click()

@when('I register book') #PASS
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('/book/create'))
        if context.browser.url == context.get_url('/book/create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('submit').first.click()

@then('There are {count:n} book') #PASS
def step_impl(context,count):
    from catalog.models import Book
    assert not count == Book.objects.count()
