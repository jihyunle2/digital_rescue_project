
from django.contrib import admin
from django.urls import path
import digital_rescue.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', digital_rescue.views.home, name='home'),
]
