import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

data = [
    {
        "博主": "蕉下官方旗舰店",
        "ID": "1",
        "URL": "https://www.iesdouyin.com/share/video/7317848191443995931/?region=CN&mid=7317848319362009892&u_code=16c2i54ib&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=5Blp0ALnupPX54jJtrZw5FuHPOBlBtO7PQRsIE.ZPsY-&share_version=0&ts=1735959097&from_aid=6383&from_ssr=1",
        "Awesome ID": "7317848191443995931",
        "标题": "一件顶多件！这性价比真的太值啦#蕉下官方旗舰店气绒服#蕉下官方旗舰店#冬季穿搭",
        "评论量": "0",
        "分享量": "2",
        "点赞量": "8",
        "收藏量": "1",
        "视频发布时间": "2024-01-01 10:10:00",
        "采集时间": "2025-01-04 10:51:39"
    },
    {
        "博主": "蕉下官方旗舰店",
        "ID": "2",
        "URL": "https://www.iesdouyin.com/share/video/7317848552250674482/?region=CN&mid=7317848649000930075&u_code=16c2i54ib&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=oPFgj_Wz9hl_KPLS9h2qzzqnxOhTnO9fRbGBF9YfY6E-&share_version=0&ts=1735959097&from_aid=6383&from_ssr=1",
        "Awesome ID": "7317848552250674482",
        "标题": "南方的姐妹福音！#冬季必备#蕉下官方旗舰店气绒服#冬季新款#蕉下官方旗舰店",
        "评论量": "2",
        "分享量": "3",
        "点赞量": "20",
        "收藏量": "3",
        "视频发布时间": "2024-01-01 18:10:00",
        "采集时间": "2025-01-04 10:51:39"
    },
    {
        "博主": "蕉下官方旗舰店",
        "ID": "3",
        "URL": "https://www.iesdouyin.com/share/video/7317849435424165130/?region=CN&mid=7317849524737887015&u_code=16c2i54ib&did=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=p2QvtrT5bmXbATZLZV70jTk5Euxo5.VfzDenCSk_OUs-&share_version=0&ts=1735959097&from_aid=6383&from_ssr=1",
        "Awesome ID": "7317849435424165130",
        "标题": "这个冬天，和闺蜜穿起来！#蕉下官方旗舰店气绒服#蕉下官方旗舰店#姐妹日常#我们俩",
        "评论量": "2",
        "分享量": "13",
        "点赞量": "106",
        "收藏量": "17",
        "视频发布时间": "2024-01-01 18:15:00",
        "采集时间": "2025-01-04 10:51:39"
    }]

with open('temp.txt', 'w', encoding='utf-8') as f:
    for j in data:
        f.write(str(j) +'\n')
        f.flush()

task = 1502
for i in range( int(task/20) + 1):
    print(i)
    