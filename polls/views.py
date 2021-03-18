from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse

from .models import Question,Choice
# Create your views here.

def index(request):
	latest_questions_list = Question.objects.order_by('-publish_date')
	context = {
		'latest_questions_list' : latest_questions_list
	}
	return render(request,'polls/index.html',context)

def detail(request,question_id):
	try:
		question = Question.objects.get(id=question_id)
		context ={
			'question' : question
		}
	except:
		raise Http404('Question does not exist!!')
	
	return render(request,'polls/detail.html',context)

def result(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	context = {
	'question' : question
	}
	return render(request,'polls/result.html',context)

def vote(request,question_id):
	question = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		context={
			'question':question,
			'error_message':"You didn't select anything!",

		}
		return render(request, "polls/detail.html",context)

	else:
		selected_choice.votes +=1
		selected_choice.save()
		total_votes = 0
		for choice in question.choice_set.all():
			total_votes+=choice.votes
		for choice in question.choice_set.all():
			if(choice.votes):
				choice.percent = round(choice.votes/total_votes*100,2)
				choice.save()
		return HttpResponseRedirect(reverse('polls:result',args=(question_id,)))

def sayHello(request):
	return HttpResponse("Hello from user also!")