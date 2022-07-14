from django.contrib import admin
from django.urls import path,include
from .views import home,ArticleDetailView,ProductListView,FoodDetailView,FoodListView

urlpatterns = [
    path('',home.as_view(),name='home'),
    path('article/<slug:slug>/',ArticleDetailView.as_view(), name='article-detail'),
    path('products/',ProductListView.as_view(), name='product-list'),
    path("food", FoodListView.as_view(), name="food-list"),
    path("food/<slug:slug>", FoodDetailView.as_view(), name="food-detail"),  # new

    # path('artical/<int:pk>/', ArticalDetailView.as_view(), name='artical-detail'),
    # path('food/',FoodListView.as_view(),name='food-list'),
    # path('meal/',MealListView.as_view(),name='meal-list'),
    # path('food/create/',FoodCreateView.as_view(),name='food-create'),
    # path('<slug:slug>/', FoodDetailView.as_view(), name='food-detail'),
    # path('<slug:slug>/update', FoodUpdateView.as_view(),name='food-update'), 
    # path('<slug:slug>/delete/', FoodDeleteView.as_view()),
    # path('meal/<int:pk>/delete/', MealDeleteView.as_view()),
    # path('meal/create/',MealCreateView.as_view(),name='meal-create'),
    # # path('<int:pk>/',MealDetailView.as_view(),name='meal-detail'),
    # path('meal/<int:pk>/', MealDetailView.as_view(), name='meal-detail'),
    # path('meal/<int:pk>/update', MealUpdateView.as_view(),name='meal-update'), 
    # path('meal/test/', testView.as_view(),name='meal-test'), 



    # path('<slug:slug>/', FoodDetailView.as_view(), name='food-detail'),
    # path('<slug:slug>/update', FoodUpdateView.as_view(),name='food-update'), 
    # path('<slug:slug>/delete/', FoodDeleteView.as_view()),

    
    
]