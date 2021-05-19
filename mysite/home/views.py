import json

from django.core import serializers
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.http import require_http_methods

from home.models import Menu, Home, CourseMessage, HomeImages, TeachingResources, ReferenceBooks


@require_http_methods(["GET"])
def show_menus(request):
    response = {}
    try:
        menus = Menu.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", menus))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_homes(request):
    response = {}
    try:
        homes = Home.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", homes))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_courseMessage(request):
    response = {}
    try:
        courseMessage = CourseMessage.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", courseMessage))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_homeImages(request):
    response = {}
    try:
        homeImages = HomeImages.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", homeImages))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_teachingResources(request):
    response = {}
    try:
        teachingResources = TeachingResources.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", teachingResources))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_referenceBooks(request):
    response = {}
    try:
        referenceBooks = ReferenceBooks.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", referenceBooks))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
