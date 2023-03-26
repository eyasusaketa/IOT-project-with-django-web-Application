from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
  path('admin/', admin.site.urls),

  path('home/', views.default,name="moisture"),
  path('<int:day>/byday/', views.custom,name="custom"),
  #path('login/', include('home.urls')),


                ]
