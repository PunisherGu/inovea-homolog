from django.urls import path
from core.views import *


urlpatterns = [
  path('articles/<str:subject>/get', ArticlesGetView.as_view(), name='articles_get'),
]