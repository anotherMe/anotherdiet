from tastypie.resources import ModelResource
from longevity.models import Alimento


class AlimentoResource(ModelResource):
	
	class Meta:
		queryset = Alimento.objects.all()
		resource_name = 'alimento'
