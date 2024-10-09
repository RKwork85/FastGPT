## Fastgpt 知识库接口本地测试

>1 创建一个知识库(知识库中的密钥是用户密钥)

'''
curl --location --request POST 'http://localhost:3000/api/core/dataset/create' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \
--header 'Content-Type: application/json' \
--data-raw '{
    "parentId": null,
    "type": "dataset",
    "name":"rkworkk测试",
    "intro":"介绍",
    "avatar": "",
    "vectorModel": "embedding-2",
    "agentModel": "glm-4"
}'


return: 知识库ID
{"code":200,"statusText":"","message":"","data":"66ee8813b2e1e065a3377fdf"}
'''

>2 获取知识库列表：知识库列表

'''
curl --location --request POST 'http://localhost:3000/api/core/dataset/list?parentId=' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \
--header 'Content-Type: application/json' \
--data-raw '{
    "parentId":""
}'

return：data结构列表套字典：[{},{}...],新的数据会插到列表头部

{"code":200,"statusText":"","message":"","data":[{"_id":"66ee8939b2e1e065a337800e","avatar":"","name":"rkworkk测试","intro":"","type":"dataset","permission":{"value":4294967295,"isOwner":true,"hasManagePer":true,"hasWritePer":true,"hasReadPer":true},"vectorModel":{"model":"embedding-2","name":"rkwork_embedding","avatar":"/imgs/model/openai.svg","charsPointsPrice":0,"defaultToken":512,"maxToken":3000,"weight":100},"defaultPermission":0,"inheritPermission":true},{"_id":"66ee84d9b2e1e065a3377fac","avatar":"","name":"rkwork测试","intro":"","type":"dataset","permission":{"value":4294967295,"isOwner":true,"hasManagePer":true,"hasWritePer":true,"hasReadPer":true},"vectorModel":{"model":"embedding-2","name":"rkwork_embedding","avatar":"/imgs/model/openai.svg","charsPointsPrice":0,"defaultToken":512,"maxToken":3000,"weight":100},"defaultPermission":0,"inheritPermission":true},{"_id":"66ee7633b2e1e065a3377323","avatar":"/icon/logo.svg","name":"libai","intro":"","type":"dataset","permission":{"value":4294967295,"isOwner":true,"hasManagePer":true,"hasWritePer":true,"hasReadPer":true},"vectorModel":{"model":"embedding-2","name":"rkwork_embedding","avatar":"/imgs/model/openai.svg","charsPointsPrice":0,"defaultToken":512,"maxToken":3000,"weight":100},"defaultPermission":0,"inheritPermission":true}]}

'''



'''

>3 删除一个知识库: 传参id

'''
curl --location --request DELETE 'http://localhost:3000/api/core/dataset/delete?id=66ee8813b2e1e065a3377fdf' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \

return:状态码
{"code":200,"statusText":"","message":"","data":null}

'''


>4 获取知识库详情 

'''
curl --location --request GET 'http://localhost:3000/api/core/dataset/detail?id=66ee84d9b2e1e065a3377fac' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \

return: 知识库更为详细信息

{"code":200,"statusText":"","message":"","data":{"_id":"66ee84d9b2e1e065a3377fac","parentId":null,"teamId":"66eb92e14dcb0cfe3038476a","tmbId":"66eb92e24dcb0cfe30384776","type":"dataset","status":"active","avatar":"","name":"rkwork测试","vectorModel":{"model":"embedding-2","name":"rkwork_embedding","avatar":"/imgs/model/openai.svg","charsPointsPrice":0,"defaultToken":512,"maxToken":3000,"weight":100},"agentModel":{"model":"glm-4","name":"rkwork","avatar":"/imgs/model/openai.svg","maxContext":125000,"maxResponse":16000,"quoteMaxToken":120000,"maxTemperature":1.2,"charsPointsPrice":0,"censor":false,"vision":true,"datasetProcess":true,"usedInClassify":true,"usedInExtractFields":true,"usedInToolCall":true,"usedInQueryExtension":true,"toolChoice":true,"functionCall":false,"customCQPrompt":"","customExtractPrompt":"","defaultSystemChatPrompt":"","defaultConfig":{}},"intro":"","defaultPermission":0,"inheritPermission":true,"updateTime":"2024-09-21T08:33:29.295Z","__v":0,"permission":{"value":4294967295,"isOwner":true,"hasManagePer":true,"hasWritePer":true,"hasReadPer":true}}}
'''
>5 创建一个空的集合 

'''
curl --location --request POST 'http://localhost:3000/api/core/dataset/collection/create' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \
--header 'Content-Type: application/json' \
--data-raw '{
    "datasetId":"66ee84d9b2e1e065a3377fac",
    "parentId": null,
    "name":"空的集合测试",
    "type":"virtual",
    "metadata":{
      "test":111
    }
}'


