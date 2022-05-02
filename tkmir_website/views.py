from asyncio.windows_events import NULL
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, PostsCreationForm
from .models import PostsCreation
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import Profile
from django.contrib.auth import logout
from django.shortcuts import redirect


def index(request):
    return render(request, 'tkmir_website/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db() 
            user.profile.name = form.cleaned_data.get('first_name')
            user.profile.name = user.profile.name +' '+ form.cleaned_data.get('last_name')
            user.profile.roll_no = form.cleaned_data.get('roll_no')
            user.profile.mobile = form.cleaned_data.get('mobile')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.institution = form.cleaned_data.get('institution')
            user.profile.department = form.cleaned_data.get('department')
            user.profile.role = form.cleaned_data.get('role')
            user.save()
            ######################### mail system ####################################
            # htmly = get_template('tkmir_website/email.html')
            # d = { 'username': user.username }
            # subject, from_email, to = 'welcome', 'your_email@gmail.com', user.email
            # html_content = htmly.render(d)
            # msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            # ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('log-reg')
        else:
            messages.warning(request, f'Invalid Credentials')
    else:
        form = UserRegisterForm()
    return render(request, 'tkmir_website/registration.html', {'form': form, 'title':'reqister here'})
  

def log_reg(request):
    if request.user.is_authenticated:
        return redirect('logout')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('posts')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    
    return render(request, 'tkmir_website/login_register.html', {'form':form, 'title':'log in'})
@login_required(login_url='log-reg')
def profile(request):
    name = request.user.profile.name 
    roll_no = request.user.profile.roll_no
    mobile = request.user.profile.mobile
    college = request.user.profile.college
    department = request.user.profile.department
    print(name)
    return render(request, 'tkmir_website/profile.html', {'name':name, 'roll_no':roll_no, 'mobile':mobile, 'college':college, 'department':department})
@login_required(login_url='log-reg')
def posts(request):
    posts = PostsCreation.objects.all()
    return render(request, 'tkmir_website/posts.html',{'posts':posts})
@login_required(login_url='log-reg')
def posts_creation(request):
    if request.method == 'POST':
        form = PostsCreationForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.title = form.cleaned_data.get('title')
            f.content = form.cleaned_data.get('content')
            f.author = request.user
            f.save()
            messages.success(request, f'You have succefully made a post!')
            return redirect('posts')
    else:
        form = PostsCreationForm()
    return render(request, 'tkmir_website/posts_creation.html',{'form': form})


@login_required(login_url='log-reg')
def logout_view(request):
    logout(request)
    messages.warning(request, f'You have succefully logged out!')
    return redirect('home')