from django.conf.global_settings import LOGIN_URL
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from mymen.forms import RahitRegistrationForm, RahitLoginForm


def join(request):
    registration_template = 'mymen/join.html'
    registration_success_redirect = LOGIN_URL
    args = {}
    args.update(csrf(request))
    form = RahitRegistrationForm
    if request.method == 'POST':
        form = RahitRegistrationForm(request.POST);
        if form.is_valid():
           form.save()
           messages.add_message(request, messages.SUCCESS, "Registration completed successfully!!")
           return HttpResponseRedirect(LOGIN_URL)
        else:
            messages.add_message(request, messages.ERROR, "Error Occurred!!")

    args['form'] = form
    return render_to_response(registration_template, args, context_instance=RequestContext(request))


def login(request):
    args = {}
    args.update(csrf(request))
    form = RahitLoginForm()
    if request.method == 'POST':
        form = RahitLoginForm(request.POST);
        username = request.POST['username']
        password = request.POST['password']

        """
        check for email also and
        enable user to login using email or username

        """
        try:
            user = User.objects.get(email=username)
            username = user.username
            request.POST['username'] = username
        except Exception:
            username = username

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                messages.add_message(request, messages.SUCCESS, "Successfully logged in!!")
                return HttpResponseRedirect('/')
            else:
                messages.add_message(request, messages.ERROR, "Please activate your account first!!")
        else:
            messages.add_message(request, messages.ERROR, "Invalid username or password")
    args['form'] = form
    return render_to_response('mymen/login.html', args, context_instance=RequestContext(request))

