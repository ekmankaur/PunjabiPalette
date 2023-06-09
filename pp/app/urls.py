from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path



urlpatterns = [
    path('', views.home, name='home'),
    path("aboutus/", views.aboutus,name="aboutus"),
    path("contactus/", views.contactus,name="contactus"),
    path('signup/', views.Signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/home.html'), name='logout'),
    path("category/<slug:val>", views.Category.as_view(),name="category"),
    path("productpage/<int:pk>", views.ProductPage.as_view(),name="productpage"),
    path("profile/", views.Profile.as_view(),name="profile"),
    path("addtocart/", views.addtocard, name="addtocart"),
    path('removefromcart/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.display_cart, name='cart'),
    path('placeorder/', views.placeorder, name='placeorder'),
    path('afterorder/', views.afterorder, name='afterorder'),
    path('orders/', views.orders, name='orders'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
