from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
import logging




def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    # logger = logging.getLogger('django')
    #logger.info('here goes your message')
    #posts = Post.objects.all()
    # logger.info(posts[0].author)
    return render(request, 'blog/post_list.html', {'posts': posts, 'time': timezone.now()})

def post_detail (request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})