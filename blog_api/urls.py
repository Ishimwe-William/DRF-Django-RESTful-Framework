
# https://www.django-rest-framework.org/api-guide/generic-views/

from django.urls import path
from .views import PostDetails, PostList

app_name='blog_api'

urlpatterns = [
    path('<int:pk>/',PostDetails.as_view(), name='detailCreate'),
    path('',PostList.as_view(),name='listCreate'),
]