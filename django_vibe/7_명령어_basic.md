# 1. URL 설계
```
'/' : 홈 페이지
'/about': 소개 페이지
'/contact': 연락처 페이지
'/blog': 블로그 메인 페이지
'/blog/1': 블로그 1번 글 페이지
'/blog/2': 블로그 2번 글 페이지
'/admin': 관리자 페이지
```

# 2. Model 설계
```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)    
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()    
    posts = models.ManyToManyField(Post, related_name='categories')
```

# 3. 초기 세팅 명령어

## 3.1 windows
```bash
python -m venv venv
venv\Scripts\activate
pip install django
django-admin startproject config .
```

## 3.2 macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install django
django-admin startproject config .
```

## 3.3 공통

```python
# config/settings.py

ALLOWED_HOSTS = ['*']

#################################
# terminal commands

python manage.py migrate
python manage.py runserver
```

# 4. 앱 생성 및 등록

```python
# terminal commands
python manage.py startapp blog

#################################
# config/settings.py
INSTALLED_APPS = [
    ...
    'blog',
]

#################################

# config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

#################################
# blog/urls.py
# 파일이 없으니 생성하셔야 합니다!

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
]

##################################
# blog/views.py
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def blog_list(request):
    return render(request, "blog_list.html")


def blog_detail(request, post_id):
    return render(request, "blog_detail.html", {"post_id": post_id})

#################################
# 없으니 만드셔야 합니다.
# 꾸미진 않겠습니다.
# blog/templates/home.html
# blog/templates/about.html
# blog/templates/contact.html
# blog/templates/blog_list.html
# blog/templates/blog_detail.html

##################################
# terminal commands
python manage.py runserver

#################################
# blog/models.py

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    posts = models.ManyToManyField(Post, related_name='categories')

##################################
# terminal commands
python manage.py makemigrations
python manage.py migrate

##################################
# blog/admin.py

from django.contrib import admin

from .models import Post, Comment, Category
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)

##################################
python manage.py createsuperuser
leehojun
leehojun@gmail.com
dlghwns1234!
dlghwns1234!

##################################
python manage.py runserver

# 게시물 3개 등록

#################################
# blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def blog_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog_list.html", {"posts": posts})


def blog_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog_detail.html", {"post": post})

#################################
# blog/templates/blog_list.html
{% for post in posts %}
    <h2><a href="{% url 'blog_detail' post.id %}">{{ post.title }}</a></h2>
    <p>{{ post.created_at }}</p>
    <hr>
{% endfor %}

# blog/templates/blog_detail.html
<h1>{{ post.title }}</h1>
<p>{{ post.created_at }}</p>
<div>{{ post.content }}</div>
```