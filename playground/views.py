from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Value, F, Func
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Order, Customer, Collection
from tags.models import TaggedItem

def say_hell(request):
    x = 1
    y = 2
    
    #--------ONE---------
    
    #queryset = Product.objects.filter(unit_price__range=(20,30))
    #queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    #queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    
    
    #---------TWO---------
    
    """Using the annotate expressions"""
    #queryset = Customer.objects.annotate(new_id=F('id')+1)
    # queryset = Customer.objects.annotate(
    #     #CONCAT 
    #     full_name = Func(F('first_name'),Value(' '),F('last_name'), function='CONCAT')
    # )
     
    """ OR """
     
    #queryset = Customer.objects.annotate(
        # full_name=Concat('first_name', Value(' '), 'last_name')
    #)
    
    
    #--------THREE--------
    
    #--> Referencing product's contenttype id
    # content_type = ContentType.objects.get_for_model(Product)  
    
    """Getting the tag of the items in the table referenced from content-type"""
    
    # queryset = TaggedItem.objects \
    #     .select_related('tag') \
    #     .filter(
    #         content_type = content_type,
    #         object_id = 1
    # )
    
    #NOTE!!! ==== This can be encapsulated in a function, and called directly as a --CUSTOM Manager
    #             Check TaggedItemManager in Tags Model
    #   --->   TaggedItem.objects.get_tags_for(Product,1)
     
    return render(request, 'hello.html', {'name': 'The GOAT', 'result':list(queryset)})


def say_hello(request):
    #-----Creating Objects-------->
    
    #NOTE: Item should exist b4 adding it to the created object
    
    """This method is better because all var name changes are applied throughout the application"""
    collection = Collection(pk=1) 
    collection.title = 'Clothing'
    collection.save()
    #--------------OR---------------
    # collection = Collection.objects.create(title='a', featured_product_id=1)
    
    #------Updating objects------->
    
    #'''''' All Updates (Query fetch) ''''''''
    # collection = Collection.objects.get(pk=11) 
    # collection.featured_product = None
    # collection.save()
    
    #'''''' All Updates ''''''''
    #Collection.objects.update(featured_product=None)
    
    #'''''Singke Updates -------
    #Collection.objects.filter(pk=11).update(featured_product=1)
    
    #------Single Delete------
    # collection = Collection(pk=11) 
    # collection.delete()
    #----------OR---------
    
    #'''' Multiple/Query Delete ''''
    #Collection.objects.filter(id__gt=11).delete()
    
    #------- Excuting Raw SQL Queries --------#
    #queryset = Product.objects.raw('SELECT * FROM store_product')
    
    return render(request, 'hello.html', {'name': 'The GOAT'})
    