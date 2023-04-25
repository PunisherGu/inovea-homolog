from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
import requests
import os

from core.serializers import testserializer

class ArticlesGetView(generics.GenericAPIView):


    def get(self, request, subject):
        api_key = os.getenv('API_KEY')

        url = f'https://newsapi.org/v2/everything?q={subject}&apiKey={api_key}'

        request = requests.get(url)
        
        if request.status_code == 200:
            articles_list = []
            response = request.json()
            articles = response['articles']

            for article in articles:
                data = {
                    'author': article['author'],
                    'title': article['title'],
                    'description': article['description'],
                }
                articles_list.append(data)

            content = {
                'success': True,
                'message': 'Artigos listados com sucesso',
                'data': articles_list
            }
            return Response(content, status=status.HTTP_200_OK)



        else:
            response = request.json()
            message = response['message']
            content = {
                'success': False,
                'message': f'A solicitação externa retornou {request.status_code} com a mensagem - {message}',
            }
            return Response(content, status=status.HTTP_200_OK)

        
        