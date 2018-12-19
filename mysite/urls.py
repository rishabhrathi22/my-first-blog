from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
<<<<<<< HEAD
]
=======
]
>>>>>>> 0f8e60a2bcf1775c200795998d014efdc7acc074
