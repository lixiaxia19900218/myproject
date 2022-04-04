from django.urls import path

from . import views

'''
1. 根据参数返回数据
2.



1. 增加姓名 POST
2. 查询姓名 GET

'''





urlpatterns = [
    path('', views.index,name = 'index'),
    
    # 新增数据
    path('add', views.add,name ='add'),

    # 查询数据  name=xixia,返回 "xiaxia年龄是:"

    # 删除数据  name=xiaxia,返回删除成功


    # 改数据 name=xiaxia,age=20(原先是10)，返回更新成功
    
   
]