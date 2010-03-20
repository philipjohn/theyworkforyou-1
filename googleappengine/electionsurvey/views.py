#
# views.py:
# Views for TheyWorkForYou election quiz Django project
#
# Copyright (c) 2010 UK Citizens Online Democracy. All rights reserved.
# Email: francis@mysociety.org; WWW: http://www.mysociety.org/
#

from google.appengine.api import urlfetch
from django.shortcuts import render_to_response, get_object_or_404#

def index(request):
    return render_to_response('index.html', {})


