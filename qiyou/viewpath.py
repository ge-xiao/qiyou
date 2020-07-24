import numpy as np
#import generate_view
import xlrd
#import search_view
import qiyou.component as component
data = xlrd.open_workbook('/root/mysite/qiyou/三级行政区景点.xls')
table = data.sheet_by_index(0)
n = table.nrows
def change_distance(graph,distance,path,point,address,graph_calculate,distance_calculate,index) :
    global n
    for i in range(0,n):
        if graph[point][i] != np.inf:
            if distance[i] != np.inf:
                if distance[point]+graph[point][i] < distance[i]:
                    distance[i] = distance[point]+graph[point][i]
                    distance_calculate[i] = distance_calculate[point]+graph_calculate[point][i]
                    path[i] = path[point]+"-"+address[i][0]
                    index[i] = str(index[point]) + "-" + str(graph_calculate[i][point])
            else:
                distance[i] = distance[point]+graph[point][i]
                distance_calculate[i] = distance_calculate[point]+graph_calculate[point][i]
                path[i] = path[point]+"-"+address[i][0]
                index[i] = str(index[point]) + "-" + str(graph_calculate[i][point])

def view_path(src,dst):
    global n
    graph_calculate = component.readthefile("/root/mysite/qiyou/graph_calculate_view") #读文件
    for i in range(0, n):
        for j in range(0, n):
            graph_calculate[i][j] = float(graph_calculate[i][j])
    graph = component.readthefile("/root/mysite/qiyou/graph_view")
    for i in range(0, n):
        for j in range(0, n):
            graph[i][j] = float(graph[i][j])
    address = component.readthefile("/root/mysite/qiyou/address_view")
    for i in range(0,n):                #找到src和dst对应得编号
        if address[i][0] == src:
            src = i
    for i in range(0,n):
        if address[i][0] == dst:
            dst = i
    index = [0 for i in range(n)]       #定义存储路径距离
    path = [" " for i in range(n)]      #定义path存储路径
    distance = [np.inf for i in range(n)]       #定义distance存储到src带view权值得最短距离
    distance_calculate = [np.inf for i in range(n)]         #定义distance_calculate存储到src的实际最短距离
    unsearch = [0 for i in range(n)]         #定义unsearch存储需要搜索得点（0不需要，-1需要）
    component.calculate_searchneed(unsearch,address,src,dst,3,4)    #计算需要搜索的点
    unsearch[src] = 0
    count = 0
    for i in range(0,n):                #初始化distance
        distance[i] = graph[src][i]
        distance_calculate[i] = graph_calculate[src][i]
        if graph[src][i] != np.inf:
            path[i] = address[src][0]+"-"+address[i][0]
            index[i] = str(graph_calculate[src][i])
    pointx = np.inf
    while True:
        point = component.calculate_priority(unsearch,distance,dst)
        if point == pointx:
            break
        change_distance(graph,distance,path,point,address,graph_calculate,distance_calculate,index)
        pointx = point
    if distance[dst] == np.inf:
        component.calculate_searchneed(unsearch, address, src, dst, 10, 5)
        pointx = np.inf
        while True:
            point = component.calculate_priority(unsearch, distance, dst)
            if point == pointx:
                break
            change_distance(graph, distance, path, point, address, graph_calculate, distance_calculate,index)
            pointx = point      
    if distance_calculate[dst] != np.inf:
        date = component.generate_date(path[dst],index[dst])[0]
        #print("总距离为：",distance[dst],"km")
        #print("路径为：",path[dst])
        #print(date)
        x=component.generate_date(path[dst],index[dst])[1]
    else:
        date="不建议骑行到该地区"
    #print("总距离为：",distance[dst],"km")
    #print("路径为：",path[dst])
    #print(date)
    return (distance_calculate[dst],path[dst],date,x)