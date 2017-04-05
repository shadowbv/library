from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from documents.models import *

#from dateutil.tz import tzutc, tzlocal


#def document(request, id_doc):
#    doc = Document.objects.filter(doc_id=id_doc)
#    item = DocItem.objects.filter(doc_id=id_doc)
#    if doc.exists():
#        if doc[0].name is None:
#            s = "Unnamed Name"
#        else:
#            s = doc[0].name
#        if doc[0].author is not None:
#            s = s + " " + doc[0].author
#        else:
#            s = s + " " + "Unnamed Author" + " "
#    else:
#        s = "Not exist"
#
#    return HttpResponse(s+str(item[0].qtyact))


def document(request, id_doc):
    try:
        doc = Document.objects.get(doc_id=id_doc)
    except ObjectDoesNotExist:
        pass
    item = DocItem.objects.filter(doc=id_doc)
    return render(request, "index.html", locals())


def search(request):
    errors = []
    form = {}
    if request.POST:
        form['name'] = request.POST.get('name')

        if not form['name']:
            errors.append('Заполните имя')#

        if not errors:
            docs = Document.objects.filter(author__icontains=form['name'])
            # ... сохранение данных в базу
            # return HttpResponse('Спасибо за ваше сообщение!')

    return render(request, "search.html", locals())

