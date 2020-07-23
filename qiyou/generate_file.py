import generate
import generate_view
import numpy as np
import xlrd
def text_save(filename, data):    #filename为写入的文件的路径，data为要写入数据列表.
  file = open(filename,'a')
  for i in range(len(data)):
    s = str(data[i]).replace('[','').replace(']','')    #去除[]
    s = s.replace("'",'').replace(',','') +'\n'     #去除单引号，逗号，每行末尾追加换行符
    file.write(s)
  file.close()
  print("保存文件成功")
a = generate_view.generate_graph_view(100,1.8)[0]      #通过其生成各个文件（graph，address，graph_view,graph_calculate_view,address_view）
text_save("graph_calculate_view",a)
a = generate_view.generate_graph_view(100,1.8)[1]
text_save("graph_view",a)
a = generate_view.generate_graph_view(100,1.8)[2]
text_save("address_view",a)
a = generate.generate_graph(100)[0]
text_save("graph",a)
a = generate.generate_graph(100)[1]
text_save("address",a)
