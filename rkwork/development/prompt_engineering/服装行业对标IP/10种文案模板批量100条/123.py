color_data1 = '品牌：SW\n无缝拼接鹅绒外套\n颜色：姜黄色\n材质：高品质 90%鹅绒\n版型：修身设计\n优点：摆臂自由，运动无拘无束；机洗'
color_data2 = '品牌：SW\n无缝拼接鹅绒外套\n颜色：奶油杏\n材质：高品质 90%鹅绒\n版型：修身设计\n优点：摆臂自由，运动无拘无束；机洗'
color_data3 = '品牌：SW\n无缝拼接鹅绒外套\n颜色：浅白灰\n材质：高品质 90%鹅绒\n版型：修身设计\n优点：摆臂自由，运动无拘无束；机洗'
color_data4 = '品牌：SW\n无缝拼接鹅绒外套\n颜色：黑色\n材质：高品质 90%鹅绒\n版型：修身设计\n优点：摆臂自由，运动无拘无束；机洗'
color_data5 = '品牌：SW\n无缝拼接鹅绒外套\n颜色：芥末色\n材质：高品质 90%鹅绒\n版型：修身设计\n优点：摆臂自由，运动无拘无束；机洗'
color_data6 = '品牌：SW\n无缝拼接鹅绒外套\n颜色：沙棕色\n材质：高品质 90%鹅绒\n版型：修身设计\n优点：摆臂自由，运动无拘无束；机洗'
color_data_list = [color_data1,color_data2,color_data3,color_data4,color_data5,color_data6]
data = []
for index,i in enumerate(color_data_list):
    for j in range(10):
        data.append({"ID":f"{index + 1}","DataId":f"{index + 1}-f{j + 1}","data":i})
print(data)