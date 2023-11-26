from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutuser, name="logout"),
    path('register/', views.registerpage, name="register"),
    path('', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('feed/', views.feed, name="feed"),
    path('post/<str:pk>/', views.post, name="post"),
    path('poll/<str:pk>/', views.poll, name='poll'),
    path('goods/', views.goods, name="goods"),
    path('feedback/', views.feedback, name="feedback"),
    path('addpost/', views.addpost, name="addpost"),
    path('updatepost/<str:pk>/', views.updatepost, name="updatepost"),
    path('deletepost/<str:pk>/', views.deletepost, name="deletepost"),
    path('products/api', views.ProductsListView.as_view()),
    path('comments/api', views.CommentsListView.as_view()),
]