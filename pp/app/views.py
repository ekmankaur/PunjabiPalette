from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.http import JsonResponse
from . models import *
from . forms import *

# Renders the home.html template and passes the current user 
# object to the template
def home(res):
    return render(res, 'app/home.html', {'user': res.user})

# Renders the aboutus.html template
def aboutus(res):
    return render(res,"app/aboutus.html")

# Renders the contactus.html template
def contactus(res):
    return render(res,"app/contactus.html")

# Retrieves products based on the given category value and renders
#  the category.html template
class Category(View):
    def get(self,res,val):
        products = Product.objects.filter(category=val)
        return render(res, "app/category.html",locals())

 # Retrieves a specific product based on the given primary key (pk) 
 # and renders the productpage.html template
class ProductPage(View):
    def get(self,res,pk):
        product = Product.objects.get(pk=pk)
        return render(res, "app/productpage.html",locals())

# Handles the form submission for user signup
# If the form is valid, saves the user and redirects to the login page
# else Renders the signup.html template with an empty SignUpForm instance
def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    
    return render(request, 'app/signup.html', {'form': form})

# Renders the profile.html template with an empty ProfileForm instance
# Handles the form submission for updating user profile
# If the form is valid, updates the user's profile and shows a success message
# If the form is invalid, shows a warning message
class Profile(View):
    def get(self,res):
        form = ProfileForm()
        return render(res,'app/profile.html', locals())
    def post(self,res):
        form = ProfileForm(res.POST)
        if form.is_valid():
            user = res.user
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            phonenumber = form.cleaned_data['phonenumber']

            customer = Customer.objects.get(user=user)
            customer.firstname = firstname
            customer.lastname = lastname
            customer.email = email
            customer.phonenumber = phonenumber
            customer.save()

            messages.success(res,"Profile Saved!")
        else:
            messages.warning(res,"Invalid Input!")
        return render(res,'app/profile.html', locals())

# Adds a product to the user's cart
    # Retrieves the product ID from the GET request parameters
    # Increments the quantity of the product in the cart or creates a new cart item if not present
def addtocard(request):
    user = request.user
    product_id = request.GET.get("product_id")
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("/cart")

# Removes a product from the user's cart
    # Retrieves the product ID from the GET request parameters
    # Decreases the quantity of the product in the cart or deletes the cart item if the quantity becomes zero
def remove_from_cart(request):
    user = request.user
    product_id = request.GET.get("product_id")
    product = Product.objects.get(id=product_id)
    
    try:
        cart_item = Cart.objects.get(user=user, product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

        return JsonResponse({'success': True})
    except Cart.DoesNotExist:
        return JsonResponse({'success': False})

# Displays the user's cart
# Retrieves the cart items for the current user
# Calculates the accumulated price for all items in the cart
def display_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    accumulated_price = 0

    for item in cart:
        price = item.product.price
        accumulated_price += price * item.quantity

    cart = Cart.objects.filter(user=user)

    return render(request, 'app/cart.html', {
        'cart': cart,
        'accumulatedprice': accumulated_price
    })

 # Places an order for the user
# Retrieves the customer's information (first name, last name, email)
# Retrieves the cart items and concatenates the product names
# Creates an Order object with the user's details and product names
# Deletes the cart items after the order is placed
def placeorder(request):
    customer = Customer.objects.get(user=request.user)
    first_name = customer.firstname
    last_name = customer.lastname
    email = customer.email

    cart = Cart.objects.filter(user=request.user)
    product_names = ', '.join([item.product.title for item in cart])

    order = Order.objects.create(
        user=request.user,
        first_name=first_name,
        last_name=last_name,
        email=email,
        product_names=product_names
    )

    cart.delete()

    return redirect('afterorder')

# Renders the afterorder.html template
def afterorder(request):
    return render(request, 'app/afterorder.html')

# Retrieves the user's orders
# Renders the orders.html template with the user's orders
def orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'orders': orders})