return：集合id:但是不会在知识库中存储集合ID

{"code":200,"statusText":"","message":"","data":"66ee8d66b2e1e065a337811d"}

{"code":200,"statusText":"","message":"","data":{"_id":"66ee8939b2e1e065a337800e","parentId":null,"teamId":"66eb92e14dcb0cfe3038476a","tmbId":"66eb92e24dcb0cfe30384776","type":"dataset","status":"active","avatar":"","name":"rkworkk测试","vectorModel":{"model":"embedding-2","name":"rkwork_embedding","avatar":"/imgs/model/openai.svg","charsPointsPrice":0,"defaultToken":512,"maxToken":3000,"weight":100},"agentModel":{"model":"glm-4","name":"rkwork","avatar":"/imgs/model/openai.svg","maxContext":125000,"maxResponse":16000,"quoteMaxToken":120000,"maxTemperature":1.2,"charsPointsPrice":0,"censor":false,"vision":true,"datasetProcess":true,"usedInClassify":true,"usedInExtractFields":true,"usedInToolCall":true,"usedInQueryExtension":true,"toolChoice":true,"functionCall":false,"customCQPrompt":"","customExtractPrompt":"","defaultSystemChatPrompt":"","defaultConfig":{}},"intro":"","defaultPermission":0,"inheritPermission":true,"updateTime":"2024-09-21T08:52:09.669Z","__v":0,"permission":{"value":4294967295,"isOwner":true,"hasManagePer":true,"hasWritePer":true,"hasReadPer":true}}}

'''
>6 创建一个纯文本集合

'''
curl --location --request POST 'http://localhost:3000/api/core/dataset/collection/create/text' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text":"夏为公司成立于1988年",
    "datasetId":"66ee8939b2e1e065a337800e",
    "parentId": null,
    "name":"纯文本集合测试",

    "trainingType": "qa",
    "chunkSize":8000,
    "chunkSplitter":"",
    "qaPrompt":"11",

    "metadata":{}
}'

return : 字典格式

{"code":200,"statusText":"","message":"","data":{"collectionId":"66ee9280b2e1e065a337826d","results":{"insertLen":1,"overToken":[],"repeat":[],"error":[]}}}
'''

>7 创建一个链接集合 
'''

curl --location --request POST 'http://localhost:3000/api/core/dataset/collection/create/link' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \
--header 'Content-Type: application/json' \
--data-raw '{
    "link":"https://baike.baidu.com/item/%E6%9D%9C%E7%94%AB/63508?fr=ge_ala",
    "datasetId":"66ee8939b2e1e065a337800e",
    "parentId": null,
    "name":"杜甫百科链接",
    "trainingType": "chunk",
    "chunkSize":512,
    "chunkSplitter":"",
    "qaPrompt":"",

    "metadata":{
        "webPageSelector":".docs-content"
    }
}'

return：json：集合id ；显示页面中只有网页title

{"code":200,"statusText":"","message":"","data":{"collectionId":"66ee94edb2e1e065a3378390","results":{"insertLen":0}}}
'''
>8 创建一个文件集合(文本数据上传接口)

'''
传入一个文件，创建一个集合，会读取文件内容进行分割。目前支持：pdf, docx, md, txt, html, csv。
使用代码上传时，请注意中文 filename 需要进行 encode 处理，否则容易乱码。


curl --location --request POST 'http://localhost:3000/api/core/dataset/collection/create/localFile' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \
--form 'file=@"/home/rkwork/rkwork/project/FastGPT/rkwork/development/kb/dufu.txt"' \
--form 'data="{\"datasetId\":\"66ee8939b2e1e065a337800e\",\"parentId\":null,\"trainingType\":\"chunk\",\"chunkSize\":512,\"chunkSplitter\":\"\",\"qaPrompt\":\"\",\"metadata\":{}}"'


return: json:{} 

