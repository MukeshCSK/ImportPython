from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


DIFFICULTY = (
    (0,"Easy"),
    (1,"Medium"),
    (2,"Hard")
)

class Post(models.Model):
    post_title = models.CharField('post_title',max_length=200, unique=True,null=True)
    slug = models.SlugField('post_slug',max_length=200, unique=True,null=True)
    post_pic = models.ImageField('post_pic',upload_to='chicks/',default='False',null=True)
    post_updated_on = models.DateTimeField('post_updated_on',auto_now= True)
    post_summary = models.CharField('post_summary',max_length=120, unique=True,null=True)
    post_content = RichTextField('post_content',null=True)
    post_created_on = models.DateTimeField('post_created_on',auto_now_add=True,null=True)
    post_difficulty = models.IntegerField('post_difficulty',choices=DIFFICULTY, default=0,null=True)

    class Meta:
        ordering = ['-post_created_on']

    def __str__(self):
        return self.post_title

class Blog(models.Model):
    blog_title = models.CharField('blog_title',max_length=200, unique=True,null=True)
    slug = models.SlugField('blog_slug',max_length=200, unique=True,null=True)
    blog_pic = models.ImageField('blog_pic',upload_to='chicks/',default='False',null=True)
    blog_updated_on = models.DateTimeField('blog_updated_on',auto_now= True,null=True)
    blog_summary = models.CharField('blog_summary',max_length=120, unique=True,null=True)
    blog_content = RichTextField('blog_content',null=True)   
    blog_created_on = models.DateTimeField('blog_created_on',auto_now_add=True,null=True)

    class Meta:
        ordering = ['-blog_created_on']

    def __str__(self):
        return self.blog_title


TYPE = (
    (0,"Coding"),
    (1,"Mini-Project"),
    (2,"Project")
)


class Project(models.Model):
    project_title = models.CharField('project_title',max_length=200, unique=True,null=True)
    slug = models.SlugField('project_slug',max_length=200, unique=True,null=True)
    project_pic = models.ImageField('project_pic',upload_to='chicks/',default='False',null=True)
    project_updated_on = models.DateTimeField('project_updated_on',auto_now= True,null=True)
    project_summary = models.CharField('project_summary',max_length=120, unique=True,null=True)
    project_content = RichTextField('project_content',null=True)   
    project_created_on = models.DateTimeField('project_created_on',auto_now_add=True,null=True)
    project_type = models.IntegerField('project_type',choices=TYPE, default=0,null=True)

    class Meta:
        ordering = ['-project_created_on']

    def __str__(self):
        return self.project_title
