from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about_us.html')


def checkout_cart(request):
    return render(request, 'checkout_complete.html')


def checkout_complete(request):
    return render(request, 'checkout_complete.html')


def checkout_info(request):
    return render(request, 'checkout_info.html')


def checkout_payment(request):
    return render(request, 'checkout_payment.html')


def contact(request):
    return render(request, 'contact_us.html')


def faq(request):
    return render(request, 'faq.html')


def index_fix_header(request):
    return render(request, 'index_fixed_header.html')


def my_account(request):
    return render(request, 'my_account.html')


def product_detail(request):
    return render(request, 'product_detail.html')


def product(request):
    return render(request, 'product.html')


def search(request):
    return render(request, 'index.html')


def index_inverse(request):
    return render(request, 'index_inverse_header.html')



