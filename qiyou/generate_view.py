from math import sin, asin, cos, radians, fabs, sqrt, atan, pi
import numpy as np
import xlrd
EARTH_RADIUS = 6371  # 地球平均半径，6371km
def hav(theta):
    s = sin(theta / 2)
    return s * s
def get_distance_hav(lat0, lng0, lat1, lng1):   #计算两点距离
    "用haversine公式计算球面两点间的距离。"
    # 经纬度转换成弧度
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)
    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))
    return distance
def generate_graph_view(x,y):      #生成graph，graph_calculate,address,x为景点占权重的参数（0到1景点少优先，1到景点多优先）
    data = xlrd.open_workbook('/root/mysite/qiyou/三级行政区景点.xls')   #读excel
    table = data.sheet_by_index(0)
    n = table.nrows
    address = [[0 for i in range(3)]for i in range(n)]
    graph = [[np.inf for i in range(n)]for i in range(n)]
    graph_view = [[np.inf for i in range(n)]for i in range(n)]
    for i in range(0,n):
        for j in range(0,3):
            address[i][j] = table.cell(i,j).value
    for i in range(0,n):
        lng1, lat1 = (address[i][1],address[i][2])
        for j in range(0,n):
            lng2, lat2 = (address[j][1],address[j][2])
            dist = get_distance_hav(lat1,lng1,lat2,lng2)
            change_point = table.cell(i,3).value + table.cell(j,3).value
            change_value = 1 - (atan(change_point/20)/pi) * y
            dist_view = dist * change_value
            if i != j:
                if i == 945 and j == 2176 or j == 945 and i == 2176:
                    graph[i][j] = dist
                    graph_view[i][j] = dist_view
                else:
                    if 940 < i < 1022 or 940 < j < 1022:
                        if dist < 220:
                            graph[i][j] = dist
                            graph_view[i][j] = dist_view
                    else:
                        if 1830 < i < 1902 or 1830 < j < 1902:
                            if dist < 220:
                                graph[i][j] = dist
                                graph_view[i][j] = dist_view
                        else:
                            if 2141 < i < 2180 or 2141 < j < 2180:
                                if dist < 220:
                                    graph[i][j] = dist
                                    graph_view[i][j] = dist_view
                            else:
                                if dist < x:
                                    graph[i][j] = dist
                                    graph_view[i][j] = dist_view
            else:
                graph[i][j] = 0
                graph_view[i][j] = 0
    return (graph,graph_view,address)
