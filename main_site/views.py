from django.shortcuts import render,redirect
from main_site.models import Question
import json

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

# view the questions to be response
def super_view_questions(request):
    question_list = Question.objects.all().order_by('cat')
    return render(request,"main_site/super_view_question.html",{"questions":question_list})

def response_questions(request,id):
    question = Question.objects.get(id=id)
    if request.method == "POST":
        # check if the string not empty
        question.reply(request.POST['response'])
        return redirect('super_view_questions')
    else:
        return render(request,"main_site/response_question.html",{"question":question})

def view_agenda(request):
    with open('agenda.json',encoding='utf-8') as f:
        agenda = json.load(f)
    return render(request,"main_site/agenda.html",{'agenda':agenda})

def view_slide(request):
    text_slide = open("slides.md", "r").read()
    return render(request,"main_site/view_slides.html",{'slides':text_slide})

def index(request):
    return render(request,'main_site/index.html',)

def generate_slide(request):
    questions = Question.objects.exclude(response=None).order_by('cat')
    
    f = open("slides.md", "w")
    first = True

    for question in questions:
        # sperate questions with slide page
        if not first:
            f.write("\n---\n\n")
        first = False

        # catagory and question title
        f.write("### {}: {}\n".format(question.cat,question.title))
        # question content
        f.write("{} - by {}\n".format(question.content,question.asker))

        # generate a page for response if the response isn't "EMPTY"
        if question.response != 'EMPTY':
            f.write("\n---\n\n")
            f.write("{}\n".format(question.response))
    f.close()
    return redirect('view_slide')
