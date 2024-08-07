from django.urls import path
from .views import main
from .views import about
from .views import checkout_cart
from .views import checkout_complete
from .views import checkout_payment
from .views import contact
from .views import checkout_info
from .views import faq
from .views import index_fix_header
from .views import my_account
from .views import product_detail
from .views import product
from .views import search
from .views import index_inverse

urlpatterns = [
    path('', main),
    path('about/', about),
    path('cart/', checkout_cart),
    path('cartcomplete/', checkout_complete),
    path('checkout/', checkout_payment),
    path('checkoutinfo/', checkout_info),
    path('contact/', contact),
    path('faq/', faq),
    path('index/', index_fix_header),
    path('myaccount/', my_account),
    path('productdetail/', product_detail),
    path('product/', product),
    path('search/', search),
    path('index_inverse/', index_inverse),

]



