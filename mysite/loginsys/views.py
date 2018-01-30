

# Create your
#
#  views here.
from django.contrib import auth
from django.contrib.auth import authenticate
from django.template.context_processors import csrf
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from .models import My_user_form,Link_with_email
import redis
from mysite import settings





def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password )
        if user is not None:
            auth.login(request,user)
            redis_session = redis.StrictRedis(host='localhost',port=6379,db=0,password=None)
            redis_session.set('auth',True)
            redis_session.save()
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            args['login_error'] = "This user dont excist"
            return render_to_response('loginsys/login.html',args)
    else:
            return render_to_response('loginsys/login.html',args)



def logout(request):
    redis_session = redis.StrictRedis(host='localhost',port=6379,db=0,password=None)
    redis_session.delete('auth')
    auth.logout(request)
    return HttpResponseRedirect(reverse('polls:index'))

def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            
            new_user_form.save()
            new_user = auth.authenticate(username = new_user_form.cleaned_data['username'], password = new_user_form.cleaned_data['password1'])
            auth.login(request,new_user)
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            args['form'] = new_user_form
    return render(request,"loginsys/register.html",args)

def cabinet(request):
    args = {}
    args.update(csrf(request))
    id = request.user.id
    if request.user.is_authenticated():
        args['username'] = request.user.username
        args['email'] = request.user.email
        args['telegram_bot'] = 'https://telegram.me/ZlainBlya_bot?start='+str(id)
    else:
        args['username'] = 'None'
        args['email'] = 'None'
    return render(request,"loginsys/cabinet.html",args)

def get_email(request):
    username = request.user.username
    password = request.POST['password']
    email = request.POST['email']
    user = authenticate(username=username,password=password)
    if user is not None :
        user.email = email
        user.save()
    return HttpResponseRedirect(reverse('polls:index'))

def link_with_account(request):
    if request.POST:
        chat_id = request.POST['chat_id']
        email = request.user.email
        get_notice = request.POST['get_notice']
        new_link = Link_with_email.objects.create(email = email,chat_id = chat_id,get_notice = get_notice)
    return HttpResponseRedirect(reverse('polls:index'))

def get_links(request):
    args = {}
    args.update(csrf(request))
    links = Link_with_email.objects.all()
    args['links'] = links
    return render(request,"loginsys/links.html",args)
