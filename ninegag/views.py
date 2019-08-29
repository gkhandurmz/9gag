from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import auth
from post.models import Post
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm
from django.utils import timezone


def home(request):
    pro = Post.objects
    return render(request, 'home.html', {'post': pro})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            messages.success(request, 'You Have Registered...')
            return redirect('home')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':

        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid Username or Password'})

    else:
        return render(request, 'login.html')


def logout_user(request):
    auth.logout(request)
    return redirect('home')


def SpecificPost(request, postslug):
    i = Post.objects.get(slug=postslug)
    context = {'postall': i}
    return render(request, 'spost.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'You Have Edited Your Profile...')
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            auth.update_session_auth_hash(request, form.user)
            messages.success(request, 'You Have Edited Your Password...')
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}
    return render(request, 'change_password.html', context)


def create(request):
    if request.method == 'POST':
        if request.POST["title"] and request.POST['URL'] and request.POST['summary'] and request.POST['body'] and\
           request.FILES['image']:
            post = Post()
            post.title = request.POST["title"]
            if request.POST['URL'].startswith('http://') or request.POST['URL'].startswith('https://'):
                post.URL = request.POST['URL']
            else:
                post.URL = 'http://'+request.POST['URL']
            post.summary = request.POST['summary']
            post.body = request.POST['body']
            post.image = request.FILES['image']
            post.pub_date = timezone.datetime.now()
            post.total_votes = 0
            post.SentBy = request.user
            post.save()
            return redirect('home')
        else:
            return render(request, 'create.html', {'error': 'You need to fill all areas!'})
    else:
        return render(request, 'create.html',)

