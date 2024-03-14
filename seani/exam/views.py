from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .forms import CandidateForm
from .models import Exam

def home (request):
    user = request.user
    return render(request, 'exam/home.html', {'user': user})

# Create your views here.

def question(request, m_id, q_id = 1):
    exam = request.user.exam
    questions= exam.breakdown_set.filter(question_module_id = m_id)
    question = questions[q_id -1].question
    return render(request, 'exam/question.html',{"question": question})
def add_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            stage = form.cleaned_data['stage']
            career = form.cleaned_data['career']
            username = form.cleaned_data['username']


            # crear usuario
            user = User.objects.create_user(username, email, password)
            # editar usuario
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # crear examen 
            exam = Exam.objects.crate(user=user, stage=stage, career=career)
            #llenar examen 
            exam.set_modules()
            exam.set_questions()
            html = """
            <h1>Usuario y examen creado</h1>
            <a href="/exam/add">Agregar otro</a>
            """
          
            return HttpResponse('html')

    form = CandidateForm()
    return render(request,'exam/add_candidate.html', {"form": form})