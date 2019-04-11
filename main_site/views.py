from django.shortcuts import render
from main_site.models import Question
def view_questions(request):
    question_list = Question.objects.all()
    return render(request,"main_site/question_answer.html",{"questions":question_list})

def submit_questions(request):
    if request.method == "POST":
        if request.POST['name'] and request.POST['title'] and request.POST['content']:
            new_question = Question()
            new_question.asker = request.POST['name']
            new_question.title = request.POST['title']
            new_question.content = request.POST['content']
            new_question.submit()
            return view_questions(request)
        else:
            return render(request,"main_site/submit_question.html")
    else:
        return render(request,"main_site/submit_question.html")

def view_questions(request):
    question_list = Question.objects.all()
    return render(request,"main_site/view_question.html",{"questions":question_list})

def response_questions(request,id):
    question = Question.objects.get(id=id)
    if request.method == "POST":
        question.seen = True
        question.reponse = request.POST['response']
        question.save()
        return view_questions(request)
    else:
        return render(request,"main_site/response_question.html",{"question":question})

def view_agenda(request):
    return render(request,"main_site/agenda.html")

def index(request):
    return render(request,'main_site/index.html',)
