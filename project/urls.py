from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='signup/', permanent=True)),
    path('signup/', include('signup_app.urls')),
    path('login/', include('login_app.urls')),
    path('todoapp/', include('todo_app.urls')),
]
