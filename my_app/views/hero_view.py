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
    
    def edit(self, request, id):
        data = request.data.copy()
        validate = IdHeroValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors)
        queryset = Hero.objects.get(id=validate.data['id'])
        data_save = HeroSerializer(queryset, data=data, partial=True)
        if not data_save.is_valid():
            return validate_error(data_save.errors)
        data_save.save()
        return response_data(data=data_save.data)
    
    def delete(self, request, id):
        data = request.data.copy()
        validate = IdHeroValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors)
        result = Hero.objects.get(id=validate.data['id'])
        result.deleted_at = datetime.now()
        result.save()
        return response_data()
    
    def restore(self, request, id):
        data = request.data.copy()
        validate = IdHeroValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors)
        result = Hero.objects.get(id=validate.data['id'])
        result.deleted_at = None
        result.save()
        serializer = HeroSerializer(result)
        return response_data(serializer.data)
    
    def drop(self, request, id):
        data = request.GET.copy()
        validate = IdHeroValidate(data={'id':id})
        if not validate.is_valid():
            return validate_error(validate.errors)
        Hero.objects.get(id=validate.data['id']).delete()
        return response_data()