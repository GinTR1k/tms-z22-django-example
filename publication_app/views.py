from django.shortcuts import render

from .models import Post


def main_page(request):
    posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all()

    contex = {'title': 'ПРИВЕТ МИР', 'posts': posts}
    return render(request, 'main_page.html', contex)
