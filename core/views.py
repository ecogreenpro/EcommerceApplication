from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View

from .forms import ProfileModelForm
from .models import Products, CartProducts, Order, userProfile
from .models import Products, Categories, Brands
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def header(request):
    context = {}
    return render(request, 'header.html', context)


def footer(request):
    context = {}
    return render(request, 'footer.html', context)


# def home(request):
#     context = {}
#     product = Products.objects.raw("SELECT * FROM core_products")
#     return render(request, 'home.html', {"Products": product})


def about(request):
    context = {}
    return render(request, 'base/about.html', context)


def contact(request):
    context = {}
    return render(request, 'base/contact.html', context)


def privacyPolicy(request):
    context = {}
    return render(request, 'base/privacyPolicy.html', context)


def terms(request):
    context = {}
    return render(request, 'base/refundReturnsPolicy.html', context)


def paymentProcess(request):
    context = {}
    return render(request, 'base/paymentProcess.html', context)


def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'account/userprofile.html')
        else:
            messages.info(request, 'Invalid Login')
    else:
        return render(request, 'account/login.html', context)
    return render(request, 'account/login.html', context)


def logout(request):
    auth.logout(request)
    messages.info(request, 'Successfully Logout')
    return redirect('/login/')


def dashboard(request):
    context = {}
    return render(request, 'account/dashboard.html', context)


def forgotpassword(request):
    context = {}
    return render(request, 'account/forgotpassword.html', context)


def changePassword(request):
    context = {}
    return render(request, 'account/changePassword.html', context)


def signup(request):
    context = {}
    return render(request, 'account/signup.html', context)


def createUser(request):
    context = {}
    first_name = request.POST['firstName']
    last_name = request.POST['lastName']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    if User.objects.filter(email=email).exists():
        messages.warning(request, 'This Email already taken')
        return redirect('signup')
    else:
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'This username already taken,Please Choose another one')
            return redirect('signup')
        else:
            userRegistration = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                        email=email,
                                                        password=password)
            userRegistration.is_staff = False
            userRegistration.save()
            messages.info(request, 'Registration Confirmed')
    return render(request, 'account/login.html')


def updateProfile(request):
    address = request.POST['address']
    country = request.POST['country']
    city = request.POST['city']
    phone = request.POST['phone']

    userProfile.objects.filter(user=request.user).update(address=address, city=city,
                                                         country=country,
                                                         Phone=phone)

    # if request.method == 'POST':
    #     if profile.is_valid():
    #         profile.save()
    messages.info(request, 'Profile Updated ')
    return render(request, 'account/userprofile.html')


# def updateProfile(request):
#     profile = userProfile.objects.get(user=request.user)
#     form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
#     confirm = False
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             confirm = True
#
#     context = {
#         'profile': profile,
#         'form': form,
#         'confirm': confirm,
#     }
#
#     return render(request, 'account/userprofile.html', context)


def userprofile(request):
    context = {}
    return render(request, 'account/userprofile.html', context)


def userOrder(request):
    context = {}
    return render(request, 'account/userOrder.html', context)


def balance(request):
    context = {}
    return render(request, 'account/balance.html', context)


def chat(request):
    context = {}
    return render(request, 'account/chat.html', context)


@login_required(login_url='/login')
def cart(request):
    category = Categories.objects.all()  # Access User Session information
    cart = CartProducts.objects.filter(user=request.user)
    total = 0
    for rs in cart:
        if rs.item.discountPrice:
            total += rs.item.discountPrice * rs.quantity
        else:
            total += rs.item.price * rs.quantity
    context = {
        'cart': cart,
        'category': category,
        'total': total
    }
    return render(request, 'cart.html', context)


@login_required(login_url='/login')
def checkout(request):
    category = Categories.objects.all()  # Access User Session information
    userprofile = userProfile.objects.get(user=request.user)
    cart = CartProducts.objects.filter(user=request.user)
    total = 0
    for rs in cart:
        if rs.item.discountPrice:
            total += rs.item.discountPrice * rs.quantity
        else:
            total += rs.item.price * rs.quantity
    context = {
        'cart': cart,
        'category': category,
        'total': total,
        'userProfile': userprofile,
    }
    return render(request, 'checkout.html', context)


# class checkoutView(LoginRequiredMixin, View):
#     def get(self, *args, **kwargs):
#         try:
#             order = CartProducts.objects.get(user=self.request.user, isOrdered=False)
#             context = {
#                 'object': order
#             }
#             return render(self.request, 'checkout.html', context)
#         except ObjectDoesNotExist:
#             messages.error(self.request, "You do not have an active order")
#             return redirect("/")


#
#
# class CartView(LoginRequiredMixin, View):
#     def get(self, *args, **kwargs):
#         try:
#             order = CartProducts.objects.get(user=self.request.user, isOrdered=False)
#             context = {
#                 'object': order
#             }
#             return render(self.request, 'cart.html', context)
#         except ObjectDoesNotExist:
#             messages.error(self.request, "You do not have an active order")
#             return redirect("/")


