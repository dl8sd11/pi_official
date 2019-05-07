from django.shortcuts import render,redirect
from main_site.models import Question
def submit_questions(request):
    if request.method == "POST":
        if request.POST['name'] and request.POST['title'] and request.POST['content']:
            new_question = Question()
            new_question.asker = request.POST['name']
            new_question.title = request.POST['title']
            new_question.content = request.POST['content']
            new_question.cat = request.POST['cat']
            new_question.submit()
            return redirect('view_questions')
        else:
            return render(request,"main_site/submit_question.html")
    else:
        return render(request,"main_site/submit_question.html")

def view_questions(request):
    question_list = Question.objects.all()
    return render(request,"main_site/view_question.html",{"questions":question_list})

def view_paper(request):
    return render(request,"main_site/view_paper.html")

def super_view_questions(request):
    question_list = Question.objects.all()
    return render(request,"main_site/super_view_question.html",{"questions":question_list})

def response_questions(request,id):
    question = Question.objects.get(id=id)
    if request.method == "POST":
        question.seen = True
        question.response = request.POST['response']
        question.save()
        return redirect('super_view_questions')
    else:
        return render(request,"main_site/response_question.html",{"question":question})

def view_agenda(request):
    return render(request,"main_site/agenda.html")

def index(request):
    return render(request,'main_site/index.html',)

def generate_slide(request):
    questions = Question.objects.exclude(response=None)
    print(questions)
    f = open("slides.md", "a")
    first = True
    for question in questions:
        if not first:
            f.write("---\n\n")
        first = False
        f.write("## {}\n".format(question.title))
        f.write("{} - by {}\n\n".format(question.content,question.asker))
        if question.response != 'EMPTY':
            f.write("---\n\n")
            f.write("{}\n\n".format(question.response))
    f.close()
    return redirect('index')