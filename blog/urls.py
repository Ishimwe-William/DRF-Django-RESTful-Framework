from django.urls import path
from django.views.generic import TemplateView

app_name = 'blog'

urlpatterns = [
    # display the template page that is /templates/blog/index.html
    path('', TemplateView.as_view(template_name="blog/index.html")),
]