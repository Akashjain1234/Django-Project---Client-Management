from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', home_page),
    path('add/', add_page),
    path('display/', display_page),
    path('update/<int:id>/', update_page),
    path('delete/<int:id>/', delete_page),
    path('signup/', Signup_page),
    path('login/', login_page),
    path('logout/', logout_page),
    path('project/<int:id>/', project_page),
    path('clientinfo/<int:id>/', clientinfo_page),
    path('displaypro/', displaypro_page),
    path('userinfo/', userinfo_page),
    path('delsuccess/', delsuccess_page),
    path('deletepro/<int:id>/', deletepro_page),




]
 