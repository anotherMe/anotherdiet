import tastypie.resources as res
import tastypie.constants as const
from longevity.models import Food


class FoodResource(res.ModelResource):

    class Meta:
        queryset = Food.objects.all()
        resource_name = 'food'
        filtering = {
            #"nome": const.ALL
            "nome": ('contains')
        }