{"code":200,"statusText":"","message":"","data":{"collectionId":"66ee9a2eb2e1e065a33784e5","results":{"insertLen":42,"overToken":[],"repeat":[],"error":[]}}}
'''
>9 创建训练订单 （特殊:）

'''
curl --location --request POST 'http://localhost:3000/api/support/wallet/usage/createTrainingUsage' \
--header 'Authorization:  Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \
--header 'Content-Type: application/json' \
--data-raw '{
    "datasetId": "66ee8939b2e1e065a337800e",
    "name": "rkwrok 可选，自定义订单名称，例如：文档训练-fastgpt.docx"
}'

return：
{"code":200,"statusText":"","message":"","data":"66f0e376006fa8f9f258032e"}

'''
>10 某个一个知识库的集合

'''
curl --location --request POST 'http://localhost:3000/api/core/dataset/collection/list' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W'  \
--header 'Content-Type: application/json' \
--data-raw '{
    "pageNum":1,
    "pageSize": 10,
    "datasetId":"66ee8939b2e1e065a337800e",
    "parentId": null,
    "searchText":""
}'

return:{others, [{},{}], 总数}
{"code":200,"statusText":"","message":"","data":{"pageNum":1,"pageSize":10,"data":[{"_id":"66ee9a2eb2e1e065a33784e5","parentId":null,"tmbId":"66eb92e24dcb0cfe30384776","type":"file","name":"dufu.txt","forbid":false,"trainingType":"chunk","tags":[],"fileId":"66ee9a2eb2e1e065a33784e2","createTime":"2024-09-21T10:04:30.857Z","updateTime":"2024-09-21T10:04:30.857Z","dataAmount":42,"trainingAmount":0,"permission":{"value":4294967295,"isOwner":true,"hasManagePer":true,"hasWritePer":true,"hasReadPer":true}},{"_id":"66ee94edb2e1e065a3378390","parentId":null,"tmbId":"66eb92e24dcb0cfe30384776","type":"link","name":"杜甫（唐代著名现实主义诗人）_百度百科","forbid":false,"trainingType":"chunk","tags":[],"rawLink":"https://baike.baidu.com/item/%E6%9D%9C%E7%94%AB/63508?fr=ge_ala","createTime":"2024-09-21T09:42:05.691Z","updateTime":"2024-09-21T09:42:05.691Z","dataAmount":0,"trainingAmount":0,"permission":{"value":4294967295,"isOwner":true,"hasManagePer":true,"hasWritePer":true,"hasReadPer":true}},{"_id":"66ee9280b2e1e065a337826d","parentId":null,"tmbId":"66eb92e24dcb0cfe30384776","type":"virtual","name":"纯文本集合测试","forbid":false,"trainingType":"qa","tags":[],"createTime":"2024-09-21T09:31:44.609Z","updateTime":"2024-09-21T09:31:44.609Z","dataAmount":1,"trainingAmount":0,"permission":{"value":4294967295,"isOwner":true,"hasManagePer":true,"hasWritePer":true,"hasReadPer":true}}],"total":3}}
'''
>11 集合的详情

'''
curl --location --request GET 'http://localhost:3000/api/core/dataset/collection/detail?id=66ee94edb2e1e065a3378390' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \

return：

{"code":200,"statusText":"","message":"","data":{"_id":"66ee94edb2e1e065a3378390","parentId":null,"teamId":"66eb92e14dcb0cfe3038476a","tmbId":"66eb92e24dcb0cfe30384776","datasetId":{"_id":"66ee8939b2e1e065a337800e","parentId":null,"teamId":"66eb92e14dcb0cfe3038476a","tmbId":"66eb92e24dcb0cfe30384776","type":"dataset","status":"active","avatar":"","name":"rkworkk测试","vectorModel":"embedding-2","agentModel":"glm-4","intro":"","defaultPermission":0,"inheritPermission":true,"updateTime":"2024-09-21T08:52:09.669Z","__v":0},"type":"link","name":"杜甫（唐代著名现实主义诗人）_百度百科","forbid":false,"trainingType":"chunk","chunkSize":512,"chunkSplitter":"","qaPrompt":"","tags":[],"rawLink":"https://baike.baidu.com/item/%E6%9D%9C%E7%94%AB/63508?fr=ge_ala","metadata":{"webPageSelector":".docs-content"},"createTime":"2024-09-21T09:42:05.691Z","updateTime":"2024-09-21T09:42:05.691Z","__v":0,"hashRawText":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","rawTextLength":0,"sourceId":"https://baike.baidu.com/item/%E6%9D%9C%E7%94%AB/63508?fr=ge_ala","sourceName":"杜甫（唐代著名现实主义诗人）_百度百科","permission":{"value":4294967295,"isOwner":true,"hasManagePer":true,"hasWritePer":true,"hasReadPer":true}}}


'''
>12 修改集合信息

'''
curl --location --request PUT 'http://localhost:3000/api/core/dataset/collection/update' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \
--header 'Content-Type: application/json' \
--data-raw '{
    "id":"66ee94edb2e1e065a3378390",
    "parentId": null,
    "name": "杜甫（唐代著名现实主义诗人）_百度百科_修改集合信息",
    "tags": ["tag1", "tag2"],
    "forbid": false,
    "createTime": "2024-01-01T00:00:00.000Z"
}'

return： {}
{"code":200,"statusText":"","message":"","data":null}
'''
>13 通过外部文件 ID 修改集合信息（无用）

'''
通过外部文件 ID 修改集合信息， 只需要把 id 换成 datasetId 和 externalFileId。

curl --location --request PUT 'http://localhost:3000/api/core/dataset/collection/update' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \
--header 'Content-Type: application/json' \
--data-raw '{
    "datasetId":"6593e137231a2be9c5603ba7",
    "externalFileId":"1111",
    "parentId": null,
    "name": "测2222试",
    "tags": ["tag1", "tag2"],
    "forbid": false,
    "createTime": "2024-01-01T00:00:00.000Z"
}'

