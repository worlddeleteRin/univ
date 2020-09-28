from django.shortcuts import render
from .models import * 
from django.http import JsonResponse, HttpResponse
from django.core.files.base import ContentFile
import urllib
import os

def index(request):
    all_subjects = Subject.objects.all()
    return render(request, 'lessons/index.html', {
        'subjects': all_subjects,
    })

def subject(request, subject_id):
    current_subject = Subject.objects.get(id = subject_id)
    # itypes = current_subject.item_set.all()
    # itypes = itypes.values('itype').distinct()
    # item_types = Itemtypes.objects.filter(id__in = itypes)
    # print(item_types)
    itypes = Itemtypes.objects.filter(subject__id = subject_id)
    return render(request, 'lessons/subject.html', {
        'subject': current_subject,
        'itypes': itypes,
    })

def itype(request, subject_id, itype_id):
    current_subject = Subject.objects.get(id = subject_id)
    current_itype = Itemtypes.objects.get(id = itype_id)
    items = Item.objects.filter(
        subject = current_subject,
        itype = current_itype,
    )
    items = items.order_by('-date')
    return render(request, 'lessons/itype.html', {
        'current_subject': current_subject.id,
        'current_itype': current_itype.id,
        'items': items,
    })

def add_item_ajax(request):
    path = 'static/files/'
    current_file = request.FILES['file']
    print(request.FILES['file'])

    subject = int(request.POST['subject'])
    itype = int(request.POST['itype'])
    name = str(request.POST['name'])
    current_subject = Subject.objects.get(id = subject)
    current_itype = Itemtypes.objects.get(id = itype)


    full_name = path + str(current_file)
    fout = open(full_name, 'wb+')
    # file_content = ContentFile(current_file.read())
    cf = current_file.read()
    # for chunk in file_content.chunk():
    fout.write(cf)
    fout.close()
    item_size = os.path.getsize(full_name)
    item_size = item_size / 1024
    item_size = item_size / 1024
    item_size = round(item_size, 4)
    print(item_size)

    current_item = Item(
        name = name,
        subject = current_subject,
        itype = current_itype,
        itemurl = current_file,
        itemsize = item_size,
    )
    current_item.save()

    return JsonResponse({
        'message': 'it is ok'
    }, status = 200)

def add_itype_ajax(request):
    itype = request.GET['itype']
    itype  = urllib.parse.unquote(itype)
    subject = request.GET['subject']
    current_subject = Subject.objects.get(id = subject)
    if (Itemtypes.objects.filter(subject = current_subject, name = itype).exists()):
        return JsonResponse({
            'message': 'exist'
        })
    else:
        new_itype = Itemtypes(
            subject = current_subject,
            name = itype,
        )
        new_itype.save()
        return JsonResponse({
            'message': 'ok',
        })

def delete_itype_ajax(request):
    password = request.GET['password']
    itype = request.GET['itype']
    current_itype = Itemtypes.objects.get(id = itype)
    if (password == '343845'):
        current_itype.delete()
        return JsonResponse({
                'message': 'ok',
            })
    else:
        return JsonResponse({
                'message': 'invalid',
            })

def addblock_items_ajax(request):
    print('start loading')
    subjectid = request.GET['subject_id']
    subject = Subject.objects.get(id = subjectid)
    itypes = Itemtypes.objects.filter(subject__id = subjectid)
    print(itypes)
    print('itypes collected')
    return render(request, 'lessons/blocks/itypes_items.html', {
        'subject': subject,
        'itypes': itypes,
    })
    # return HttpResponse(content = 'kek')

def delete_item_ajax(request):
    password = request.GET['password']
    item_id = request.GET['item_id']
    if password == '343845':
        path = 'static/files/'
        current_item = Item.objects.get(id = item_id)
        os.remove(path + current_item.itemurl)
        current_item.delete()
        return JsonResponse({
            'message': 'deleted',
        }, status = 200)
    else:
        return JsonResponse({
            'message': 'invalid',
        }, status = 200)

def load_item_ajax(request):
    sid = request.GET['subject_id']
    itid = request.GET['itype_id']
    items = Item.objects.filter(
        subject__id = sid,
        itype__id = itid,
    )
    items = items.order_by('-date')
    return render(request, 'lessons/blocks/items_list.html', {
        'items': items,
    })