from django.shortcuts import render

from django.views import generic
from .models import Post

# status = 1 - only view the posted posts, ton draft
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

# from django.http import HttpResponse
# def page13(request):
#     # template_name = '13.html'
#     return HttpResponse ('this is page 13')

# from django.http import HttpResponse
def page13(request):
    return render (request, '13.html')

def about_me(request):
    return render (request, 'about_me.html')

def terms(request):
    return render (request, 'terms_of_use.html')