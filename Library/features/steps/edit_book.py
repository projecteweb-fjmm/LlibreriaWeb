from behave import *
from django.db.models import Q

use_step_matcher("parse")

@given('Exists book registered by "{username}"') #PASS
def step_impl(context,username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from catalog.models import Book
    for row in context.table:
        book = Book(user=user)
        for heading in row.headings:
            setattr(book, heading, row[heading])
        book.save()


@when('I view the details for book "{title}"') #NO PASS
def step_impl(context,title):
    from catalog.models import Book
    book = Book.objects.get(title=title)
    context.browser.visit(context.get_url(book))


@when('I edit the current book')
def step_impl(context):
    context.browser.find_link_by_text('edit').click()
    form = context.browser.find_by_tag('form').first
    for heading in context.table.headings:
        context.browser.fill(heading, context.table[0][heading])
    form.find_by_value('Submit').first.click()

@then(u'I will view the details page for book')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I will view the details page for book')


@given('I\'m not logged in')
def step_impl(context):
    context.browser.visit(context.get_url('logout'))
    assert context.browser.is_text_present('login')


@when(u'I view the details for book')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I view the details for book')


@then(u'There is no "edit" link available')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There is no "edit" link available')

@then(u'I can delete book')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then There is no "edit" link available')

