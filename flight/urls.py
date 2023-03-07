from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    # path('', TemplateView.as_view(template_name="index.html")),    
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("ticket.urls")),
]