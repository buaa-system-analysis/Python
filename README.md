# Python
Backend of Platform

## 2019-05-19 ：

#### 更新了CollectionControl.py，请添加app.py的接口

> 添加了getPaperList(userID,paperListID)函数
>
> 通过userID和paperListID返回该list中所有论文的详细信息。
>
> 返回格式：list
>
> [{
>
> 			"_id":ID,
> 	        "title":title,
> 	        "authors":authors,
> 	        "abstract": abstract,
> 	        "publishment":publishment,
> 	        "citation":citation,
> 	        "field":field,
> 	        "price":price,
> 	        "fulltextURL":fulltextURL
> ​	"resourceID" : 该篇论文的ID,
>
> ​	"content" : 评论内容,
>
> ​	"time" : 评论的时间
>
> }...]

> 添加了getSubscribeList(userID)函数
>
> 通过userID返回该user关注的所有学者的详细信息。
>
> 返回格式：list
>
> [{
>
> ```
> 		"_id":ID,
>         "name":name,
>         "organization": organization,
>         "resourceField": resourceField
> ```
>
> }...]





## 2019-05-18 ：

#### 更新了ResourceControl.py

>添加了findComment(resourceID)函数
>
>通过Paper的_id返回所有的评论。
>
>返回格式：list
>
>[{
>
>​	"userID" : 该条评论的用户,
>
>​	"resourceID" : 该篇论文的ID,
>
>​	"content" : 评论内容,
>
>​	"time" : 评论的时间
>
>}...]

