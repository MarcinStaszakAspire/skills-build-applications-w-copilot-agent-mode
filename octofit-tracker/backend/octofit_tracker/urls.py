"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse


# Helper to get codespace name from environment
def get_codespace_url():
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    return f"https://{codespace_name}-8000.app.github.dev"

def api_response(request, component):
    url = get_codespace_url()
    return JsonResponse({
        "endpoint": f"{url}/api/{component}/"
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/activities/', lambda request: api_response(request, 'activities')),
    path('api/teams/', lambda request: api_response(request, 'teams')),
    path('api/users/', lambda request: api_response(request, 'users')),
    path('api/leaderboard/', lambda request: api_response(request, 'leaderboard')),
    path('api/workouts/', lambda request: api_response(request, 'workouts')),
]
