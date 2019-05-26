from django.shortcuts import render,redirect,get_object_or_404
from main_site.models import Question,Project,Group
import json
from .burn_side import BurnSide
def burn_side(request):
    if request.GET.get('n') and request.GET.get('k'):
        try:
            agent = BurnSide(int(request.GET.get('n')),float(request.GET.get('k')))
        except ValueError:
            return render(request,'main_site/burn_side.html')
        else:
            return render(request,'main_site/burn_side.html',{
                'res' : agent.solve()
            })
    else:
        return render(request,'main_site/burn_side.html')
def submit_questions(request):
    if request.method == "POST":
        if request.POST['name'] and request.POST['title'] and request.POST['content']:
            new_question = Question()
            new_question.asker = request.POST['name']
            new_question.title = request.POST['title']
            new_question.content = request.POST['content']
            new_question.cat = request.POST['cat']
            if request.POST['cat'] is "一般":
                new_question.order = get_object_or_404(Group,name=request.POST['cat']).order
            else:
                new_question.order = -1
            new_question.submit()
            return redirect('view_questions')
        else:
            return redirect('view_questions')
    else:
        groups = Group.objects.all().order_by('order')
        return render(request,"main_site/submit_question.html",{"groups":groups})

def view_questions(request):
    question_list = Question.objects.all().order_by("order")
    return render(request,"main_site/view_question.html",{"questions":question_list})

def view_paper(request):
    return render(request,"main_site/view_paper.html")

def view_project(request):
    projects = Project.objects.all().order_by("group__order")
    return render(request,"main_site/projects.html",{"projects":projects})

# view the questions to be response
def super_view_questions(request):
    question_list = Question.objects.all().order_by('order')
    return render(request,"main_site/super_view_question.html",{"questions":question_list})

def response_questions(request,id):
    question = get_object_or_404(Question,id=id)
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
    text_slide = open("slides.md", "r",encoding='utf-8').read()
    return render(request,"main_site/view_slides.html",{'slides':text_slide})

def index(request):
    return render(request,'main_site/index.html',)

def generate_slide(request):
    questions = Question.objects.exclude(response=None).order_by('order')
    
    f = open("slides.md", "w",encoding='utf-8')
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
