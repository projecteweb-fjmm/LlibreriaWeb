from __future__ import print_function
from behave import *
import operator
from django.db.models import Q
from django.urls.base import reverse

use_step_matcher("parse")

@step('Exists a user "{username}" with password "{password}"')
def step_impl(context,username,password):