from functools import reduce

from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")

@given('Exists restaurant registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from catalog.models import Book
    for row in context.table:
        book = Book(user=user)
        for heading in row.headings:
            setattr(book, heading, row[heading])
        book.save()

@when('I register restaurant')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('book/create'))
        if context.browser.url == context.get_url('book/create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()