'''

>14 删除一个集合 

'''

curl --location --request DELETE 'http://localhost:3000/api/core/dataset/collection/delete?id=65aa2a64e6cb9b8ccdc00de8' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \

'''

>15 为集合批量添加添加数据 

'''

注意，每次最多推送 200 组数据。

curl --location --request POST 'http://localhost:3000/api/core/dataset/data/pushData' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \
--header 'Content-Type: application/json' \
--data-raw '{
    "collectionId": "66ee94edb2e1e065a3378390",
    "trainingMode": "chunk",
    "prompt": "可选。qa 拆分引导词，chunk 模式下忽略",
    "billId": "可选。如果有这个值，本次的数据会被聚合到一个订单中，这个值可以重复使用。可以参考 [创建训练订单] 获取该值。",
    "data": [
        {
            "q": "你是谁？",
            "a": "我是由rkwork 创建的FastGPT助手，用于帮助用户解决问题，提供思路"
        },
        {
            "q": "夏为公司什么时候成立的",
            "a": "该公司成立于1824年",
            "indexes": [
                {
                    "text":"夏为公司成立于1824年，至今已经有200年的历史了"
                },
                {
                    "text":"夏为公司一共有300名员工"
                }
            ]
        }
    ]
}'

return: {"code":200,"statusText":"","message":"","data":{"insertLen":2,"overToken":[],"repeat":[],"error":[]}}

'''


>16 获取集合的数据列表

'''

curl --location --request POST 'http://localhost:3000/api/core/dataset/data/list' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \
--header 'Content-Type: application/json' \
--data-raw '{
    "pageNum":1,
    "pageSize": 10,
    "collectionId":"66ee94edb2e1e065a3378390",
    "searchText":""
}'

return : 

{"code":200,"statusText":"","message":"","data":{"pageNum":1,"pageSize":10,"data":[{"_id":"66f0e67a006fa8f9f25806b5","datasetId":"66ee8939b2e1e065a337800e","collectionId":"66ee94edb2e1e065a3378390","q":"夏为公司什么时候成立的","a":"我什么都会","chunkIndex":0},{"_id":"66f0e67a006fa8f9f25806af","datasetId":"66ee8939b2e1e065a337800e","collectionId":"66ee94edb2e1e065a3378390","q":"你是谁？","a":"我是由rkwork 创建的FastGPT助手，用于帮助用户解决问题，提供思路","chunkIndex":0}],"total":2}}
'''


>17 获取单条数据详情 
'''
curl --location --request GET 'http://localhost:3000/api/core/dataset/data/detail?id=66f0e67a006fa8f9f25806b5' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \

