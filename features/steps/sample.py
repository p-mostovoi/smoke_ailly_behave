import time

import allure
from behave import *

use_step_matcher("re")


@given("we have behave installed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("we implement a test")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert True is not False


@then("behave will test it for us!")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.failed is False


@step("we implement a fail test")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert True is False


@given("Endpoint page '(?P<endpoint>.+)'")
def step_impl(context, endpoint):
    """
    :type context: behave.runner.Context
    :type Endpoint: str
    """
    context.endpoint = endpoint


@when("Open page with predefined endpoint")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    url = context.endpoint
    context.page = context.browser_context.new_page()
    context.page.goto(url)


@then("Take screenshot of page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    url = context.endpoint
    img = context.page.screenshot()
    time.sleep(2)
    allure.attach(
        img,
        name=f'{url}', attachment_type=allure.attachment_type.PNG
    )
    path = context.page.video.path()
    allure.attach(
        path,
        name=f'record', attachment_type=allure.attachment_type.WEBM
    )