# def cart(self, *args, **kwargs,):
#     order = Order.objects.get(user=self.request.user, isOrdered=False)
#     context = {
#         'object': order
#     }
#     return render(self.request, 'cart.html', context)


def orderTrack(request):
    context = {}
    return render(request, 'orderTrack.html', context)


def wishlist(request):
    context = {}
    return render(request, 'wishlist.html', context)


def becomeSeller(request):
    context = {}
    return render(request, 'becomeSeller.html', context)


def CategoryNav(request):
    context = {}
    category = Categories.objects.raw("SELECT * FROM core_categories")
    return render(request, 'sideNav.html', {"Categories": category})


def notFound(request, exception):
    return render(request, 'base/404.html')


# def shop(request):
#     context = {}
#     product = Products.objects.raw("SELECT * FROM core_products")
#     return render(request, 'shop.html', {"Products": product})


class shop(ListView):
    model = Products
    paginate_by = 16
    template_name = "shop.html"


class productDetail(DetailView):
    model = Products
    template_name = "productDetail.html"


class home(ListView):
    model = Products
    template_name = "home.html"


class CategoryView(View):
    def get(self, *args, **kwargs):
        category = Categories.objects.get(slug=self.kwargs['slug'])
        item = Products.objects.filter(category=category, isactive=True)
        context = {
            'object_list': item,
            'category_title': category.name,
            'category_description': category.description,
            'category_image': category.image
        }
        return render(self.request, "category.html", context)


class BrandView(View):
    def get(self, *args, **kwargs):
        brand = Brands.objects.get(slug=self.kwargs['slug'])
        item = Products.objects.filter(brand=brand, isactive=True)
        context = {
            'object_list': item,
            'Brand_title': brand.name,
            'Brand_description': brand.description,
            'Brand_image': brand.image
        }
        return render(self.request, "brand.html", context)


# def add_to_cart(request, slug):
#     item = get_object_or_404(Item, slug=slug)
#     order_item, created = OrderItem.objects.get_or_create(
#         item=item,
#         user=request.user,
#         ordered=False
#     )
#     order_qs = Order.objects.filter(user=request.user, ordered=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item.quantity += 1
#             order_item.save()
#             messages.info(request, "Item qty was updated.")
#             return redirect("core:order-summary")
#         else:
#             order.items.add(order_item)
#             messages.info(request, "Item was added to your cart.")
#             return redirect("core:order-summary")
#     else:
#         ordered_date = timezone.now()
#         order = Order.objects.create(
#             user=request.user, ordered_date=ordered_date)
#         order.items.add(order_item)
#         messages.info(request, "Item was added to your cart.")
#     return redirect("core:order-summary")

# @login_required(login_url='/login')
# def add_to_cart(request, slug):
#     item = get_object_or_404(Products, slug=slug)
#     order_item = CartProducts.objects.get_or_create(item=item, user=request.user, isOrdered=False)
#     order_qs = Order.objects.order_item(user=request.user, isOrdered=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         if order.items.filter(item_id=item).exists():
#             order_item.quantity += 1
#             order_item.save()
#             messages.info(request, "Item qty was updated.")
#             return redirect("core:cart")
#         else:
#             order.items.add(order_item)
#             messages.info(request, "Item was added to your cart.")
#             return redirect("core:cart")
#     else:
#         ordered_date = timezone.now()
#         order = Order.objects.create(
#             user=request.user, ordered_date=ordered_date)
#         order.items.add(order_item)
#         messages.info(request, "Item was added to your cart.")
#     return redirect("core:cart")

@login_required(login_url='/login')
def add_to_cart(request, slug):
    item = get_object_or_404(Products, slug=slug)
    checkItem = CartProducts.objects.filter(user=request.user, item=item)
    if checkItem:
        control = 1
    else:
        control = 0

    if control == 1:  # Update  shopcart
        data = CartProducts.objects.get(item=item, user=request.user)
        data.quantity += 1
        data.save()
        messages.info(request, "Quantity was updated.")
    else:
        data = CartProducts()
        data.user = request.user
        data.item = item
        data.quantity = 1
        data.isOrdered = False
        data.save()
        messages.info(request, "Item was added to your cart.")

    return redirect("core:cart")


@login_required(login_url='/login')
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Products, slug=slug)
    checkItem = CartProducts.objects.filter(user=request.user, item=item)
    if checkItem:
        control = 1
    else:
        control = 0

    if control == 1:  # Update  shopcart
        data = CartProducts.objects.get(item=item, user=request.user)
        data.quantity -= 1
        data.save()
        messages.info(request, "Quantity was updated.")

    return redirect("core:cart")


@login_required(login_url='/login')
def remove_from_cart(request, slug):
    item = get_object_or_404(Products, slug=slug)
    CartProducts.objects.filter(item=item).delete()
    messages.success(request, "Your item deleted form Cart.")
    return HttpResponseRedirect("/cart")
