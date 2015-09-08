"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name' : 'Irma Leticia Kramer',
    'bio' : 'Pythonista. PyLadies ATX Organizer! PyMoms Organizer! ',
    'email' : '', # Leave blank if you'd prefer not to share your email with other conference attendees
    'twitter_username' : 'bluflowr', # No @ symbol, just the handle.
    'github_username' : "bluflowr", 
    'headshot_url' : 'https://media.licdn.com/mpr/mpr/shrinknp_400_400/p/4/005/0ad/090/0fd9587.jpg', # Link to your GitHub, Twitter, or Gravatar profile image.
}
    
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,    
                'year': datetime.now().year,
            })
    )