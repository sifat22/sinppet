from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from.models import Snippet
from app_snippets.serializers import SnippetSerializer

# Create your views here.

@csrf_exempt #when we don't want to use csrf token we use this
def snippet_list(request):
    #list all snippet
    if request.method=="GET":
        snipptes= Snippet.objects.all()
        serializers = SnippetSerializer(snipptes, many=True)
        return JsonResponse(serializers.data, safe=False)#if the data is not ina dictionary we need to set safe= false to allow non dictionary data
    
    elif request.method=='POST':
        #Converts the raw JSON payload from the request body into native Python datatypes 
        data = JSONParser().parse(request)
        serializers = SnippetSerializer(data= data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status= 201)
        return JsonResponse(serializers.errors, status=400)
    
@csrf_exempt
def snippet_detail(request, id):
    try:
        snippet = Snippet.objects.get(id = id)
    except Snippet.DoesNotExist:
        return HttpResponse(status= 404)
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

        
