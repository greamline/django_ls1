from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib import auth
from django.http import Http404

from authapp.forms import UserCreateForm, ProfileForm
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        print('=== REQUEST POST DATA :', request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(email=email, password=password)
        data = {
            'page': 'index',
            'login_error': True,
        }
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'index.html', data)
    else:
        raise Http404


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return HttpResponseRedirect('/')
    else:
        raise Http404


def profile(request):
        user = request.user

        if user.is_authenticated:
            if request.method == 'POST':
                # user.email = request.POST.get('email')
                # user.first_name = request.POST.get('first_name')
                # user.last_name = request.POST.get('last_name')
                # user.save()
                form = ProfileForm(request.POST, request.FILES, instance=request.user)
                if form.is_valid():
                    print('REQUEST=',request.POST,request.FILES)
                    form.save()
                else:
                    print('form is not valid.')
                data = {
                    'page': 'profile',
                    'form': form,
                }

                return render(request, 'profile.html', data)
            else:
                form = ProfileForm(
                    initial={'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name,
                             'birth_date': user.birth_date, 'avatar': user.avatar, 'bio':user.bio})
                data = {
                    'page': 'profile',
                    'form': form,
                }
                return render(request, 'profile.html', data)
        else:
            return redirect('/')



def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            auth.login(request, user)
            return redirect('/')
    else:
        form = UserCreateForm()
    return render(request, 'signup.html', {'form': form})
