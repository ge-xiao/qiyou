import xlrd
import numpy as np
import math
data = xlrd.open_workbook('/root/mysite/qiyou/三级行政区.xlsx')
table = data.sheet_by_index(0)
n = table.nrows
def calculate_difference(a,b,c,d,chy): #计算y=（（a-b）/（c-d））x+c
    e = a - b
    f = c - d
    g = f / e
    h = (chy - a) * g + c
    return h
def calculate_searchneed(unsearch,address,src,dst,x,y):   #通过经纬度是否属于平行四边形计算需要搜索的点，x为范围大小的参数
    global n
    for i in range(0,n):
        address[i][1] = float(address[i][1])
        address[i][2] = float(address[i][2])
    src_lng = address[src][1]
    src_lat = address[src][2]
    dst_lng = address[dst][1]
    dst_lat = address[dst][2] 
    if src_lng > dst_lng:
        test_lng = src_lng - dst_lng
    else:
        test_lng = dst_lng - src_lng
    if src_lat > dst_lat:
        test_lat = src_lat - dst_lat
    else:
        test_lat = dst_lat - src_lat
    if test_lat < 2 and test_lng < 2:
        for i in range(0,n):
            if src_lng-1.5 < address[i][1] < src_lng+1.5 and src_lat-1.5 < address[i][2] < src_lat+1.5:
                unsearch[i] = -1
            if dst_lng-1.5 < address[i][2] < dst_lng+1.5 and dst_lat-1.5 < address[i][2] < dst_lat+1.5:
                unsearch[i] = -1
    else:
        if test_lat > test_lng:
            if src_lat > dst_lat:
                for i in range(0,n):
                    if dst_lat-y < address[i][2] < src_lat+y:
                        dif = calculate_difference(src_lat,dst_lat,src_lng,dst_lng,address[i][2])
                        if dif-x < address[i][1] < dif+x:
                            unsearch[i] = -1
            else:
                for i in range(0,n):
                    if src_lat-y < address[i][2] < dst_lat+y:
                        dif = calculate_difference(dst_lat,src_lat,dst_lng,src_lng,address[i][2])
                        if dif-x < address[i][1] < dif+x:
                            unsearch[i] = -1
        else:
            if src_lng > dst_lng:
                for i in range(0,n):
                    if dst_lng-y < address[i][1] < src_lng+y:
                        dif = calculate_difference(src_lng,dst_lng,src_lat,dst_lat,address[i][1])
                        if dif-x < address[i][2] < dif+x:
                            unsearch[i] = -1
            else:
                for i in range(0,n):
                    if src_lng-y < address[i][1] < dst_lng+y:
                        dif = calculate_difference(dst_lng,src_lng,dst_lat,src_lat,address[i][1])
                        if dif-x < address[i][2] < dif+x:
                            unsearch[i] = -1

'''                            
def calculate_priority(unsearch,distance,dst):          #计算搜索优先级，与src距离越小优先级越高
    global n
    point = 0
    p = np.inf
    for i in range(0,n):
        if unsearch[i] != 0:
                if distance[i] < p:
                    if distance[i] > distance[dst]:
                        unsearch[i] = 0
                    else:
                        point = i
                        p = distance[i]
    unsearch[point] = 0
    return point
'''

def calculate_priority(unsearch,distance,dst):          #计算搜索优先级，与src距离越小优先级越高
    global n
    point = 0
    p = np.inf
    for i in range(0,n):
        if unsearch[i] != 0:
                if distance[i] < np.inf:
                    if distance[i] > distance[dst]:
                        unsearch[i] = 0
                    else:
                        if distance[i] < p:
                            point = i
                            p = distance[i]
    unsearch[point] = 0
    return point



def readthefile(location):             #读文件，location为文件路径，zzcq为读出内容
    file = open(location, mode='r')
    zzcq = []
    contents = file.readlines()
    for msg in contents:
        msg = msg.strip('\n')
        adm = msg.split(' ')
        zzcq.append(adm)
    file.close()
    return zzcq

def generate_date(pathall,indexall):
    path = pathall.split("-")
    index = indexall.split("-")
    n = len(index)
    for i in range(0,n):
        index[i] = float(index[i])
        index[i] = round(index[i],2)
    date = ""
    T = False
    x = 1
    for i in range(0,n-1):
        if T == True:
            T = False
            continue
        else:
            if index[i]+index[i+1] < 100:
                date = date + "第"+str(x)+"天:"+path[i]+"--->"+path[i+1]+"--->"+path[i+2]+" 距离为："+str(index[i]+index[i+1])+"km"+"\n"
                x = x+1
                T = True
            else:
                if index[i] <= 100:
                    date = date + "第"+str(x)+"天:"+path[i]+"--->"+path[i+1]+" 距离为："+str(index[i])+"km"+"\n"
                    x = x+1
                if index[i] > 100:
                    dex = math.ceil(index[i]/100) - 1
                    for j in range(dex):
                        date = date + "第" + str(x) + "天:" + path[i] + "--->" + path[i + 1] + " 距离为：" + str(100)+"km" + "\n"
                        x = x+1
                    date = date + "第" + str(x) + "天:" + path[i] + "--->" + path[i + 1] + " 距离为：" + str(round(index[i]%100,2))+"km" + "\n"
    if T == False:
        i = n-1
        if index[i] <= 100:
            date = date + "第" + str(x) + "天:" + path[i] + "--->" + path[i + 1] + " 距离为：" + str(index[i])+"km" + "\n"
        if index[i] > 100:
            dex = math.ceil(index[i] / 100)
            for j in range(dex - 1):
                date = date + "第" + str(x) + "天:" + path[i] + "--->" + path[i + 1] + " 距离为：" + str(100)+"km" + "\n"
                x = x + 1
            date = date + "第" + str(x) + "天:" + path[i] + "--->" + path[i + 1] + " 距离为：" + str(round(index[i] % 100,2))+"km" + "\n"
    return (date,x)






