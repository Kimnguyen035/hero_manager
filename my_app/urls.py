from django.urls import path
from .views.hero_view import *

all_url = {
    'url_hero_view':[
        path('get-all', HeroView.as_view({'get':'get_all'}), name='get_all'),
        path('get-detail/<int:id>', HeroView.as_view({'get':'get_detail'}), name='get_detail'),
        path('add-hero', HeroView.as_view({'post':'add'}), name='add'),
    ]
}   

urlpatterns = []

for item in all_url:
    urlpatterns += all_url[item]