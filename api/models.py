from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization  # Добавляем импорт
from shop.models import Category, Course
from .authentication import CustomApiKeyAuthentication

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']
        authentication = CustomApiKeyAuthentication()
        authorization = Authorization()  # Добавляем

class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomApiKeyAuthentication()
        authorization = Authorization()  # Исправляем