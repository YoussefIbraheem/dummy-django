
from django.contrib import admin
from django.urls import path , include
import app.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(app.urls)),
]
