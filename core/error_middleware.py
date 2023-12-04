import logging
import traceback

logger = logging.getLogger(__name__)


class LogErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        logger.error("\n----intercepted 500 error stack trace----")
        logger.error(exception)
        logger.error(type(exception))
        tb = exception.__traceback__
        logger.error(traceback.format_exception(type(exception), exception, tb))
        logger.error("----\n")
        return None  # Let other middlewares do further processing
