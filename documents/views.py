from django.http import HttpResponse
from django.shortcuts import render
from documents.models import *
#from dateutil.tz import tzutc, tzlocal


def document(request, id_doc):
    doc = Document.objects.filter(doc_id=id_doc)
    item = DocItem.objects.filter(doc_id=id_doc)
    if doc.exists():
        if doc[0].name is None:
            s = "Unnamed Name"
        else:
            s = doc[0].name
        if doc[0].author is not None:
            s = s + " " + doc[0].author
        else:
            s = s + " " + "Unnamed Author" + " "
    else:
        s = "Not exist"

    return HttpResponse(s+str(item[0].qtyact))


def index(request, id_doc):
    doc = Document.objects.filter(doc_id=id_doc)
    item = DocItem.objects.filter(doc_id=id_doc)
    if doc.exists():
        if doc[0].name is None:
            s = "Unnamed Name"
        else:
            s = doc[0].name
        if doc[0].author is not None:
            s = s + " " + doc[0].author
        else:
            s = s + " " + "Unnamed Author" + " "
    else:
        s = "Not exist"
    doc = Document.objects.get(doc_id=id_doc)
    #itm = DocItem.objects.get(doc_id=id_doc)
    return render(request, "index.html", locals())
