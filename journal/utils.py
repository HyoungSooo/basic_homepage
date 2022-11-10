from .models import Year


def for_conference():
  context = {'inter': [], 'dome': []}

  year = Year.objects.all().order_by('year')
  inter_cnt = 1
  dome_cnt = 1
  for i in range(len(year)):
    inter_paper = year[i].Ypaper.filter(category = 'International')
    for k in inter_paper:
        k.ordering = inter_cnt
        k.save()
        inter_cnt += 1 
    inter_paper = inter_paper.order_by("-ordering")
    context['inter'].append({year[i] : inter_paper})

    dome_paper = year[i].Ypaper.filter(category = 'Domestic')
    for j in dome_paper:
        j.ordering = dome_cnt
        j.save()
        dome_cnt += 1
    dome_paper = dome_paper.order_by("-ordering")
    context['dome'].append({year[i] : dome_paper})

  context['inter'] = list(reversed(context['inter']))
  context['dome'] = list(reversed(context['dome']))

  return context

def for_paper():
  context = {'inter': [], 'dome': []}

  year = Year.objects.all().order_by('year')
  inter_cnt = 1
  dome_cnt = 1
  for i in range(len(year)):
    inter_paper = year[i].Yconfer.filter(category = 'International')
    for k in inter_paper:
        k.ordering = inter_cnt
        k.save()
        inter_cnt += 1 
    inter_paper = inter_paper.order_by("-ordering")
    context['inter'].append({year[i] : inter_paper})

    dome_paper = year[i].Yconfer.filter(category = 'Domestic')
    for j in dome_paper:
        j.ordering = dome_cnt
        j.save()
        dome_cnt += 1
    dome_paper = dome_paper.order_by("-ordering")
    context['dome'].append({year[i] : dome_paper})

  context['inter'] = list(reversed(context['inter']))
  context['dome'] = list(reversed(context['dome']))

  return context


def for_patents():
    context = {
      'patents' : []
    }
    
    year = Year.objects.all().order_by('year')
    
    order_cnt = 1

    for i in year:
        value = i.Ypatent.all()
        for j in value:
            j.ordering = order_cnt
            j.save()
            order_cnt += 1
        value = value.order_by("-ordering")
        context['patents'].append({i.year : value})
    context['patents'] = list(reversed(context['patents']))
    return context