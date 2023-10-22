import logging

logger = logging.getLogger(__name__)

class LoggingMiddleware:
    def __init__(self, get_response):
            self.get_response = get_response
            # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        logger.info(request.body)
        logger.info('Request data')
        logger.info(request.data)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        logger.info(response.content)
        return response
