from django.conf.urls import url, include
from longevity.api import FoodResource
from . import views


food_resource = FoodResource()

urlpatterns = [
    url(r'^api/', include(food_resource.urls)),
    url(r'^$', views.index, name='index'),
]
