from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from blog.models import Post 
from django.core.context_processors import csrf
from django.template import RequestContext

def main(request):
    """Main listing."""
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts, 10)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("list.html", dict(posts=posts, user=request.user))

def post_page(request, post_url):
    post = Post.objects.get(post_url=post_url)
    d = dict(post=post, user=request.user)
    d.update(csrf(request))
    return render_to_response("post.html", d)

def archive(request):
    posts = Post.objects.all().order_by("-created")
    return render_to_response("archive.html", dict(posts=posts, user=request.user))

def tag(request, tag):
    posts = Post.objects.filter(tags__name=tag).order_by("-created")
    return render_to_response("tag.html", dict(posts=posts, tag=tag, user=request.user))
