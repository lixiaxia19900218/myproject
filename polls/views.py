from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

dbs =[]
dbs1 =[]

def index(response):
    return HttpResponse("hello world,lixiaxia")

#获取
@csrf_exempt
def add(request):
    # 1. 获取参数 GET请求
    #if request.method == 'GET':
        name = request.GET.get("name")
        if name  == 'tang':
            return HttpResponse('I LOVE YOU ')
        

        age = request.GET.get("age")
        if age == "0"  and  name == 'lying':
            return HttpResponse("错误的信息年龄，怕是在娘胎里吧！！！")

        # 2. 存 todo
        
        if name in dbs:
            if 'None' in dbs:
                dbs.remove()
        else:
            dbs.append(name)
        if age in dbs1:
            if 'None' in dbs1:
                dbs.remove()
        else:
            dbs1.append(age)
        print('dbs+++++++++++++++++++++',dbs)
        print('dbs1++++++++++++++++++++',dbs1)
        print('len(dbs)+++++++++++++++++++',len(dbs))
        print('len(dbs1)++++++++++++++++++++++',len(dbs1))
        # 3.返回数据
        
        #return JsonResponse
        return HttpResponse("your info: %s %s"%(dbs,dbs1))
    
    #elif request.method == 'POST':
    #    pass



 
def get(request):
     pass
