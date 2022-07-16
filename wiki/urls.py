from django.contrib import admin
from django.urls import path,include
from .views import PostDetailView,PostListView,PostCreateView,PostUpdateView

urlpatterns = [
    path('<slug:slug>/',PostDetailView.as_view(), name='post-detail'),
    path('',PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
        
]