from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests as req

# Create your views here.

def index(request):
    res = req.get("https://dummyjson.com/products")
    #plist =res.json()["products"]
    #names = [x["title"] for x in plist]
    #html_result = f'''
    #                <ol>
    #                    <li>
    #                        {"</li><li>".join(names)}
    #                    </li>
    #                </ol>
    #                '''
    #return HttpResponse(html_result)
    return render(request,template_name='index.html', context={"plist": res.json()["products"]})

