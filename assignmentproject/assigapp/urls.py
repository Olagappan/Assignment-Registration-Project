from django.urls import path

from assigapp import views

urlpatterns = [
    # path('',views.login,name='log'),
    # path('logdata',views.log_data),
    path('',views.register,name='reg'),
    path('aregdata',views.reg_data),
]