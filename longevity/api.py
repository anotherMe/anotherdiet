from tastypie.resources import ModelResource
from longevity.models import Food


class FoodResource(ModelResource):
	
	class Meta:
		queryset = Food.objects.all()
		resource_name = 'food'
