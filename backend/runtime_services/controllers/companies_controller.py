import json
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from webapi.models import Company
from django.core import serializers
from controllers.serializers.companies_serializer import CompanySerializer
from rest_framework import status
from json.decoder import JSONDecodeError
from django.db.utils import IntegrityError
import datetime


def get(request, companyId):
    objects = Company.objects.filter(pk=companyId)
    if len(objects) == 0:
        return HttpResponseNotFound("Not Found")
    
    data = serializers.serialize('json', objects)
    return HttpResponse(data, 'application/json')

def getAll(request):
    objects = Company.objects.all()
    if len(objects) == 0:
        return HttpResponseNotFound("Not Found")
    
    data = serializers.serialize('json', objects)
    return HttpResponse(data, 'application/json')

def post(request):
    try:
        model = json.loads(request.body.decode('utf-8'))
        entity = CompanySerializer(data=model)
        
        if entity.is_valid():
            entity.validated_data['createdAt'] = datetime.datetime.now()
            entity.validated_data['updatedAt'] = datetime.datetime.now()
            entity.validated_data['profile_id'] = 1
            entity.save()
            data = serializers.serialize('json', [entity.instance])
            return HttpResponse(data, 'application/json')
        else:
            return BadRequestHandler("Request payload failed schema validation")
    except JSONDecodeError as e:
        return BadRequestHandler(e.args[0])
    except IntegrityError as e:
        return BadRequestHandler(e.args[1])
    

def patch(request, companyId):
    objects = Company.objects.filter(pk=companyId)
    if len(objects) == 0:
        return HttpResponseNotFound("Not Found")
    
    try:
        model = json.loads(request.body.decode('utf-8'))
        entity = CompanySerializer(data=model)
        savedEntity = objects[0]
        
        if entity.is_valid():
            savedEntity.updatedAt = datetime.datetime.now()
            savedEntity.name = entity.validated_data['name']
            savedEntity.state = entity.validated_data['state']
            savedEntity.country = entity.validated_data['country']
            savedEntity.zipCode = entity.validated_data['zipCode']
            savedEntity.email = entity.validated_data['email']
            savedEntity.portal = entity.validated_data['portal']
            savedEntity.save()
            data = serializers.serialize('json', [savedEntity])
            return HttpResponse(data, 'application/json')
        else:
            return BadRequestHandler("Request payload failed schema validation")
    except JSONDecodeError as e:
        return BadRequestHandler(e.args[0])
    except IntegrityError as e:
        return BadRequestHandler(e.args[1])
    
        
def delete(request, companyId):
    objects = Company.objects.filter(pk=companyId)
    if len(objects) == 0:
        return HttpResponseNotFound("Not Found")
    
    entity = objects[0]
    entity.delete()
    data = serializers.serialize('json', objects)
    return HttpResponse(data, 'application/json')

    
def BadRequestHandler(e):
    error = {
        "message": e,
        "schema": {
            "name" : "",
            "state": "",
            "country": "",
            "zipCode": "",
            "email": "",
            "portal": ""
        }
    }
    return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
    