from django.urls import path

from .views import home,next

app_name = "user"

urlpatterns = [
    path('combi/', home, name='home'),
    path('next',next, name = 'next')

]
