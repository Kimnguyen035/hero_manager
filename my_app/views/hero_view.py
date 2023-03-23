from .views import *

class HeroView(ViewSet):
    def get_all(self, request):
        queryset = Hero.objects.filter(deleted_at__isnull=True)
        serializer = HeroSerializer(queryset, many=True)
        return response_data(serializer.data)
    
    def get_detail(self, request, id):
        validate = IdHeroValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors)
        hero_detail = Hero.objects.get(id=validate.data['id'])
        serializer = HeroSerializer(hero_detail)
        return response_data(data=serializer.data)
    
    def add(self, request):
        data = request.data.copy()
        data_save = HeroSerializer(data=data)
        if not data_save.is_valid():
            return validate_error(data_save.errors)
        data_save.save()
        return response_data(data=data_save.data)