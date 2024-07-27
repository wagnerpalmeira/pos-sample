from django.contrib import admin
from django.urls import path, include
from promotions.views import promotions_view, create_promotion_view

urlpatterns = [
    path('promotions/', promotions_view, name='promotions_view'),
    path('promotions/register/', create_promotion_view, name='create_promotion'),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
]
