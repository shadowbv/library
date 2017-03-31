from django.http import HttpResponse
from students.models import *
#from dateutil.tz import tzutc, tzlocal


def student(request, stud_id):
    reader = PhysicalPerson.objects.filter(id=stud_id)
    s = ""
    i = 1
    if reader.exists():
        #for item in reader:
            s = reader[0].name + " " + reader[0].in_date.strftime('%d.%m.%Y %H:%M')
            #i += 1
    else:
        s = "Not exist"

    return HttpResponse(s)

