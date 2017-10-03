from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from content.models import ShExpJob,ShExpMan

urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset=ShExpJob.objects.all().order_by("date")[:25],
                                    template_name="content/shaexp.html")),
            ]