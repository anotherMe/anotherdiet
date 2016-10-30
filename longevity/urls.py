from django.conf.urls import url, include
from longevity.api import AlimentoResource
from . import views


alimento_resource = AlimentoResource()

urlpatterns = [
    url(r'^api/', include(alimento_resource.urls)),
    url(r'^$', views.index, name='index'),
]
