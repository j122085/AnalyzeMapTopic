from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^ipeen$',views.ipeen_list,name='ipeen_list'),
    url(r'^hr104$',views.hr104_list,name='hr104_list'),
    url(r'^human$',views.human_count_list,name='human_count_list'),
    url(r'^cost$',views.cost_power_list,name='cost_power_list'),
    url(r'^get$',views.post_list,name='post_list'),
    url(r'^map$',views.Amap,name='map'),
]