return :
{"code":200,"statusText":"","message":"","data":{"id":"66f0e67a006fa8f9f25806b5","teamId":"66eb92e14dcb0cfe3038476a","q":"夏为公司什么时候成立的","a":"我什么都会","chunkIndex":0,"indexes":[{"defaultIndex":true,"dataId":"154","text":"夏为公司什么时候成立的\n我什么都会","_id":"66f0e67a006fa8f9f25806b6"},{"defaultIndex":false,"dataId":"153","text":"夏为公司成立于1824年，至今已经有200年的历史了","_id":"66f0e67a006fa8f9f25806b7"},{"defaultIndex":false,"dataId":"152","text":"夏为公司一共有300名员工","_id":"66f0e67a006fa8f9f25806b8"}],"datasetId":"66ee8939b2e1e065a337800e","collectionId":"66ee94edb2e1e065a3378390","sourceName":"杜甫（唐代著名现实主义诗人）_百度百科_修改集合信息","sourceId":"https://baike.baidu.com/item/%E6%9D%9C%E7%94%AB/63508?fr=ge_ala","isOwner":true,"canWrite":true}}

'''

>18 修改单条数据 

'''
1 查看单条数据详情

curl --location --request GET 'http://localhost:3000/api/core/dataset/data/detail?id=66f0eb0b006fa8f9f2580821' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \

>{"code":200,"statusText":"","message":"","data":{"id":"66f0eb0b006fa8f9f2580821","teamId":"66eb92e14dcb0cfe3038476a","q":"夏为公司什么时候成立的","a":"该公司成立于1824年","chunkIndex":0,"indexes":[{"defaultIndex":true,"dataId":"156","text":"夏为公司什么时候成立的\n该公司成立于1824年","_id":"66f0eb0b006fa8f9f2580822"},{"defaultIndex":false,"dataId":"159","text":"夏为公司成立于1824年，至今已经有200年的历史了","_id":"66f0eb0b006fa8f9f2580823"},{"defaultIndex":false,"dataId":"157","text":"夏为公司一共有300名员工","_id":"66f0eb0b006fa8f9f2580824"}],"datasetId":"66ee8939b2e1e065a337800e","collectionId":"66ee94edb2e1e065a3378390","sourceName":"杜甫（唐代著名现实主义诗人）_百度百科_修改集合信息","sourceId":"https://baike.baidu.com/item/%E6%9D%9C%E7%94%AB/63508?fr=ge_ala","isOwner":true,"canWrite":true}}

2 修改单条数据
curl --location --request PUT 'http://localhost:3000/api/core/dataset/data/update' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dataId":"66f0eb0b006fa8f9f2580821",
    "q":"夏为公司什么时候成立的_修改单条数据测试",
    "a":"夏为公司成立于1824年，至今已经有200年的历史了_修改单条数据测试",
    "indexes":[
        {
            "dataId": "156",
            "defaultIndex":false,
            "text":"夏为公司成立于1824年，至今已经有200年的历史了_修改单条数据测试"
        },
        {
            "text":"修改后的自定义索引2。（会删除原来的自定义索引2，并插入新的自定义索引2）"
        }
    ]
}'


>19 搜索测试 
'''
curl --location --request GET 'http://localhost:3000/api/core/dataset/data/detail?id=66f0e67a006fa8f9f25806b5' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \

return :


'''
curl --location --request POST 'http://localhost:3000/api/core/dataset/searchTest' \
--header 'Authorization: Bearer fastgpt-zS8WVggasOYrSobYOoU6E9QTAbO0FMyGnCjyOHOe0PrK9yxIu7584A3Plj7BSNA2W' \
--header 'Content-Type: application/json' \
--data-raw '{
    "datasetId": "66ee8939b2e1e065a337800e",
    "text": "夏为公司创立时间",
    "limit": 5000,
    "similarity": 0,
    "searchMode": "embedding",
    "usingReRank": false
}'


return 

