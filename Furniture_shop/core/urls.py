from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from .views import homepage, shop, signup, login_old
from product.views import product
from cart.views import add_to_cart

urlpatterns = [
    path('',homepage, name='homepage'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('signup/', signup, name='signup'),
    path('login/', login_old, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)