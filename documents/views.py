from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, InvalidPage
import operator
import json

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
    item = DocItem.objects.filter(doc=id_doc).order_by("item_intno")
    return render(request, "docinfo.html", locals())


def search(request):
    errors = []
    form = {}
    #searchw = {}
    postq = ""
    getq = ""
    #docs = []

    if request.POST or request.GET:

        try:
            page_num = request.GET.get('page')
        except KeyError:
            page_num = 1

        if request.POST:
            form['name'] = request.POST.get('name')
            page_num = 1

        elif request.GET:
            form['name'] = request.GET.get('q')

        search_word = str(form['name'])
        count_let = len(search_word)
        searchw = search_word.strip(" ").split(" ")
        #x = search_word

        if not form['name']:
            errors.append('Заполните имя')

        if not errors:
            if len(search_word) > 3:
                #for x in searchw:
                paginator = Paginator(Document.objects.filter(Q(author__icontains=search_word.strip(" ")) | Q(name__icontains=search_word.strip(" "))).order_by("name", "author"), 10)
                    #docs = Document.objects.filter(Q(author__icontains=x) | Q(name__icontains=x))
         #else:
                #pass
                #return HttpResponse('Спасибо за ваше сообщение!')
            # ... сохранение данных в базу
            # return HttpResponse('Спасибо за ваше сообщение!')
                try:
                    docs = paginator.page(page_num)
                except InvalidPage:
                    docs = paginator.page(1)

    return render(request, "search.html", locals())


def get_name_author(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        drugs = Document.objects.filter(author__icontains=q)[:20]
        results = []
        drug_json = {}
        for drug in drugs:
            drug_json['id'] = drug.doc_id
            drug_json['label'] = drug.author
            drug_json['value'] = drug.author
            results.append(drug_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
