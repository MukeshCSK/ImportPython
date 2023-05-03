from django.contrib import admin
from .models import Post
from .models import Blog
from .models import Project

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'slug', 'post_pic','post_created_on','post_summary',)
    search_fields = ['post_title', 'post_content']
    prepopulated_fields = {'slug': ('post_title',)}

admin.site.register(Post, PostAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'slug', 'blog_pic','blog_created_on','blog_summary',)
    search_fields = ['blog_title', 'blog_content']
    prepopulated_fields = {'slug': ('blog_title',)}

admin.site.register(Blog, BlogAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'slug', 'project_pic','project_created_on','project_summary',)
    search_fields = ['project_title', 'project_content']
    prepopulated_fields = {'slug': ('project_title',)}

admin.site.register(Project, ProjectAdmin)