import numpy as np
#import generate

import xlrd
import qiyou.component as component
data = xlrd.open_workbook('/root/mysite/qiyou/三级行政区.xlsx')
table = data.sheet_by_index(0)
n = table.nrows

def change_distance(graph,distance,path,point,address,index):
    global n
    for i in range(0,n):
        if graph[point][i] != np.inf:
            if distance[i] != np.inf:
                if distance[point]+graph[point][i] < distance[i]:
                    distance[i] = distance[point]+graph[point][i]
                    path[i] = path[point]+"-"+address[i][0]
                    index[i] = str(index[point])+"-"+str(graph[i][point])
            else:
                distance[i] = distance[point]+graph[point][i]
                path[i] = path[point]+"-"+address[i][0]
                index[i] = str(index[point])+"-"+str(graph[i][point])

def shortest_path(src,dst):
    global n
    graph = component.readthefile("/root/mysite/qiyou/graph")   #读graph文件
    for i in range(0, n):
        for j in range(0, n):
            graph[i][j] = float(graph[i][j])
    address = component.readthefile("/root/mysite/qiyou/address")     #读address文件
    for i in range(0,n):            #找到src对应的序号
        if address[i][0] == src:
            src = i
    for i in range(0,n):            #找到dst对应得序号
        if address[i][0] == dst:
            dst = i
    index = [0 for i in range(n)]  # 定义存储路径距离
    path = [" " for i in range(n)]  # 定义path存储src到dst路径
    distance = [np.inf for i in range(n)]       #定义distance存储各个点到src得距离
    unsearch = [0 for i in range(n)]            #定义unsearch存储各个点是否需要搜索（0不需要，-1则需要）
    component.calculate_searchneed(unsearch,address,src,dst,1,1)   #通过计算得到大致需要搜索得点
    unsearch[src] = 0
    for i in range(0,n):                        #初始化distanc
        distance[i] = graph[src][i]
        if graph[src][i] != np.inf:
            path[i] = address[src][0]+"-"+address[i][0]
            index[i] = str(graph[src][i])
    pointx = np.inf
    while True:
        point = component.calculate_priority(unsearch,distance,dst)
        if point == pointx:
            break
        change_distance(graph,distance,path,point,address,index)
        pointx = point
    if distance[dst] == np.inf:         #如果未找到路径，扩大范围
        component.calculate_searchneed(unsearch, address, src, dst, 10, 5)
        pointx = np.inf
        while True:
            point = component.calculate_priority(unsearch, distance, dst)
            if point == pointx:
                break
            change_distance(graph, distance, path, point, address,index)
            pointx = point
    if distance[dst] != np.inf:
        date = component.generate_date(path[dst],index[dst])[0]
        x=component.generate_date(path[dst],index[dst])[1]

    else:
        date="不建议骑行到该地区"
    
    #print("总距离为：",distance[dst],"km")
    #print("路径为：",path[dst])
    #print(date)
    return (distance[dst],path[dst],date,x)
    
    #print("总距离为：",distance[dst],"km")
    #print("路径为：",path[dst])






