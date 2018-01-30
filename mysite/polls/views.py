
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import Question,Choice,CommentForm,Comment
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.core.paginator import Paginator
from django.template.context_processors import csrf
import redis



# Create your views here.
def index(request,page_number = 1):
    question_list = Question.objects.all()
    current_list = Paginator(question_list,4)
    args = {}
    args.update(csrf(request))
    args['latest_question_list'] = current_list.page(page_number)
    args['username'] = auth.get_user(request).username
    return render(request,'polls/index.html',args)


def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
        comment = Comment.objects.filter(comment_question_id=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not excist')
    return render(request,'polls/detail.html',{'question':question,'form':CommentForm,'comments':comment})

def result(request, question_id):
    question = get_object_or_404(Question,pk = question_id)
    return render(request,'polls/result.html',{'question':question})



def votes(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{'question': question,'error_message':'You didnt select a choise'})
    else:
        if "test" not in request.session:
            selected_choice.votes += 1
            selected_choice.save()
        return HttpResponseRedirect('/polls/'+str(question_id)+'/results/')

def add_comment(request,question_id):
    session = redis.StrictRedis(host='localhost',port=6379,db=0)
    if session.get('auth'):
        if request.POST:
            new_form = CommentForm(request.POST)
            if new_form.is_valid():
                comment = new_form.save()
                comment.comment_question = Question.objects.get(id = question_id)
                new_form.save()
            return detail(request,question_id)
    return detail(request,question_id)

def del_comment(request,comment_id):
    session = redis.StrictRedis(host='localhost',port=6379,db=0)
    if session.get('auth'):
        if request.POST:
            comment = Comment.objects.get(pk = comment_id)
            comment.delete()
    return HttpResponseRedirect('/')

def add_like(request, comment_id):
    if request.POST:
        comment = Comment.objects.get(pk = comment_id)
        comment.comment_likes += 1
        comment.save()
    return HttpResponseRedirect('/')

