from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^ipeen$',views.ipeen_list,name='ipeen_list'),
    url(r'^hr104$',views.hr104_list,name='hr104_list'),
    url(r'^human$',views.human_count_list,name='human_count_list'),
    url(r'^cost$',views.cost_power_list,name='cost_power_list'),
    url(r'^bus$',views.bus_list,name='bus_list'),
    url(r'^store$',views.store_list,name='store_list'),
    url(r'^get$',views.post_list,name='post_list'),#try
    url(r'^map$',views.Amap,name='map'),


    url(r'^input$',views.inputer,name='data_input'),
    url(r'^push$',views.push,name='data_push'),
    url(r'^wow$',views.wow,name='wow_list'),
    # url(r'^datawow$',views.dataWow,name='data_Wow'),
]