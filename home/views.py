from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from twisted.conch.ssh.connection import messages
from django.contrib import messages

from course.models import Course, Subject, Tutor
from .models import Setting, ContactForm, ContactMessage
from course.models import Student


# Create your views here.

def index(request):
    setting = Setting.objects.get()
    course = Course.objects.all()
    course_cr = Course.objects.all().order_by('id')[:4]
    subject_cr = Subject.objects.all().order_by('id')[:3]
    tutor_cr = Tutor.objects.all().order_by('id')[:3]
    context = {'setting':setting,
               'course_cr':course_cr,
               'subject_cr':subject_cr,
               'tutor_cr':tutor_cr,}

    return render(request,'index.html',context)

def about(request):
    settings = Setting.objects.get()
    context = {'setting': settings}
    return render(request,'about.html',context)

def contact_get(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Thanks, " + data.name + "We received your message and will respond shortly... ")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.all()
    form = ContactForm
    context = {'setting': setting}
    return render(request,'contact.html',context)


def tutors(request):
    tutor = Tutor.objects.all()
    tutor_cr = Tutor.objects.all().order_by('id')[:3]
    setting = Setting.objects.get()
    context = {
               'tutor_cr' : tutor_cr,
               'tutor' : tutor,
               'setting' : setting,
    }
    return render(request, 'tutors.html', context)


def students(request):
    student = Student.objects.all()
    student_cr = Student.objects.all().order_by('id')[:3]
    setting = Setting.objects.get()
    context = {
               'student_cr' : student_cr,
               'student' : student,
               'setting' : setting,
    }
    return render(request, 'students.html', context)

def subject(request):
    subject = Subject.objects.all()
    subject_cr = Student.objects.all().order_by('id')[:3]
    setting = Setting.objects.get()
    context = {
               'subject_cr' : subject_cr,
               'subject' : subject,
               'setting' : setting,
    }
    return render(request, 'subjects.html', context)
