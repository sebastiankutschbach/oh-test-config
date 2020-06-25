from core.log import logging

from behave.log_capture import capture

def before_all(context):
    logging.info('starting gherkin tests')
    context.config.setup_logging()
    context.config.log

@capture
def after_scenario(context):
    logging.debug(context)
