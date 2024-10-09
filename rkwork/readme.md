#  rkwork 工作目录说明

```
├── compose_quick                                                       // docker compose 文件目录
│   ├── mongo
│   │   └── data
│   │       ├── diagnostic.data  [error opening dir]
│   │       └── journal  [error opening dir]
│   ├── mysql
│   │   ├── #innodb_redo
│   │   ├── #innodb_temp
│   │   ├── media_crawler
│   │   ├── mysql
│   │   ├── oneapi
│   │   ├── performance_schema
│   │   └── sys
│   ├── oneapi
│   │   └── logs
│   └── pg
│       └── data  [error opening dir]
└── development                                                         // 开发记录                                                 // python接口测试目录
    ├── config.json
    ├── docker-compose-pgvector.yml
    ├── interface_py                                                   // python API示例
    │   └── interface_oneapi.py                                        // api 调用oneapi中的模型
    │   ├── interface_fastgpt.py                                       // api 调用Fastgpt平台应用
    └── rk_readme.md
```



## Fastgpt 应用接口测试


>**对话**
### 1 api 对接Oneapi平台模型 

```
curl --location --request POST 'http://127.0.0.1:3001/api/v1/chat/completions' \
--header 'Authorization: sk-3aeP4hpc7OlzUThX870d2817E45f496580Ee465fDc3d34D6' \
--header 'Content-Type: application/json' \
--data-raw '{
    "chatId": "glm-4",
    "stream": false,
    "detail": false,
    "variables": {
        "uid": "asdfadsfasfd2323",
        "name": "张三"
    },
    "messages": [
        {
            "content": "写一篇800字的文章，题目为：论当代大学生的社会担当",
            "role": "user"
        }
    ]
}'


   
```


### 2 api 对接Fastgpt平台发布应用

```
curl --location --request POST 'http://127.0.0.1:3000/api/v1/chat/completions' \
--header 'Authorization: Bearer fastgpt-xX2FbZzgsKIJIVXH1Kng0GtBY89kYXJbRZ2Bre1N1Zh0ajU6jIOW9' \
--header 'Content-Type: application/json' \
--data-raw '{
    "chatId": "111",
    "stream": true,
    "detail": false,
    "messages": [
        {
            "content": "写一篇800字的文章，题目为：论当代大学生的社会担当",
            "role": "user"
        }
    ]
}'
```



## 关于token

中文场景下
一个 token ≈ 1.6汉字

英文场景下
一个 token ≈ 0.75单词 ≈ 4个字符



## problems

1 fastgpt 应用 api_key 使用错误
>:{"code":500,"statusText":"","message":"Key is error. You need to use the app key rather than the account key.","data"null}

solve: 应在应用发布中生成密钥,而非账号API密钥



## workflow

1 翻译工作流


>The phrase "岁月静好，执手携老" can be translated into English as "May the years be peaceful and the days be filled with love, holding hands until old age."


{
  "data1": "第一轮：直译\n愿年份平静，日子充满爱，手牵手直到老年。\n\n第二轮：优化\n愿岁月静好，时光充满温情，相携之手直至暮年。\n\n第三轮：校验优化后的句子是否流畅\n岁月静好，时光流转间爱意满满，携手同行，直至白头。\n\n第四轮：美化\n愿时光轻柔，爱意如歌，你我手牵手，共赴岁月之巅。\n\n第五轮：定稿\n岁月悠长，爱如歌谣，携手并肩，共度时光直至白首。"
}

```
function getContentOfLastElement(text) {
    const matches = text.match(/\n([^\n]*)/g);
    // 直接返回去除前后空白的最后一个匹配项，如果存在的话
    return matches ? matches[matches.length - 1].trim() : null;
}

const text = `第一轮：直译\n愿年份平静，日子充满爱，手牵手直到老年。\n\n第二轮：优化\n愿岁月静好，时光充满温情，相携之手直至暮年。\n\n第三轮：校验优化后的句子是否流畅\n岁月静好，时光流转间爱意满满，携手同行，直至白头。\n\n第四轮：美化\n愿时光轻柔，爱意如歌，你我手牵手，共赴岁月之巅。\n\n第五轮：定稿\n岁月悠长，爱如歌谣，携手并肩，共度时光直至白首。`;

const lastElement = getContentOfLastElement(text);
console.log(lastElement);

```

几点注意：
```
代码工具需要

入口函数名称要对： function main({arg1}, ) 

return {json格式} ;设置变量接收 对应的关键字
```

## 2 知识库

>饺子，又称水饺、扁食，是中国传统的面点之一，其历史可以追溯到古代中国。关于饺子的起源，有多种说法，其中较为广泛接受的是起源于汉代。据传，饺子是由汉代名医张仲景所创。当时，张仲景为了治疗病人的耳朵冻伤，将羊肉和一些驱寒药材切碎，用面皮包裹后煮熟，形状类似耳朵，称为“娇耳”，后来逐渐演变成了今天的饺子。


## 数据库

- Mysql: oneapi的相关数据
- MongoDB：用于存储除了向量外的各类数据
- PostgreSQL/Milvus：存储向量数据

mysql 连接：
username:passowrd:database

pg 连接：
username:passowrd:database


mongo 连接:

mongodb://myusername:mypassword@0.0.0.0:27017/fastgpt?authSource=admin&directConnection=true

## docs

[快速开始](./../docSite/content/zh-cn/docs/development/intro.md)

[知识库搜索方案和参数](./../docSite/content/zh-cn/docs/course/dataset_engine.md)

description: '本节会详细介绍 FastGPT 知识库结构设计，理解其 QA 的存储格式和多向量映射，以便更好的构建知识库。同时会介绍每个搜索参数的功能。这篇介绍主要以使用为主，详细原理不多介绍。'

[知识库接口](./../docSite/content/zh-cn/docs/development/openapi/dataset.md)

[工具外部使用](./../docSite/content/zh-cn/docs/use-cases/gapier.md)


[对接微信](./../docSite/content/zh-cn/docs/use-cases/onwechat.md)


[lab高级编排导入](./../docSite/content/zh-cn/docs/workflow/examples/lab_appointment.md)


[](./home/rkwork/rkwork/project/FastGPT/docSite/content/zh-cn/docs/course/dataset_engine.md)



## bugs

git commit -am 'rk: v1.0.0 两个文件夹: docker compose 快速启动, API接口文档测试'

无法连接数据库mongodb:

>Unable to load connection: MongoServerSelectionError: getaddrinfo EAI_AGAIN mongo

