from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Categories, Posts, Tags


def post_list(request):
    """
    All Posts View
    """
    post_list = Posts.objects.all()
    paginator = Paginator(post_list , 10)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'post_list.html', {'posts': posts})


def post(request, slug):
    """
    Single Post View
    """
    post = Posts.objects.get(slug=slug)
    return render(request, 'post.html', {
        'post': post
    })


def category(request, slug):
    """
    Category View
    """
    category = Categories.objects.get(slug=slug)
    posts = Posts.objects.all(category__slug=slug)
    return render(request, 'category.html', {
        'category': category,
        'posts': posts
    })


def category_list(request):
    """
    Category View
    """
    categories = Categories.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def tag(request, slug):
    """
    Display all Posts for a Tag
    """
    tag = Tags.objects.get(slug)
    return render(request, 'tag.html', {
        'tag': tag
    })


def tag_list(request):
    """
    All Tag View
    """
    tags = Tags.objects.all()
    return render(request, 'tag_list.html', {'tags': tags})


def get_recent_posts(request):
    """
    Maybe to display on the side
    """
    posts = Posts.object.all()[:10]
    return posts