{"code":200,"statusText":"","message":"","data":{"list":[{"id":"66f0e67a006fa8f9f25806b5","q":"夏为公司什么时候成立的","a":"我什么都会","chunkIndex":0,"datasetId":"66ee8939b2e1e065a337800e","collectionId":"66ee94edb2e1e065a3378390","sourceId":"https://baike.baidu.com/item/%E6%9D%9C%E7%94%AB/63508?fr=ge_ala","sourceName":"杜甫（唐代著名现实主义诗人）_百度百科_修改集合信息","score":[{"type":"embedding","value":0.8337006568908691,"index":0}],"tokens":19},{"id":"66ee9282b2e1e065a337827f","q":"夏公司是哪一年成立的？","a":"夏公司成立于1988年。\n\n------\n\n现在我们可以继续添加更多的问题和答案了，请提供需要整理的详细信息。","chunkIndex":0,"datasetId":"66ee8939b2e1e065a337800e","collectionId":"66ee9280b2e1e065a337826d","sourceName":"纯文本集合测试","score":[{"type":"embedding","value":0.7643303871154785,"index":1}],"tokens":53},{"id":"66f0eb0b006fa8f9f2580821","q":"夏为公司什么时候成立的_修改单条数据测试","a":"test","chunkIndex":0,"datasetId":"66ee8939b2e1e065a337800e","collectionId":"66ee94edb2e1e065a3378390","sourceId":"https://baike.baidu.com/item/%E6%9D%9C%E7%94%AB/63508?fr=ge_ala","sourceName":"杜甫（唐代著名现实主义诗人）_百度百科_修改集合信息","score":[{"type":"embedding","value":0.732600748538971,"index":2}],"tokens":20},{"id":"66ee9a2fb2e1e065a337853c","q":"这时，中原战局大有好转，代宗即位后命长子雍王李适为天下兵马元帅，仆固怀恩为副元帅，讨伐史朝义。广德元年（763年）正月， 史朝义被迫自杀，河南河北各州全部收复。消息传到梓州，杜甫高兴得热泪横流，写下了“平生第一快诗”《闻官军收河南河北》。但他全家仍在梓州逃难，难以回到家乡。同年，严武再度入蜀任职。杜甫得知严武重来的消息，喜出望外，于是在广德二年（764年）春又从阆州领着妻子赶回成都。三月，杜甫刚回到成都，严武就启奏他为节度参谋、检校工部员外郎，赐绯鱼袋 [11]，后人因此称杜甫为“杜工部”。回到草堂，他本有一番修饰环境的打算，远近的邻居朋友也想一一相会，但一入节度使官署，就进入练兵备战的气氛中。七月，严武亲临前线，写下《军城早秋》诗，杜甫于九月写了和诗《奉和严大夫军城早秋》，赞美严武破吐蕃七万余众，拔当狗、盐川的胜利。杜甫在幕府半年，生活拘束，与同僚之间亦难免有“分曹失异同”的不愉快纠纷，最后在永泰元年（765年）正月三日辞幕府归浣花溪。 [100]\n漂泊南下\n夔府生活\n永泰元年（765年）四月，严武病逝，杜甫在成都无所依靠，在五月就携家沿岷江东下，结束了“五载客蜀郡，一年居梓州”的生活，“转作潇湘游”。 [100]","a":"","chunkIndex":10,"datasetId":"66ee8939b2e1e065a337800e","collectionId":"66ee9a2eb2e1e065a33784e5","sourceId":"66ee9a2eb2e1e065a33784e2","sourceName":"dufu.txt","score":[{"type":"embedding","value":0.21920403838157654,"index":3}],"tokens":680},{"id":"66f0eb0b006fa8f9f258081b","q":"你是谁？","a":"我是由rkwork 创建的FastGPT助手，用于帮助用户解决问题，提供思路","chunkIndex":0,"datasetId":"66ee8939b2e1e065a337800e","collectionId":"66ee94edb2e1e065a3378390","sourceId":"https://baike.baidu.com/item/%E6%9D%9C%E7%94%AB/63508?fr=ge_ala","sourceName":"杜甫（唐代著名现实主义诗人）_百度百科_修改集合信息","score":[{"type":"embedding","value":0.21168437600135803,"index":4}],"tokens":35},{"id":"66ee9a2fb2e1e065a3378600","q":"参考资料\n12月12日：中国唐代著名诗人杜甫诞辰．中华人民共和国中央人民政府．2007-02-12 [引用日期2020-12-06]\n2《旧唐书卷一百九十下·列传第一百四十》：杜甫，字子美，本襄阳人，后徙河南巩县。曾祖依艺，位终巩令。祖审言，位终膳部员外郎，自有传。父闲，终奉天令。\n3杜甫．《全唐诗·壮游》．北京．中华书局．1960\n4杜甫．《全唐诗·壮游》．北京：中华书局，1960\n5杜甫．《全唐诗·奉赠韦丞丈二十二韵》．北京：《中华书局》，1960\n6陈贻欣．杜甫评传 上．上海古籍出版社．1982年08月第1版．第42页\n7欧阳修、宋祁．《新唐书·卷二百一·列传第一百二十六·文艺上·杜审言·孙甫》．《中华书局》．1997\n8《新唐书卷二百一·列传第一百二十六》：天宝十三载，玄宗朝献太清宫，飨庙及郊，甫奏赋三篇。帝奇之，使待制集贤院，命宰相试文章，擢河西尉，不拜，改右卫率府胄曹参军。数上赋颂，因高自称道，且言：\"先臣恕、预以来，承儒守官十一世，迨审言，以文章显中宗时。臣赖绪业，自七岁属辞，且四十年，然衣不盖体，常寄食于人，窃恐转死沟壑，伏惟天子哀怜之。若令执先臣故事，拔泥涂之久辱，则臣之述作虽不足鼓吹《六经》，至沈郁顿挫，随时敏给，扬雄、枚皋可企及也。有臣如此，陛下其忍弃之？\"\n9《新唐书卷二百一·列传第一百二十六》：会禄山乱，天子入蜀，甫避走三川。肃宗立，自鄜州羸服欲奔行在，为贼所得。至德二年，亡走凤翔上谒，拜右拾遗。与房琯为布衣交，琯时败陈涛斜，又以客董廷兰，罢宰相。甫上疏言：“罪细，不宜免大臣。”帝怒，诏三司亲问。宰相张镐曰：“甫若抵罪，绝言者路。”帝乃解。甫谢，且称：“琯宰相子，少自树立为醇儒，有大臣体，时论许琯才堪公辅，陛下果委而相之。观其深念主忧，义形于色，然性失于简。酷嗜鼓琴，廷兰托琯门下，贫疾昏老，依倚为非，琯爱惜人情，一至玷污。臣叹其功名未就，志气挫衄，觊陛下弃细录大，所以冒死称述，涉近讦激，违忤圣心。陛下赦臣百死，再赐骸骨，天下之幸，非臣独蒙。”然帝自是不甚省录。\n10（唐）杜甫著；（清）钱谦益笺注．中国古典文学丛书 钱注杜诗 下．上海古籍出版社．2009.04．第688页","a":"","chunkIndex":40,"datasetId":"66ee8939b2e1e065a337800e","collectionId":"66ee9a2eb2e1e065a33784e5","sourceId":"66ee9a2eb2e1e065a33784e2","sourceName":"dufu.txt","score":[{"type":"embedding","value":0.19823035597801208,"index":6}],"tokens":1203},{"id":"66ee9a2fb2e1e065a3378551","q":"回到华州，旱灾的威胁就开始了，人民在天灾加战争负担双重压迫下毫无活路。杜甫写下《夏日叹》和《夏夜叹》，忧时伤乱，咏叹国难民苦。面对污浊的时政与无法遏制的饥荒，他只能在乾元二年（759年）七月弃官不做，带着家小远走秦州（今甘肃天水），另谋生路。 [12] [100]\n杜甫到秦州曾打算在东柯谷、西枝村觅一块隐居之地，但是这个羌胡杂居，吐蕃势力又不断扩张的地方，他无法久住下去。不过在秦州留下的三个多月中，却在他诗卷中增加了不少边塞题材的新作（《秦州杂诗》《寓目》等）。到了十月，他怀着“无食问乐土，无衣思南州”的念头，又领着全家南下同谷（今甘肃成县）。可是奔波了几十天，到同谷后，竟陷入饥寒交迫的绝境。这种种惨痛经历都写在《乾元中寓居同谷县作歌七首》里。在同谷住了 一个多月，杜甫又在十二月一日起程赴成都。 [100]\n从秦州到同谷、又从同谷到成都这两段路程中，杜甫曾有计划地写了《青阳峡》《木皮岭》《飞仙阁》《五盘》《剑门》等二十四首纪行诗，每段十二首，记述了自己一步步走过来的山川胜迹的真实面貌。这一年中，杜甫“一岁四行役”，从洛阳到华州、华州到秦州、秦州到同谷、同谷到剑南，可以说这是他艰苦奔波的一年，也是他思想变化最大、诗歌创作空前丰收的一年。 [100]","a":"","chunkIndex":8,"datasetId":"66ee8939b2e1e065a337800e","collectionId":"66ee9a2eb2e1e065a33784e5","sourceId":"66ee9a2eb2e1e065a33784e2","sourceName":"dufu.txt","score":[{"type":"embedding","value":0.19580084085464478,"index":7}],"tokens":675},{"id":"66ee9a2fb2e1e065a337854e","q":"客居蜀中\n杜甫全家初到成都时，寄居在一座僧徒寥落的古寺里，靠着“故人供禄米，邻舍与园蔬”，全家人的生活不仅可以暂时维持，而且从第二年就开始经营浣花溪西岸的草堂住宅（世称“杜甫草堂”，也称“浣花草堂”）了。在战乱中奔波多年的杜甫，总算有了个栖身之所了。他卜居初定，就一面忙着种树、种竹、种菜，一面还得为完成营建工程， 到蜀州、新津、青城等外县去访问乞贷于亲友，他步行或乘舟来往，无意中就写成了《为农》《田舍》《水槛遣心二首》《客至》《进艇》等不少怡情适意的小诗。可惜，好景不长，上元二年（761年）五月，杜甫草堂边的一棵有两百年寿命的柚树被暴风连根拔起，更不幸的是同年八月，他新建的草堂又遭一场暴风，使他全家“床头屋漏无干处，雨脚如麻未断绝”。他在不眠的长夜里，不禁从自家的苦难想到天下无数流离失所的人民，于是奋笔写下了“安得广厦千万间，大庇天下寒士俱欢颜，风雨不动安如山。呜呼！何时眼前突兀见此屋，吾庐独破受冻死亦足”的名句。 [100]在此期间，朝廷曾补授杜甫为京兆功曹参军，但他未去就职。 [12]\n上元二年（761年）十二月，杜甫的老友严武由绵州刺史升任兼管东西两川的节度使。上元三年（762年）春夏，杜甫和严武多次往来访问，在唱和诗篇中，严武曾劝他出来做官，他则希望严武能理解自己疏懒的个性。同 年四月，玄宗、肃宗父子两人相继去世，唐代宗即位，七月召严武入朝。杜甫亲自送严武到绵州奉济驿才分手，不料这时剑南西川兵马使徐知道在成都发动了叛乱，严武被乱兵阻隔，不得出剑门，杜甫也回不了成都，只得转 到梓州，依靠“李梓州”“严二别驾”等新朋友。八月，徐知道的叛乱被高适镇压，但动乱未止，杜甫只得把家属移到梓州来，并打算离东川，投三峡，赴西京。 [100]","a":"","chunkIndex":9,"datasetId":"66ee8939b2e1e065a337800e","collectionId":"66ee9a2eb2e1e065a33784e5","sourceId":"66ee9a2eb2e1e065a33784e2","sourceName":"dufu.txt","score":[{"type":"embedding","value":0.18225139379501343,"index":8}],"tokens":973},{"id":"66ee9a2fb2e1e065a3378558","q":"杜甫随着东下的小船，五月到嘉州（今四川乐山），六月到戎州（今四川宜宾）、渝州（今重庆市），七月到忠州（今重庆忠县），秋天到云安（今重庆云阳）。这时，他的消渴病和疟疠都犯了，遂馆居于严明府之水阁，到大历元年（766年）春移居夔州白帝城（今属重庆奉节）。同年秋，从成都调来夔州任都督的柏茂琳到任，对杜甫“频分月俸”，又不时派人给他送些瓜菜。大历二年（767年）三月，他在夔州瀼西买了四十亩果园，还带有“茅斋八九椽”， 柏氏又委托他代管东屯稻田百亩，生活比过去富裕一些了。 [100]\n从永泰二年（766年）暮春到大历三年（768年）孟春时节，亦即杜甫五十五岁至五十七岁的时候。在不到两年时间中，杜甫共写作了四百余首诗，不仅数量上达到高潮（在现存一千四百多首杜甫诗作中占了将近三分之一） [102]，诗的内容形式 也颇具特色。他回忆、反思了自己前半生生活经历和创作历程，写了《壮游》《昔游》《往在》《遣怀》等自传性的长篇，历史的光明与黑暗与 自己的爱憎倾向融合在一起，酝酿出无限的沉痛与辛酸。他仍然是“穷年忧黎元”的诗人，但他晚年的诗除描述“千家野哭”“万国征戍”而外，更特别关心人才，特别是能拨乱反正、真正忧国爱民的人才，这从《同元使君舂陵行》《赠李十五丈别》可以看出。而《祭故相国清河房公文》《八哀诗》《寄韩谏议注》等诗，则反映了他的人才观。这一时期，杜甫还写了不少夔府景物、气候、风土、民生疾苦的诗篇，并努力探求七律这种形式的艺术表现力，创作了《咏怀古迹五首》《诸将五首》《秋兴八首》等篇章。 [100]","a":"","chunkIndex":11,"datasetId":"66ee8939b2e1e065a337800e","collectionId":"66ee9a2eb2e1e065a33784e5","sourceId":"66ee9a2eb2e1e065a33784e2","sourceName":"dufu.txt","score":[{"type":"embedding","value":0.1685832440853119,"index":9}],"tokens":827},
'''




