from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserProfile, BlogPost, Comment, Product, Store, Question, Choice, ContactMessage
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from .serializers import CommentsListSerializer
from .serializers import ProductsListSerializer

from django.db.models import Q
import django_filters

class ProductsListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer

    @action(methods=['GET'], detail=False, url_path='product')
    def get_queryset(self, products):
        products = Product.objects.filter(Q(product__exact=2))
        data = ProductSerializer(instance=products, many=True).data
        return Response(data)

class CommentsFilter(django_filters.FilterSet):
    queryset = Comment.objects.all()
    class Meta:
        model = Comment
        fields = ['post', 'author', 'content', 'created_at']

class CommentsListView(generics.ListAPIView):
    model = Comment
    serializer_class = CommentsListSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = CommentsFilter

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Comment.objects.filter(author=user).order_by('-created_at')
        else:
            return Comment.objects.none()

class ProductsListAllView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer

    @action(detail=False, methods=['GET'])
    def all(self, request):
        queryset = self.queryset
        serialized_data = self.get_serializer(queryset, many=True).data
        return Response(serialized_data)

def loginpage(request):
    page = 'login'
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login_register.html', {'form': form, 'page': page})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
        messages.error(request, f'Неправильный логин или пароль')
        return render(request, 'login_register.html', {'form': form, 'page': page})

def logoutuser(request):
    logout(request)
    return redirect('home')

def registerpage(request):
    page = 'register'
    context = {'page': page}
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'login_register.html', {'form': form, "page": page})
    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login_register.html', context)
        

def home(request):
    polls = Question.objects.all()
    context = {'polls': polls}
    return render(request, 'home.html', context)

def profile(request):
    return render(request, 'profile.html')

def feed(request):
    posts = BlogPost.objects.all()
    context = {'posts': posts}
    return render(request, 'feed.html', context)

def post(request, pk):
    post = BlogPost.objects.get(id=pk)
    comments = post.comment_set.all()
    context = {'post': post, 'comments': comments}
    return render(request, 'post.html', context)

def poll(request, pk):
    poll = Question.objects.get(id=pk)
    context = {'poll': poll}
    return render(request, 'home.html', context)

def goods(request):
    return render(request, 'goods.html')

def feedback(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'feedback.html', context)

def addpost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('feed')
    context = {'form': form}
    return render(request, 'addpost.html', context)

def updatepost(request, pk):
    post = BlogPost.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            return redirect('feed')
    context = {'form': form}
    return render(request, 'addpost.html', context)

def deletepost(request, pk):
    post = BlogPost.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('feed')
    return render(request, 'delete.html', {'obj':post})

def goods(request):   
    stores = Store.objects.prefetch_related('sleep_products').all()
    return render(request, 'goods.html', {'stores': stores})

def comments(request):   
    comments = Comment.objects.prefetch_related('post').all()
    return render(request, 'goods.html', {'comments': comments})