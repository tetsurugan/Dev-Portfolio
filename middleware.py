##for a classmate will be deleted later


import logging
import time
from datetime import datetime
from django.http import HttpResponseForbidden

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    """ Middleware to log incoming requests, user, response status, and processing time. """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        
        response = self.get_response(request)
        
        end_time = time.time()
        processing_time = end_time - start_time
        
        log_message = (
            f"[{datetime.now()}] {request.method} {request.path} - "
            f"User: {request.user if request.user.is_authenticated else 'Anonymous'} - "
            f"Status: {response.status_code} - "
            f"Processing Time: {processing_time:.4f}s"
        )
        
        logger.info(log_message)  # Save logs in Django's logging system

        return response
##Security Middleware ###
class SecurityMiddleware:
    """ Middleware to restrict IPs and add security headers. """

    BLOCKED_IPS = ['123.45.67.89',]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = self.get_client_ip(request)

        if ip in self.BLOCKED_IPS:
            logger.warning(f"⛔ Blocked access from {ip}")
            return HttpResponseForbidden("Access Denied")

        response = self.get_response(request)

#security
        response["X-Frame-Options"] = "DENY"
        response["X-XSS-Protection"] = "1; mode=block"
        response["X-Content-Type-Options"] = "nosniff"

        return response

    def get_client_ip(self, request):
        """ Retrieve client IP address """
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")


class PerformanceMonitoringMiddleware:
    """ Middleware to track request processing time and log slow requests. """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        
        response = self.get_response(request)
        
        end_time = time.time()
        processing_time = (end_time - start_time) * 1000 

        if processing_time > 500:  
            logger.warning(f" Slow Request: {request.path} took {processing_time:.2f}ms")

        return response
