import re
from django.conf import settings
 
RE_MULTISPACE = re.compile(r"\s{2,}\n")
 
class MinifyHTMLMiddleware(object):
    def process_response(self, request, response):
        if 'text/html' in response['Content-Type'] and settings.COMPRESS_HTML:
            response.content = RE_MULTISPACE.sub(" ", response.content)
        return response
