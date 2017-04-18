# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

#view for Students
def students_list(request):
    students = (
    {'id':1,
    'first_name': u'Виталий',
    'last_name': u'Podoba',
    'ticket': 235,
    'image': 'img/podoba3.jpg'},
    {'id':2,
    'first_name': u'Yan',
    'last_name': u'Khadzhyisky',
    'ticket': 2135,
    'image': 'img/piv.jpg'},
    )
    return render(request, 'students/students_list.html', {'students':students})
def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')
def students_edit(request, sid):
    return HttpResponse('<h1>Students Edit %s Form</h1>' % sid)
def students_delete(request, sid):
    return HttpResponse('<h1>Students Delete %s Form</h1>' % sid)

#view for Groups
def groups_list(request):
    return HttpResponse('<h1>Groups List Form</h1>')
def groups_add(request):
    return HttpResponse('<h1>Groups Add Form</h1>')
def groups_edit(request, gid):
    return HttpResponse('<h1>Groups Edit %s Form</h1>' % gid)
def groups_delete(request, gid):
    return HttpResponse('<h1>Groups Delete %s Form</h1>' % gid)
