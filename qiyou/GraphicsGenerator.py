from PIL import Image, ImageDraw,ImageFont

class GraphicsGenerator:
    def __init__(self,category,width=400,height=400):
        self.width = width*3
        self.height = height*3
        self.length = 10
        self.lng=[]
        self.lat=[]
        self.name=[]
        self.n=10
        self.info=dict()
        self.category=category

    def create_graphics(self,s):
        #文件读取
        f=open('./qiyou/data.txt','r')
        count=0
        for line in f:
            l=line.split(' ')
            #self.name.append(l[0])
            #self.lng.append(float(l[1]))
            #self.lat.append(float(l[2]))
            self.info[l[0]]=(float(l[1]),float(l[2]))
            #if count==self.n-1:
            #    break
            count+=1
        self.n=count
        #print(count)
        #参数配置
        route_list=s.split('-')
        #print(route_list)
        count=0
        for i in route_list:
            self.name.append(i)
            self.lng.append(self.info[i][0])
            self.lat.append(self.info[i][1])
            count+=1
        min_x=self.lng[0]
        max_x=self.lng[0]
        min_y=self.lat[0]
        max_y=self.lat[0]
        for i in range(count):
            if self.lng[i]>max_x:
                max_x=self.lng[i]
            if self.lng[i]<min_x:
                min_x=self.lng[i]
            if self.lat[i]>max_y:
                max_y=self.lat[i]
            if self.lat[i]<min_y:
                min_y=self.lat[i]
        #print(min_x,max_x,min_y,max_y)

        #print(coefficient_x,coefficient_y)
        compensate_x=0.05*self.width
        compensate_y=0.1*self.height

        if (max_x-min_x)<(max_y-min_y):
            #coefficient_x=self.width/(max_x-min_x)
            coefficient_y=self.height/(max_y-min_y)
            coefficient_x=coefficient_y
            if (max_x-min_x)/(max_y-min_y)<0.5:
                compensate_x+=(0.5-(max_x-min_x)/(max_y-min_y))*self.width
        else:
            coefficient_x=self.width/(max_x-min_x)
            coefficient_y=coefficient_x 
            if (max_y-min_y)/(max_x-min_x)<0.5:
                compensate_y+=(0.5-(max_y-min_y)/(max_x-min_x))*self.height
        #画图模块

        route_graph = Image.new('RGB',(int(self.width*1.2),int(self.height*1.2)),(255,255,255))
        draw=ImageDraw.Draw(route_graph)
        font=ImageFont.truetype('./qiyou/msyh.ttc',30,encoding='utf-8')
        r=10
        for i in range(count-1):
            #print(self.name[i],self.lng[i],self.lat[i],'\n')
            draw.line(((self.lng[i]-min_x)*coefficient_x+compensate_x,self.height*1.2-(self.lat[i]-min_y)*coefficient_y-compensate_y,(self.lng[i+1]-min_x)*coefficient_x+compensate_x,self.height*1.2-(self.lat[i+1]-min_y)*coefficient_y-compensate_y),'red')
            draw.ellipse(((self.lng[i]-min_x)*coefficient_x+compensate_x-r,self.height*1.2-(self.lat[i]-min_y)*coefficient_y-compensate_y-r,(self.lng[i]-min_x)*coefficient_x+compensate_x+r,self.height*1.2-(self.lat[i]-min_y)*coefficient_y-compensate_y+r),'red')
            #print((self.lng[i]-min_x)*coefficient_x+compensate_x-r,self.height*1.2-(self.lat[i]-min_y)*coefficient_y-compensate_y+r)
            draw.text(((self.lng[i]-min_x)*coefficient_x+compensate_x,self.height*1.2-(self.lat[i]-min_y)*coefficient_y-compensate_y),self.name[i],'black',font=font)
            #draw.line(((self.lng[i]-min_x)*coefficient_x+compensate_x,(self.lat[i]-min_y)*coefficient_y+compensate_y,(self.lng[i+1]-min_x)*coefficient_x+compensate_x,(self.lat[i+1]-min_y)*coefficient_y+compensate_y),'red')
            #draw.ellipse(((self.lng[i]-min_x)*coefficient_x+compensate_x-r,(self.lat[i]-min_y)*coefficient_y+compensate_y-r,(self.lng[i]-min_x)*coefficient_x+compensate_x+r,(self.lat[i]-min_y)*coefficient_y+compensate_y+r),'red')
            #draw.text(((self.lng[i]-min_x)*coefficient_x+compensate_x,(self.lat[i]-min_y)*coefficient_y+compensate_y),self.name[i],'black',font=font)
        draw.ellipse(((self.lng[count-1]-min_x)*coefficient_x+compensate_x-r,self.height*1.2-(self.lat[count-1]-min_y)*coefficient_y-compensate_y-r,(self.lng[count-1]-min_x)*coefficient_x+compensate_x+r,self.height*1.2-(self.lat[count-1]-min_y)*coefficient_y-compensate_y+r),'red')
        draw.text(((self.lng[count-1]-min_x)*coefficient_x+compensate_x,self.height*1.2-(self.lat[count-1]-min_y)*coefficient_y-compensate_y),self.name[count-1],'black',font=font)
        
        if self.category=='short':
            image_name='image/'+str(route_list[0])+'-'+str(route_list[-1])+'_short'+'.png'
        else:
            image_name='image/'+str(route_list[0])+'-'+str(route_list[-1])+'_view'+'.png'
        #print(image_name)
        route_graph.resize((self.width,self.height),Image.ANTIALIAS)
        route_graph.save('./qiyou/'+image_name, "PNG")
        return image_name

'''

def main():
    s="黑龙江哈尔滨-黑龙江双城-吉林榆树-吉林德惠-吉林长春-吉林怀德-吉林四平-辽宁康平-辽宁新民-辽宁阜新-辽宁北票-辽宁朝阳-内蒙古宁城-河北平泉-河北宽城-河北兴隆-河北三河-河北廊坊-河北大城-河北南皮-山东商河-山东长清-山东平阴-山东嘉祥-山东金乡-河南夏邑-安徽涡阳-安徽利辛-安徽霍丘-安徽六安-安徽岳西-安徽太湖-江西湖口-江西都昌-江西南昌-江西进贤-江西南城-福建建宁-福建宁化-江西瑞金-江西会昌-江西安远-江西龙南-广东翁源-广东佛岗-广东广州"
    graphicsGenerator=GraphicsGenerator()
    graphicsGenerator.create_graphics(s)

if __name__ == "__main__":
    main()
'''