from django.shortcuts import render, redirect
from .models import Project, Structure
from .forms import AppealForm
import smtplib
from email.message import EmailMessage

# Create your views here.
def home(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {'projects':projects})

def structure(request):
    persons = Structure.objects.all()
    return render(request, "structure.html", {'persons':persons})

def project_detail_view(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, "detail_project.html", {'project':project})


def contact(request):
    form = AppealForm(request.POST)
    if form.is_valid():
        form.save()
        data = form.data
        print(data)
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("aiinar.beauty@gmail.com", "qcdthurungnodery")
        
        
        msg = "Поступило анонимное обращение. Текст:" + data['text'] + "."
        from_ = 'aiinar.beauty@gmail.com'
        to_ = 'nurik.bro.2000@gmail.com'
        subject = 'Новое анонимное обращение'   
        em = EmailMessage()
        em.set_content(msg)
        em['To'] = to_
        em['From'] = from_
        em['Subject'] = subject
        
        server.send_message(em)
        
        return redirect('contact')
    return render(request, 'contact.html', {'form': form})