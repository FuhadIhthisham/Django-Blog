from django.urls import path
from . import views
from . views import (PostListView,
                     PostCreateView,
                     PostUpdateView,
                     PostDeleteView,
                     UserPostListView,)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='blog-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('about/', views.about, name='blog-about')
]