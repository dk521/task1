

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *

# Items with rating 3 or above
class Items(APIView):
    def get(self, request):

        items = Ratings.objects.filter(rating__gte=3)

        items_list = []

        for i in items:
            one_item = {}

            one_item['category'] = i.subcategory.category.name
            one_item['sub_category'] = i.subcategory.name
            one_item['item_name'] = i.name
            one_item['item_description'] = i.description
            one_item['rating'] = i.rating

            items_list.append(one_item)

        return Response(items_list)


# nested json format -> Category -> subcategory -> items
class Items(APIView):
    def get(self, request):
        items = Items.objects.all()



        categories = []
        
        

        for i in Categories.objects.all():
            one_category = {}
            one_category['description'] = i.description
            subcategoris = []

            for j in SubCategories.objects.filter(category=i):

                items = []
                one_subcategory = {}                
                one_subcategory['descripton'] = j.descripton


                for k in Items.obejcts.filter(subcategory=j):
                    one_item = {}
                    one_item['name'] = k.name
                    one_item['price'] = k.price
                    one_item['description'] = k.description
                    items.append(one_item)

                one_subcategory = {'items' : items}

                subcategories.append(one_subcategory)

            categories.append(one_category)

        return Response(categories)





            

            

