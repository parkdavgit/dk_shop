from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Destination, Cart, Allorder, Checkorder 
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from .forms import CheckoutForm, NewFoodForm 
 
from django.conf import settings
import uuid

# Create your views here.
def index(request):
	
	dests = Destination.objects.all()
	page = request.GET.get('page','1')

	paginator = Paginator(dests, 8)
	page_obj = paginator.get_page(page)
	 
	return render(request, 'index.html',{'dests':page_obj})

def detail(request, dest_id):
    #destination = Destination.objects.get(pk=dest_id)
    destination=get_object_or_404(Destination,id=dest_id)   
    context={'destination':destination}

    return render(request, 'detail.html', context)

@login_required(login_url='index')
def cart(request, destination_id):
    quantity = request.POST.get('quantity')#detail.html에서 선택한 quantity를 받음.
    destination=get_object_or_404(Destination,id=destination_id)   #pk=5인 objects 갈비 가격 재고수량....
    user = request.user#login user
   
    initial = {'name': destination.name, 'quantity': quantity}#갈비 가격 그리고 카트에 담은 수
    cart = Cart.objects.filter(user=user)#user가 login한 user의 카트 objects - user, destinations, quantity
    
    if request.method == 'POST':
      
            for i in cart :
                if i.destinations == destination:#카트에 destination가 갈비가 있으면  
                    destination = Destination.objects.filter(pk=destination_id)#갈비 정보
                    Cart.objects.filter(user=user, destinations__in=destination).update(quantity=F('quantity') + quantity)
                    messages.success(request,'장바구니 등록 완료')
                    return redirect('cartview', user.pk)


            Cart.objects.create(user=user, destinations=destination, quantity=quantity)
            messages.success(request, '장바구니 등록 완료')
            return redirect('cartview', user.pk)


@login_required(login_url='index')
def cartview(request, user_id):
   
    user = User.objects.get(pk=user_id)#user david 1111 objects
    cart = Cart.objects.filter(user=user)#david cart 
    ##paginator = Paginator(cart, 10)
    ##page = request.GET.get('page')
    ##try:
        ##cart = paginator.page(page)
    ##except PageNotAnInteger:
        ##cart = paginator.page(1)
    ##except EmptyPage:
       ##cart = paginator.page(paginator.num_pages)
    context = {'user': user, 'cart': cart }
    return render(request, 'cartview.html', context)


def delete_cart(request, user_id): #user.pk =1 or 16 david
    
    user = request.user#david
    cart = Cart.objects.filter(user=user)#
    quantity = 0
   
    if request.method == 'POST':
        pk =int(request.POST.get('destination'))
       
        #while True:
            #try:
                #pk =int(request.POST.get('destination'))
        
                #break  # 정상적으로 숫자를 입력받은 경우 while문 수행을 중단합니다.
            #except ValueError:
                #return redirect('cartview', user.pk)       # ValueError가 발생하면 수행

    
        destination = Destination.objects.filter(pk=pk)
        for i in cart:
            if i.destinations == destination :
                quantity =  i.quantity

        if quantity > 0 or quantity == 0:
            destination = Destination.objects.filter(pk=pk)
            cart = Cart.objects.filter(user=user, destinations__in=destination)
            cart.delete()
            return redirect('cartview', user.pk)   

 

def checkout(request, user_id):
    user = request.user
    allorder = Allorder.objects.filter(user=user)#
    allorder.delete()
    # before checkout, all old order should be deleted


    user = request.user#david
    cart = Cart.objects.filter(user=user)#
    # this checkout is for Order name email postal code address saving purpose
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            o = Checkorder(
                name = cleaned_data.get('name'),
                email = cleaned_data.get('email'),
                postal_code = cleaned_data.get('postal_code'),
                address = cleaned_data.get('address'),
            )
            o.save()

    # this is for Order product price quantity order_id saving purpose @ Allorder
            # from  cart items to order items save
            all_items = Cart.objects.filter(user=user)
            
            checkorder = Checkorder.objects.filter(pk=o.pk)
           
            for cart_item in all_items:
                li = Allorder(
                    user=user,
                    quantity = cart_item.quantity,
                    destinations = cart_item.destinations,
                    checkorder_id = o.pk
                )
                li.save()

            # this delete all cart item and this is from cart.py
            
            all_items.delete()

            request.session['checkorder_id'] = o.pk

            messages.add_message(request, messages.INFO, 'Order Placed!')
            return redirect('payment',  user.pk)


    else:
               
        form = CheckoutForm()
        return render(request, 'checkout.html', {'cart': cart,'form': form})      



def payment(request, user_id):
    checkorder_id= request.session.get('checkorder_id')
    checkorder=get_object_or_404(Checkorder,id=checkorder_id)
    
    user = User.objects.get(pk=user_id)
    destination = Destination.objects.all()
    allorder = Allorder.objects.filter(user=user)
     

    host=request.get_host()
	

    paypal_dict= {
        'business': 'Businessdk@gmail.com',
        'amount':checkorder.total_cost,
        'item_name': checkorder.id, # paypal order detail 누르면 나타나는 이름
        'currency_code':'USD',
        'notify_url':'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url':'http://{}{}'.format(host, reverse('payment_success')),
        'cancel_url':'http://{}{}'.format(host, reverse('payment_failed' )), 
    }    
    
    form= PayPalPaymentsForm(initial=paypal_dict)

    context= {'checkorder': checkorder,'user': user,'destination': destination,'allorder': allorder, 'form':form }
	
    return render(request, 'paypal_payment.html',context)   


@csrf_exempt
def payment_success(request):
   
    return render(request, 'payment_success.html')

@csrf_exempt
def payment_failed(request):
    
    return render(request, 'payment_failed.html')
   




def delete_order(request, user_pk): #user.pk =1 or 16 david
    
    user = User.objects.get(pk=user_pk)
    allorder = Allorder.objects.filter(user=user)#
    allorder.delete()
   

    return redirect('index') 
    

def food_search(request):

    food_name = request.POST.get('food_name', '').strip()

    if len(food_name) == 0:
        food_name = request.GET.get('food_name', '').strip()

    destinations = Destination.objects.filter(name=food_name)
        
    context = {'destinations': destinations}
    return render(request, 'searchR.html', context)  

 
def food_create(request):
    if request.method == 'POST':
        form = NewFoodForm(request.POST, request.FILES)
        if form.is_valid():
        
            cleaned_data = form.cleaned_data
            p=Destination(

                name = request.POST['name'],
                price = request.POST['price'],
                desc = request.POST['desc'],
                img = request.FILES['img'],
        
                )
            p.save()

            messages.success(request, "success!")
            return redirect('index')
        else:
            print(form.errors)
            messages.error(request, "fail!")

    else:
        form = NewFoodForm()
    return render(request, 'food_create.html', {'form':form})


@staff_member_required
def food_edit(request,destination_id):
    user = request.user
    destination = get_object_or_404(Destination, pk=destination_id)
    
    
    if request.method == 'POST':#form 채워 온 것을 받고  save 하고 나머지 author ,timezone 정해줌
        form = NewFoodForm(request.POST, instance=destination)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.author = request.user
            
            destination.save()
            return redirect('index')
    else:
        form = NewFoodForm(instance=destination)#destination_create.html form에 destination instance 넣어 보여줘라
        return render(request, 'food_create.html', {'form': form})

@staff_member_required
def food_delete(request, destination_id):
    destination = get_object_or_404(Destination, pk=destination_id)
    destination.delete()
    return redirect('index') 

def profile(request):
    context = {'user': request.user}
    return render(request, 'profile.html', context)        