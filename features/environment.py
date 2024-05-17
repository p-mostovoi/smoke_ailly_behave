"""
 -----------------------------------------------------------------------------
 BEHAVE ENVIRONMENT:
-----------------------------------------------------------------------------
"""
# pylint: disable=locally-disabled, import-error, line-too-long, logging-fstring-interpolation, unused-argument, unused-import, bare-except
import json
import logging
import os

from pathlib import Path
from playwright.sync_api import sync_playwright

root_path = Path(__file__).parent.parent
log_path = root_path.joinpath("logs")
LOG_LEVEL = logging.DEBUG


def before_all(context):
    """
    Actions that should be done before all
    """
    playwright = sync_playwright().start()
    context.playwright = playwright


def after_all(context):
    """
    Actions that should be done after all
    """
    context.playwright.stop()


def before_feature(context, feature):
    """
    Actions that should be done before any feature
    """

    # Browser settings depending on SUT
    browser = context.playwright.chromium.launch(headless=True)
    context.browser = browser
    context.user_tokens = {}


def after_feature(context, feature):
    """
    Actions that should be done after any feature
    """
    try:
        context.browser.close()
    except:
        pass



def before_scenario(context, scenario):
    """
    Actions that should be done before any scenario
    """
    context.browser_context = context.browser.new_context()

def after_scenario(context, scenario):
    """
    Actions that should be done after any feature
    """
    # context.page.close()
    context.browser_context.close()


def before_step(context, step):
    """
    Actions that should be done before each step
    """
    pass


def after_step(context, step):
    """
    Actions that should be done after each step
    """
    pass

def before_tag(context, tag):
    """
    Actions that should be done before each tag
    """
    pass


def after_tag(context, tag):
    """
    Actions that should be done after each step
    """
