import logging

logger = logging.getLogger(__name__)

class LoggingMiddleware:

    def process_request(self, request):
        logger.info(request)

    def process_response(self, request, response):
        logger.info(response)
