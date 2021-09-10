from django.shortcuts import render
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, status
from .models import Messages
from django.core.paginator import Paginator
import re
from django.http import JsonResponse
import json
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MessageSerializers

# Create your views here.


class MessagesView(APIView):
    def get(self, request):
        if request.method == "GET":
            try:
                message = Messages.objects.all()
                return HttpResponse(message)
            except Exception as e:
                return HttpResponse(e)


class MessagesSingleView(APIView):
    def get(self, request, pk):
        if request.method == "GET":
            try:
                message = Messages.objects.get(pk=pk)
                return HttpResponse(message)
            except Exception as e:
                return HttpResponse(e)


class MessagesListView(APIView):
    def get(self, request, id):
        if request.method == "GET":
            try:
                message = Messages.objects.all()
                pagination = Paginator(message, 10)
                users = pagination.page(id + 1)
                return HttpResponse(users)
            except Exception as e:
                return HttpResponse(e)


# @method_decorator(csrf_exempt, name='dispatch')
# @action(methods=['post'], detail=True, permission_classes=[IsAdminUser])
class MessagesCreateView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializers

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)








    # def create_message(self, request):
    #     try:
    #
    #         data = json.loads(request.body.decode("utf-8"))
    #         author = data.get('author')
    #         text = data.get('text')
    #         if ValidateEmail(author) and ValidateText(text):
    #             product_data = {
    #                     'author': author,
    #                     'text': text,
    #             }
    #             message = Messages.objects.create(**product_data)
    #             data = {
    #                 'message': f"New message added with email {message.author}"
    #             }
    #             return JsonResponse(data, status=201)
    #     except Exception as e:
    #         return HttpResponse(e)


def ValidateEmail(email):
    if len(email) > 6:
        if re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email) is not None:
            return 1
    return 0

def ValidateText(text):
    if len(text)<=100:
        if re.match('^(?!\s*$).+', text) is not None:
            return 1
    return 0

