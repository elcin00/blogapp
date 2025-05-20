from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog, Category

# Create your views here.

data = {
    "blogs":[
        {
            "id": 1,
            "title": "Complete web developing",
            "image": "1.jpg",
            "is_active": True,
            "is_home": False,
            "description": "A very good course"
        },
        {
            "id": 2,
            "title": "Python course",
            "image": "2.jpg",
            "is_active": True,
            "is_home": True,
            "description": "A very good course"
        },
        {
            "id": 3,
            "title": "Django course",
            "image": "3.jpg",
            "is_active": False,
            "is_home": True,
            "description": "A very good course"
        }
    ]
}

def index(request):
    context = {
        # "blogs": data["blogs"]
        "blogs": Blog.objects.filter(is_active=True, is_home=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        # "blogs": data["blogs"]
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, slug):
    # blogs = data["blogs"]
    # selectedBlog = None
    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBlog = blog

    # blogs = data["blogs"]
    # selectedBlog = [blog for blog in blogs if blog["id"] == id][0]

    blog = Blog.objects.get(slug=slug)

    return render(request, "blog/blog_details.html", {
        "blog": blog
    })

def blogs_by_category(request, slug):
    context = {
        "blogs": Blog.objects.filter(is_active=True, category__slug=slug),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)