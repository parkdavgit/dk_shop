from django.test import TestCase

# Create your tests here.
# python manage.py runserver
# python manage.py migrate

# ub***/***4 super user
# Create your tests here.
# python manage.py runserver
# python manage.py makemigrations
# python manage.py migrate
#paypal personal 
#persondk@gmail.com
#Enough60!

# cart making - use cart doc. in note pad 
# order buythis - order name and amount is not needed.

# 왜 detail.html에서 destination_id, destination.price가 안 보일까?
# context={'destination':destination}이게 빠졌었다!

# 왜 cart 저장 후 cart 보여주기가 안 될까? 아래 카트 뷰로 OK

##def cartview(request, user_id):
    ##cart = Cart.objects.filter(user=user) 
    ##context = {'user': user, 'cart': cart }
    ##return render(request, 'cartview.html', context)

# CART DELETE - OK
##HTML( Form POST 로 %URL cart_delete, user.pk  ) <button type="submit" name="delete_cart" value="delete_cart">삭제하기</button>
###{% csrf_token %} - user.pk or usr.id OK but user_id NOT OK. user_id is OK at URL not OK at html

##URL path('cartview/<int:user_id>/delete', views.delete_cart, name='delete_cart'),

##VIEW 
###def delete_cart(request, user_id): #user.pk =1 or 16 david
###    user = request.user#david
###    cart = Cart.objects.filter(user=user)
###    quantity = 0
###    if request.method == 'POST':
###        pk =int(request.POST.get('destination'))
###        destination = Destination.objects.filter(pk=pk)
###        for i in cart:
###            if i.destinations == destination :
###                quantity =  i.quantity
###        if quantity > 0 or quantity == 0:
###            destination = Destination.objects.filter(pk=pk)
###            cart = Cart.objects.filter(user=user, destinations__in=destination)
###            cart.delete()
###            return redirect('cartview', user.pk)   


# CART --> ORDER 할 차례 : OK
## <tr><td><a href="{% url 'allorder' user.pk %}">PLACE ORDER</a>
##URL path('allorder/<int:user_id>/', views.allorder, name='allorder'),

##VIEW 
###def order(request, user_id): #user.pk =1 or 16 david
###   @login_required   

# ORDER --> PAYPAL PAYMENT ( BY ORDER ID ) : OK    
  

# ORDER 삭제 기능 추가할 것
  
#<input type="radio" id="product_{{ product.id }}" name="product" value="{{ product.products.id }}">    

# ORDER 삭제 기능 추가: OK



# def total_cost(self):
#         return sum([ li.cost() for li in self.lineitem_set.all() ] )

# def sum_cost(self):
#         return sum([ li.total_cost() for li in Allorder.objects.all() ] )

# PAYPAL ALL ORDER ?

# ERROR:Model not defined when using foreign key to second model
# You need to move the definition of Country above the definition of User.
# So the basic rule of thumb-> Everything has to be defined before you call or reference it




    
    # CART --> CHECKOUT ( ORDER ID, ADDRESS) --> PAYPAL


#<class 'travello.models.Checkorder'>": "Allorder.checkorder" must be a "Checkorder" instance.
    #checkorder = Checkorder.objects.filter(pk=o.pk) OKOKOK
           
            #for cart_item in all_items:
                # checkorder_id = o.pk       OKOKOK
                #li.save()                    li. is Allorder so Order save
                # Allorder 의 checkorder instance는 checkorder_id 이 값을 방금 저장한 checkout의 pk로 받아 저장함 
# OK
    
# CHECKOUT ( ORDER ID, ADDRESS) --> PAYPAL

# class Checkorder(models.Model):
# def total_cost(self):
# return sum([ li.cost() for li in self.allorder_set.all() ] ) 

# Error Message - checkorder doesn't have allorder 

# Error: because of this  
# checkorder = models.ForeignKey(Checkorder, on_delete=models.CASCADE, related_name='Allorder_checkorder')

# The reason the reverse is a queryset is, ForeignKey is 1-to-many relationship. Hence, the reverse is a queryset.
# The _set object is made available when related_name is not specified. 

# Solution : remove related_name
# checkorder = models.ForeignKey(Checkorder, on_delete=models.CASCADE)


# ALLORDER DELETE - OK

# DELETE OLD ORDER BEFORE NEW ORDER CHECKOUT - OK

# 선택한 상품취소시 선택이 안 된 경우 에러 해결 할 것 -  OK : checked="checked"
# <input type="radio" id="destination_{{ destination.id }}" name="destination" value="{{ destination.destinations.id }}" checked="checked">   


# SEARCH FOOD FUNCTION - OK (search.txt)

# BASE.html 형태로 변경 - OK 

# ADD CART 비회원이 했을 때 ERROR handling 
# from django.contrib.auth.decorators import login_required
# @login_required() -->  @login_required(login_url='index')
# 비회원이 CART 쓰려고 하면 index로 돌아가게  - OK

# 이런 기능 추가 - 
# if superuser 
# <a href="{% url 'food_create' %}" class="btn btn-primary float-right">등록</a>
# pic 이미지가 안 올라간다
# view.py 에서
# form = NewFoodForm(request.POST)을 아래로 바꾸니 OK
# form = NewFoodForm(request.POST, request.FILES)
# Image Upload 정리해서 저장할 것 (image_upload.txt)


# path('product/product_create/', views.product_create, name='product_create'), OK
# path('product_edit/<int:product_id>/', views.product_edit, name='product_edit'), OK (Ref:EDIT_MY_SHOPPING.txt)



# path('product_delete/<int:product_id>/', views.product_delete, name='product_delete'),
# ERROR: local variable 'destination' referenced before assignment
# destination = get_object_or_404(destination, pk=destination_id) -- ERROR: local variable 'destination' referenced before assignment
# destination = get_object_or_404(Destination, pk=destination_id) -- OK

# python manage.py runserver

 