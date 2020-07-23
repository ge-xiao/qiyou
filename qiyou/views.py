from django.shortcuts import render
from django.http import HttpResponse
from qiyou.models import *
import qiyou.viewpath as viewpath
import qiyou.shortpath as shortpath
from qiyou.GraphicsGenerator import GraphicsGenerator


import json

def index(request):

    #print(request.method)
    #print(request.body)
    
    result=request.body.decode(encoding = "utf-8")
    result=json.loads(result)
    print(result)

    user_info=result['user_info']
    user_request_type=result['user_request_type']

    if user_request_type['type_name']== 'login':

        user_objects=user.objects.filter(name=user_info['name']).filter(password=user_info['passwd'])
        
        if user_objects.count()==0:
            
            print("账户或密码错误")
            return HttpResponse("账户或密码错误")
        else:
            user_object=user_objects[0]
            print("登录成功")
            return HttpResponse("登录成功")


    if user_request_type['type_name']== 'register':
        user_objects=user.objects.filter(name=user_info['name'])

        if user_objects.count()==1:
            
            print("账户已存在")
            return HttpResponse("账户已存在")

        else :
            user.objects.create(name=user_info['name'],password=user_info['passwd'])    
            print("注册成功")
            
            return HttpResponse("注册成功")

    if user_request_type['type_name']== 'view_path':
        client_path_str=result['user_data']
        client_path=client_path_str.split("-")
        #print(client_path)
        (distance,server_path,date)=viewpath.shortest_path(client_path[0],client_path[1])


        print (distance)
        print(server_path)
        print(date)

        if server_path ==' ':
            return HttpResponse("不建议骑行")
        else:
            graphicsGenerator=GraphicsGenerator('view')
            graphicsGenerator.create_graphics(server_path)
            if data.objects.filter(user_name=user_info['name']).filter(user_path=client_path_str).filter(category='view').count() ==0:

                data.objects.get_or_create(user_name=user_info['name'],user_path=client_path_str,category='view',user_route=date,user_save='n')
            return HttpResponse('总路程:'+'{:.2f}'.format(distance)+'km'+'\n'+client_path[0]+'-'+client_path[1]+'\n'+date)


        #print(dis_part)
        '''
        route=''
        
        if server_path[0]!=' ':

            graphicsGenerator=GraphicsGenerator('view')
            graphicsGenerator.create_graphics(server_path)
            

            server_path_list=server_path.split('-')
            
            return_list=[]
            i=0
            n=len(dis_part)
            while i<n:
                temp=0
                for k in range(i,n):
                    temp=temp+dis_part[k]
                    if temp>=100 :
                        break

                if temp<100:
                    str_temp=''
                    for j in range(i,k+1):
                        str_temp=str_temp+server_path_list[j]+'--->'
                    str_temp=str_temp+server_path_list[k+1]
                    str_temp=str_temp+'-全长'+'{:.2f}'.format(temp)+'km'
                    #print(str_temp)
                    return_list.append(str_temp)
                    #print(1)
                    break
                
                str_temp=''
                for j in range(i,k):
                    str_temp=str_temp+server_path_list[j]+'--->'
                str_temp=str_temp+server_path_list[k]

                str_temp=str_temp+'-全长'+'{:.2f}'.format(temp-dis_part[k])+'km'
                #print(str_temp)
                return_list.append(str_temp)
                i=k
            
            #print(return_list)
            for i in range(len(return_list)-1):
                route=route+'第'+str(i+1)+'天:'+return_list[i]+'\n'
            
            route=route+'第'+str(len(return_list))+'天:'+return_list[len(return_list)-1]
            print(route)
            #print(route)
            if data.objects.filter(user_name=user_info['name']).filter(user_path=client_path_str).filter(category='view').count() ==0:

                data.objects.get_or_create(user_name=user_info['name'],user_path=client_path_str,category='view',user_route=route,user_save='n')
            

            return HttpResponse(client_path[0]+'-'+client_path[1]+'\n'+route)
        else:
            return HttpResponse("不建议骑行")
        '''


    if user_request_type['type_name']== 'short_path':
        client_path_str=result['user_data']
        client_path=client_path_str.split("-")
        #print(client_path)
        (distance,server_path,date)=shortpath.shortest_path(client_path[0],client_path[1])
        

        print (distance)
        print(server_path)
        print(date)
    
        if server_path ==" ":
            return HttpResponse("不建议骑行")
        else:
            graphicsGenerator=GraphicsGenerator('short')
            graphicsGenerator.create_graphics(server_path)
            if data.objects.filter(user_name=user_info['name']).filter(user_path=client_path_str).filter(category='short').count() ==0:

                data.objects.get_or_create(user_name=user_info['name'],user_path=client_path_str,category='short',user_route=date,user_save='n')
            return HttpResponse('总路程:'+'{:.2f}'.format(distance)+'km'+'\n'+client_path[0]+'-'+client_path[1]+'\n'+date)



        '''
        route=''

        if server_path[0]!=' ':
            graphicsGenerator=GraphicsGenerator('short')
            graphicsGenerator.create_graphics(server_path)
            #print(dis_part)
        
            server_path_list=server_path.split('-')
            for i in range(len(dis_part)-1):
                route=route+"骑行第"+str(i+1)+'天:'+server_path_list[i]+'--->'+server_path_list[i+1]+'-'+"全长:" +'{:.2f}'.format(dis_part[i])+'km'+'\n'

            n=len(dis_part)-1
            route=route+"骑行第"+str(n+1)+'天:'+server_path_list[n]+'--->'+server_path_list[n+1]+'-'+"全长:" +'{:.2f}'.format(dis_part[n])+'km'
            print(route)


            if data.objects.filter(user_name=user_info['name']).filter(user_path=client_path_str).filter(category='short').count() ==0:

                data.objects.get_or_create(user_name=user_info['name'],user_path=client_path_str,category='short',user_route=route,user_save='n')
        
            return HttpResponse(client_path[0]+'-'+client_path[1]+'\n'+route)
        else:
            return HttpResponse("不建议骑行")
        '''
    if user_request_type['type_name']== 'save':
        data_str=result['user_data']
        data_str=data_str.split('+')
        u_path=data_str[0]
        u_category=data_str[1]
        
        print(user_info['name'])
        print(u_path)
        print(u_category)
        data.objects.filter(user_name=user_info['name']).filter(user_path=u_path).filter(category=u_category).update(user_save='y')
        return HttpResponse("保存成功") 

    if user_request_type['type_name']== 'delete':
        data_str=result['user_data']
        data_str=data_str.split('+')
        u_path=data_str[0]
        u_category=data_str[1]
        
        print(user_info['name'])
        print(u_path)
        print(u_category)
        data.objects.filter(user_name=user_info['name']).filter(user_path=u_path).filter(category=u_category).update(user_save='n')
        return HttpResponse("删除成功")
    






    if user_request_type['type_name']== 'user_get':

        obj=data.objects.filter(user_name=user_info['name']).filter(user_save='y')
        print(obj.count())

        temp={}
        temp['data']=[]
        #print(temp)
        if obj.count()!=0:

            for i in range(obj.count()):

                dic={}
                dic['user_path']=obj[i].user_path
                dic['category']=obj[i].category
                dic['user_route']=obj[i].user_route
                temp['data'].append(dic)
                #temp=temp+obj[i].user_path+',,,'+obj[i].category+',,,'+obj[i].user_route+'==='
            #n=obj.count()-1
            #temp=temp+obj[n].user_path+',,,'+obj[n].category+',,,'+obj[n].user_route
            
        json1 = json.dumps(temp,ensure_ascii=False)
        #print(type(json1))

        return HttpResponse(json1)

    if user_request_type['type_name']== 'hot_get':
        objects=hot_route.objects.all()
        print(objects.count())
        temp=''
        if objects.count()!=0:
            for i in range(objects.count()-1):
                route_name=objects[i].route_name
                day_consume=objects[i].day_consume
                schedule=objects[i].schedule
                scenery=objects[i].scenery
                temp=temp+route_name+',,,'+day_consume+',,,'+schedule+',,,'+scenery+',,,'
            n=objects.count()-1
            temp=temp+objects[n].route_name+',,,'+objects[n].day_consume+',,,'+objects[n].schedule+',,,'+objects[n].scenery
        #print(temp)
        return HttpResponse(temp)


    if user_request_type['type_name']== 'city_get':

        data_str=result['user_data']
        objects=city_route.objects.filter(city_name=data_str)
        print(objects.count())
        temp=''
        if objects.count()!=0:
            for i in range(objects.count()-1):
                city_name=objects[i].city_name
                route_name=objects[i].route_name
                distance=objects[i].distance
                path=objects[i].path
                link=objects[i].link
                route_landscape=objects[i].route_landscape
                temp=temp+city_name+',,,'+route_name+',,,'+distance+',,,'+path+',,,'+link+',,,'+route_landscape+'==='
            n=objects.count()-1
            temp=temp+objects[n].city_name+',,,'+objects[n].route_name+',,,'+objects[n].distance+',,,'+objects[n].path+',,,'+objects[n].link+',,,'+objects[n].route_landscape
            #print(temp)
        
        return HttpResponse(temp)





def view_path(request):

    #user_data.objects.create(name='me',data='aa')
    #user_data.objects.create(name='me',data='bb')
    #print(user_data.objects.filter(name='me').count())
    #objects=city_route.objects.filter(city_name='上海')
    objects=city_route.objects.all()
    print(objects.count())
    str_temp=''
    city_name=objects[1].city_name
    route_name=objects[1].route_name
    distance=objects[1].distance
    path=objects[1].path
    link=objects[1].link
    route_landscape=objects[1].route_landscape
    str_temp=city_name+route_name+distance+path+link+route_landscape
    return HttpResponse(str_temp)
    



def short_path(request):
    objects=hot_route.objects.all()
    print(objects.count())
    temp=''
    route_name=objects[0].route_name
    day_consume=objects[0].day_consume
    schedule=objects[0].schedule
    scenery=objects[0].scenery
    temp=temp+route_name+day_consume+schedule+scenery
    #user.objects.create(name='rss',password='d')  
    #objects=data.objects.all()
    #print(objects.count())  
    return HttpResponse(temp)
    