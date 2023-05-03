'''
from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('', views.BlogList.as_view(), name='home'),
    path('', views.ProjectList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('<slug:slug>/', views.ProjectDetail.as_view(), name='project_detail'),
]
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/',views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('blog/',views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('project/',views.project_list, name='project_list'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

