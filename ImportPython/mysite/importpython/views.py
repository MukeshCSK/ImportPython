from django.shortcuts import render, get_object_or_404
from .models import Post,Blog,Project

def home(request):
    posts = Post.objects.all().order_by('-post_created_on')
    blogs = Blog.objects.all().order_by('-blog_created_on')
    projects = Project.objects.all().order_by('-project_created_on')
    return render(request, 'index.html', {'post_list': posts,'blog_list':blogs,'project_list':projects})


def post_list(request):
    posts = Post.objects.all().order_by('-post_created_on')
    return render(request, 'post_list.html', {'post_list': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    blogs = Blog.objects.all().order_by('-blog_created_on')
    projects = Project.objects.all().order_by('-project_created_on')
    return render(request, 'post_detail.html', {'post': post,'blog':blogs,'project':projects})

def blog_list(request):
    blogs = Blog.objects.all().order_by('-blog_created_on')
    return render(request, 'blog_list.html', {'blog_list': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog})

def project_list(request):
    projects = Project.objects.all().order_by('-project_created_on')
    return render(request, 'project_list.html', {'project_list': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')







'''
from django.views import generic
from .models import Post
from .models import Blog
from .models import Project

class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('-post_created_on')
    template_name = 'index.html'
    context_object_name = 'post_list'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogList(generic.ListView):
    queryset = Blog.objects.all().order_by('-blog_created_on')
    template_name = 'index.html'
    context_object_name = 'blog_list'

class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'blog_detail.html'

class ProjectList(generic.ListView):
    queryset = Project.objects.all().order_by('-project_created_on')
    template_name = 'index.html'
    context_object_name = 'project_list'

class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'project_detail.html'
'''


'''

from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-post_created_on')
    return render(request, 'index.html', {'post_list': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})

'''

