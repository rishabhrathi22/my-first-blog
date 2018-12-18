from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
<<<<<<< HEAD
]
=======
]
>>>>>>> 88e2f9a237bcc89263266535a7788b5ba97f8623
