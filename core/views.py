from django.shortcuts import render


# Create your views here.
def header(request):
    context = {}
    return render(request, 'header.html', context)


def footer(request):
    context = {}
    return render(request, 'footer.html', context)


def home(request):
    context = {}
    return render(request, 'home.html', context)


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


def shop(request):
    context = {}
    return render(request, 'shop.html', context)


def productDetail(request):
    context = {}
    return render(request, 'productDetail.html', context)


def notFound(request, exception):
    return render(request, 'base/404.html')
