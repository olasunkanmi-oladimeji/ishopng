from core import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


app_name='core'

urlpatterns = [
    
    path('',views.homepage,name='home'),
    path('About-us',views.aboutpage,name='about'),
    path('Contact-us',views.contactpage,name='contact'),
    path('wishlist',views.wishlist,name='wish'),
    path('product/<slug>/',views.ProductPage,name='product'),
    #cart function
    path('order-summary',views.ordersummary.as_view(),name='order-summary'),
    path('Add-To-cart/<slug>',views.add_to_cart,name='add_to_cart'),
    path('Remove-FROM-cart/<slug>',views.remove_from_cart,name='remove_from_cart'),
    path('Remove-Item-cart/<slug>',views.remove_single_item_from_cart,name='remove_item_cart'),
    #checkout
    path('checkout',views.checkout.as_view(),name='checkout'),
    path('payment/<payment_option>',views.Paymentview.as_view(),name='payment'),
    path('payment/verify/<id>',views.verify,name='verify'),
    path('add-coupon/', views.AddCouponView.as_view(), name='add-coupon'),
    path('request-refund/',views.RequestRefundView.as_view(), name='request-refund'),
    #filter functions
    path('search/',views.search,name='search'),
    path('product-category/<slug:category_slug>',views.category,name='category'),
    path('product-subcatgory/<slug:subcategory_slug>/',views.subcategory,name='subcategory'),
    path('product-brands/<slug:brand_slug>/',views.Brandeds,name='brands'),
    path('filter/price/',views.price,name='price'),
    path('filter/product-instock/',views.instock,name='instock'),
]


if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)