from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('',views.shp,name='shp'),
    path('ads',views.ads,name='ads'),
    path('intro',views.intro,name='intro'),
    path('reg',views.reg,name='reg'),
    path('create',views.create,name='create'),
    path('ord',views.ord,name='ord'),
    path('logout',views.logout,name='logout'),
    path('cart',views.cart,name='cart'),
    path('orders',views.orders,name='orders'),

    path('product_admin',views.product_admin,name='product_admin'),
    path('customer',views.customer,name='customer'),
    path('category',views.category,name='category'),
    path('checkout',views.checkout,name='checkout'),

    path('add_product',views.add_product,name='add_product'),
    path('add_category',views.add_category,name='add_category'),
    
    

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)