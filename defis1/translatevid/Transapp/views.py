from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse

def Home(req):
    return render(req,'transapp/index.html')

@csrf_exempt 
def translate(req):
    if req.method=="POST":
        body=json.loads(req.body)
        langue=body.get('langue')
        print(langue)
        reponse={
            "message":"hello"
        }
        repjson=json.dumps(reponse)
        return HttpResponse(repjson,content_type="application/json")
    return None