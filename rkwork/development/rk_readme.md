# fastgpt本地开发部署方案

## 快速开始

1 安装命令：

```
git clone git@github.com:RKwork85/Fastgpt_local_development.git
cd rkwork
docker compose -f ./docker-compose-pgvector.yml
```
2 配置

```

1 新增file
>projects/app/.env.local 
注： 主要需要修改API_KEY和数据库的地址与端口以及数据库账号的用户名和密码，具体配置需要和docker配置文件相同 （url/username/password）

>projects/app/data/config.local.json

>

2 安装
npm install -g pnpm
npm config set registry https://npm.aliyun.com
修改限制运行脚本

查看：
get-executionpolicy

设置：
set-ExecutionPolicy RemoteSigned
```
## Oters

- onepai 默认 账号密码为：root:123456
- 其它服务密码均为：rkwork；可在doker-compose文件中自行更改
- 需要测试一下oneapi接口功能 undo / 在oneapi项目测试显示成功/可能还需要使用
- windows11上 npm设置镜像源无法设置 ;使用临时下载源：pnpm i  --registry=https://registry.npmmirror.com
- 待解决
```
. postinstall$ sh ./scripts/postinstall.sh                                                                                                                        │ 'sh' �����ڲ����ⲿ���Ҳ���ǿ����еĳ���                                                                                                      │ ���������ļ���                                                                                                                                       └─ Failed in 25ms at D:\rkwork\project\FastGPT                                                                                                                     ELIFECYCLE  Command failed with exit code 1.  
```
- 项目启动后 mongodb无法链接
```
mongo -u rkwork -p rkwork --authenticationDatabase admin
mongo -u root -p rkwork --authenticationDatabase admin
show databases;


-  mongosh admin 命令时，你实际上是在启动 MongoDB Shell 并直接连接到名为 admin 的数据库。这样做的目的是为了执行一些管理任务，比如用户管理、角色管理或者监控数据库的健康状况。
```

- 创建一个数据库
```
db.createUser({
  user: "rkwork",
  pwd: "rkwork",
  roles: [{ role: "root", db: "fastgpt" }]
});

```
## So-vits

资源：

https://pan.baidu.com/s/12u_LDyb5KSOfvjJ9LVwCIQ?pwd=g8n4

站点：

https://www.yuque.com/umoubuton/ueupp5


## 参考资料

[官方链接] https://doc.tryfastgpt.ai/docs/development/intro/


```

你好，现在我们开始角色扮演，你的身份是：家庭和谐情感导师：周老师；我是求助者；请注意以人的口吻和我沟通交流，基本逻辑是：1 了解求助者的需求 比如：亲爱的，感谢您的信任与支持，我能抱你什么吗，需要和我聊聊吗？【爱心表情】【抱抱表情】 2 在求助者表述困境后， 认同求助者的情感，站在求助者的情绪上，给予认可： 太过分；怎么可以这样？；你一定....；3 询问求助者的家庭感情状况(主要是夫妻之间) 4 引导求助者分析产生这样状况的原因 5 分析产生原因的时间：比如生孩子后，结婚后。工作后等；6 分析当下夫妻之间的状态 7 询问求助者 的情感流通来自哪里，是否和丈夫 有沟通 9 询问求助者 这样的相处模式对感情的影响 10 适当给予求助者关怀，抚慰求助者的情绪，比如：亲爱的。辛苦你坚持这么多年了；11 为求助者分享自己的课程，语言要有亲和力；好的以上11点，请务必按照这样的方式进行情感指导。从你下次回答时开始，每次回答尽量简短，只包含一点内容
```

## 数据库登录

mysql 登录

>mysql -h localhost -P 3306 -u root -p

>SHOW DATABASES;