from django.shortcuts import render


# Create your views here.
def vendorDashboard(request):
    context = {}
    return render(request, 'vendor/vendorDashboard.html', context)


def allProduct(request):
    context = {}
    return render(request, 'vendor/allProduct.html', context)


def addProduct(request):
    context = {}
    return render(request, 'vendor/addProduct.html', context)


def vendoerStockmanager(request):
    context = {}
    return render(request, 'vendor/vendoerStockmanager.html', context)


def vendoerOrderManager(request):
    context = {}
    return render(request, 'vendor/vendoerOrderManager.html', context)


def vendorReviewManager(request):
    context = {}
    return render(request, 'vendor/vendorReview.html', context)


def salesReport(request):
    context = {}
    return render(request, 'vendor/salesReport.html', context)


def topSelling(request):
    context = {}
    return render(request, 'vendor/topSelling.html', context)


def accountsReport(request):
    context = {}
    return render(request, 'vendor/accountsReport.html', context)
