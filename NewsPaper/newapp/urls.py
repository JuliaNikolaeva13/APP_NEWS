from django.urls import path
from .views import *

urlpatterns = [
    path('authorlist', AuthorList.as_view()),
    path('postlist', PostList.as_view()),
    path('postdetail', PostDetail.as_view()),
]