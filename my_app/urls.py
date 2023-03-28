from django.urls import path
from .views.hero_view import *

all_url = {
    'url_hero_view':[
        path('get-all', HeroView.as_view({'get':'get_all'}), name='get_all'),
        path('get-detail/<int:id>', HeroView.as_view({'get':'get_detail'}), name='get_detail'),
        path('add-hero', HeroView.as_view({'post':'add'}), name='add'),
        path('edit-hero/<int:id>', HeroView.as_view({'put':'edit'}), name='edit'),
        path('delete-hero/<int:id>', HeroView.as_view({'delete':'delete'}), name='delete'),
        path('restore-hero/<int:id>', HeroView.as_view({'delete':'restore'}), name='restore'),
        path('drop-hero/<int:id>', HeroView.as_view({'delete':'drop'}), name='drop'),
    ]
}   

urlpatterns = []

for item in all_url:
    urlpatterns += all_url[item]