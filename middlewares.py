# -*- coding: utf-8 -*-
from usetracker import models
import urlparse
import re
from django.utils import timezone

class UseTrackerMiddleware(object):
    def process_request(self, request):
        regex_http          = re.compile(r'^HTTP_.+$')
        regex_content_type   = re.compile(r'^CONTENT_TYPE$')
        regex_content_length = re.compile(r'^CONTENT_LENGTH$')

        headers = {}
        for header in request.META:
            if regex_http.match(header) or regex_content_type.match(header) or regex_content_length.match(header):
                headers[header] = request.META[header]
        splituri = urlparse.urlparse(request.build_absolute_uri())
        ut = models.UseTracker(protocol = splituri.scheme,
                               host = splituri.netloc,
                               path = splituri.path,
                               get_params = splituri.query,
                               headers = unicode(headers),
                               post_payload = unicode(dict(request.POST)),
                               username = request.user.username)
        ut.save()
        request.session['ut_id'] = ut.id

    def process_response(self, request, response):
        ut = models.UseTracker.objects.get(id = request.session.get('ut_id'))
        ut.finished_at = timezone.now()
        ut.save()
        return response

    def process_exception(self, request, exception):
        ut = models.UseTracker.objects.get(id = request.session.get('ut_id'))
        ut.finished_at = timezone.now()
        ut.exception = unicode(exception)
        ut.save()
        
