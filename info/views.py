from django.shortcuts import render
from member.models import Member, Professor, CATEGORY, POSITION
from journal.models import Projects, Research
from collections import OrderedDict
from journal.utils import for_conference, for_paper, for_patents

# Create your views here.



def info(request):
    return render(request, "info.html", {})

def location(request):
    return render(request, "location.html", {})

def members(request):
    context = {}
    for i in POSITION:
        p = Member.objects.filter(position = i[0])

        context[i[0]] = p

    return render(request, "members.html", context)

def professor(request, profname):
    p = Professor.objects.get(name =profname)
    P_all = Professor.objects.all().exclude(name =profname)

    context = {"obj": p, "other" : P_all}

    for i in CATEGORY:
        k = p.prof_time.filter(category = i[0])

        context[i[0]] = k

    return render(request, "professor.html", context= context)

def publictaions(request, category):
    
    if category =='paper':
        context = for_paper()
    else:
        context = for_conference()

    return render(request , "publication.html", context= context)

def conferences(request):
    return render(request , "publication.html", {})

def patents(request):
    context = for_patents()
    return render(request , "patents.html", context)

def project(request):
    active_p = Projects.objects.all().filter(category = "Active").order_by("-start_date")
    finish_p = Projects.objects.all().filter(category = "Finish").order_by("-start_date")
    context = {}

    active_cnt = 1
    finish_cnt = 1

    for i in active_p:
      i.ordering = active_cnt
      i.save()
      active_cnt += 1
    
    for j in finish_p:
      j.ordering = finish_cnt
      j.save()
      finish_cnt += 1

    context['active'] = active_p
    context['finish'] = finish_p

    return render(request , "project.html", context)

def research(request):
    p = Research.objects.all()

    return render(request , "research.html", {'res' : p})

def album(request):
    return render(request , "album.html", {})

def members_detail(request, pk):
    context = {}

    obj = Member.objects.get(id = pk)

    context['obj'] = obj
    return render(request, "member_detail.html", context= context)
