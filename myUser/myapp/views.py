from django.http import HttpResponse
from .models import UserProfile

def insert(request, uid, q):
  qs = UserProfile(user_id=uid, questions=q)
  qs.save()
  return HttpResponse("Created!! the id is " + str(qs.id))

def delete(request, upid):
  qs = UserProfile.objects.filter(id=upid)
  if qs.count() == 0:
    return HttpResponse("Not found!!")
  else:
    qs.delete()
    return HttpResponse("Delete!!")
  
def update(request, upid, q):
  qs = UserProfile.objects.filter(id=upid)
  if not qs.exists():
    return HttpResponse("Not found!!")
  else:
    qs.update(questions=q)
    return HttpResponse("Updated!!")

def show_all(request):
  output = ""
  for val in UserProfile.objects.all().values():
    output += str(val['id']) + " " + val['questions'] + " " + str(val['user_id']) + "<br>"

  return HttpResponse(output)

