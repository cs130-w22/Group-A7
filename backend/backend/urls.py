"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dinesmart import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('createUser/', views.create_user),
    path('login/', views.login),
    path('logout/', views.logout),
    path('authTest/', views.auth_test),
    path('getCurrentUser/', views.get_current_user),
    path('requestResetPassword/', views.request_password_reset),
    path('resetPassword/', views.reset_password),
    path('browseRestaurants/', views.browse_restaurants),
    path('addReview/', views.add_review),
    path('myReviews/', views.my_reviews),
    path('getUserProfile/', views.get_user_profile),
    path('getRestaurantReviews/', views.get_reviews_by_restaurant),
    path('getRestaurantById/', views.get_restaurant_by_id),

]
