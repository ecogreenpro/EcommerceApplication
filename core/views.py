from django.contrib import messages, auth

from datetime import timezone

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
=======
from django.shortcuts import render, redirect
>>>>>>> f3e447b4f90c8244bb18fdf91df2836506304a43
from django.views.generic import ListView, DetailView, View
from .models import Products, CartProducts, Order

from .models import Products, Categories


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
    context = {}
    return render(request, 'account/logout.html', context)


def dashboard(request):
    context = {}
    return render(request, 'account/dashboard.html', context)


def forgotpassword(request):
    context = {}
    return render(request, 'account/forgotpassword.html', context)


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


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)


def cart(request):
    context = {}
    return render(request, 'cart.html', context)


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
    paginate_by = 4
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


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Products, slug=slug)
    order_item, created = CartProducts.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Item qty was updated.")
            return redirect("core:order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "Item was added to your cart.")
            return redirect("core:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item was added to your cart.")
    return redirect("core:order-summary")
