
from django.urls import path
from . views import *

urlpatterns = [
    path('', Home, name="index"),
    path('shop/', Shop, name="shop"),
    path('product_list/<int:category_id>', ProductList, name="product_list"),
    path('product-details/<int:pk>', ProductDetails, name="product-details"),
    path('about-us/', About, name="about"),
    path('packages/', Package, name="packages"),
    path('services/', AllServices, name="services"),
    path('single_services/<int:pk>', SingleServices, name="single_services"),
    path('single_service_details/<int:pk>', SingleServiceDetails, name="single_service_details"),
    path('design/', Design, name="design"),
    path('installation/', Installation, name="installation"),
    path('maintenance/', Maintenance, name="maintenance"),
    path('blog/', BlogView, name="blog"),
    path('blog-details/<int:pk>', BlogDetailsView, name="blog-details"),
    path('contact-us/', ContactUs, name="contact"),
    path('thanks/', Thanks, name="thanks"),

    path('admin-view/', AdminView, name="admin-view"),

    path('formItems/', formItems, name="formItems"),
    path('form_type_q/<int:pk>/', QFormType, name="form_type_q"),

    
]
  