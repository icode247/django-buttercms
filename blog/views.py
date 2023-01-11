from butter_cms import ButterCMS
from django.shortcuts import render
from django.http import Http404
import os
client = ButterCMS("ff0d0ebeeea392595b63eee76abdc2424e788e16")

def Index(request, page = 1):
    response = client.posts.all({'page_size': 10, 'page': page})

    try:
        recent_posts = response['data']
        print(recent_posts)
    except:
        # In the event we request an invalid page number, no data key will exist in response.
        raise Http404('Page not found')

    next_page = response['meta']['next_page']
    previous_page = response['meta']['previous_page']

    return render(request, 'index.html', {
        'recent_posts': recent_posts,
        'next_page': next_page,
        'previous_page': previous_page
    })


def Blog(request, slug):
    try:
        response = client.posts.get(slug)
    except:
        raise Http404('Post not found')

    post = response['data']
    return render(request, 'blog.html', {
        'post': post
    })
