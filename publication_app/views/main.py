from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from publication_app.models import Post


class MainPageView(View):
    @staticmethod
    def get(request):
        posts = Post.objects.filter(is_public=True).order_by('-created_at', '-id').all()

        contex = {'title': 'ПРИВЕТ МИР', 'posts': posts}
        return render(request, 'main_page.html', contex)


class PostListView(ListView):
    queryset = Post.objects.order_by('-created_at', '-id')
    template_name = 'main_page.html'
    context_object_name = 'posts'
    http_method_names = ['get']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset

        return self.queryset.filter(is_public=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = 'Посты через ListView'
        return context

    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)
        return result

    def post(self, request, *args, **kwargs):
        pass
