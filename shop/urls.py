from django.conf.urls import url
from . import views

app_name="shop"

urlpatterns = [
    url(r'^$', views.product_list, name="product_list"),
    url(r'^results/$', views.search, name="search")
]