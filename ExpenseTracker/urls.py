"""ExpenseTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ExpenseTracker import views
from django.conf.urls import url





urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',views.login,name='login'),
    path('register/',views.register,name='db'),
    path('dashboard1/<int:user_id>',views.dash,name='display'),
    path('create/<int:user_id>',views.insert,name='insert'),
    path('index/<int:user_id>',views.show_expense,name='index'),
    path('login/',views.login,name='login'),
    path('edit/<int:id>',views.edit,name="edit"),
    path('Update/<int:id>',views.stupdate,name="stupdate"),
    path('Delete/<int:id>',views.stdel,name="stdel"),
    path('dashboard1/',views.logout,name="logout"),
    path('pie/<int:user_id>',views.piechart,name="piechart")

]
