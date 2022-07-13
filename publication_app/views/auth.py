from django.contrib import auth
from django.shortcuts import redirect, render
from django.views import View

from publication_app.forms.auth import AuthForm
from publication_app.tasks import very_long_task


class AuthView(View):
    @staticmethod
    def get(request):
        form = AuthForm()
        context = {
            'auth_form': form,
        }
        return render(request, 'auth_page.html', context)

    @staticmethod
    def post(request):
        # very_long_task.delay()

        form = AuthForm(request.POST)
        error = False

        if form.is_valid():
            user = auth.authenticate(request, **form.cleaned_data)

            if user is not None:
                auth.login(request, user)

                next_page = request.GET.get('next', '/')
                return redirect(next_page)

            error = True

        context = {
            'auth_form': form,
            'error': error,
        }

        return render(request, 'auth_page.html', context)
