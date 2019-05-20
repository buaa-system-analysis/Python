# Python
Backend of Platform



## 2019-05-20 ：

#### 更新了ScholarControl.py，麻烦请修改一下app.py的接口

> 更改接口如下
>
> 
>
> ### editScholarInfo(scholarID, data):
>
> ​	data是一个json，包含了一整个学者要修改的所有信息（除了ID），比如要修改name为a，organization为b，data就是{ "name" : "a","organization" : "b" } 这样
>
> ​	返回值是一个bool表示是否修改成功
>
> ### authenticate(userID，scholarID, email):
>
> ​	返回值为是否成功添加了该认证信息（不是是否认证成功）
>
> 
>
> ### addScholar(name):
>
> ​	通过name字段新建一个新的学者，返回值为该学者的scholarID
>
> 
>
> ### findScholarByKwd(kwd):
>
> ​	通过关键字查找学者，会返回全部信息包括id，kwd为''时会返回全部学者的信息，通过这个可以获取id然后editScholarInfo





> 通过userID和paperListID返回该list中所有论文的详细信息。
>
> 返回格式：list
>
> [{
>
> ```
> 	"_id":ID,
>         "title":title,
>         "authors":authors,
>         "abstract": abstract,
>         "publishment":publishment,
>         "citation":citation,
>         "field":field,
>         "price":price,
>         "fulltextURL":fulltextURL
> ```
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
>      "name":name,
>      "organization": organization,
>      "resourceField": resourceField
> ```
>
> }...]



## 2019-05-19 ：

#### 更新了CollectionControl.py

> 添加了getPaperList(userID,paperListID)函数
>
> 通过userID和paperListID返回该list中所有论文的详细信息。
>
> 返回格式：list
>
> [{
>
> 		"_id":ID,
> 	        "title":title,
> 	        "authors":authors,
> 	        "abstract": abstract,
> 	        "publishment":publishment,
> 	        "citation":citation,
> 	        "field":field,
> 	        "price":price,
> 	        "fulltextURL":fulltextURL
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

