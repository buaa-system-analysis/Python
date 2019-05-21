## 2019-05-21 :

#### ������UserControl.py����Ҫ�µĽӿڣ�ԭ�е�editInfo����ô�����ˣ�

> ###�༭�û���Ϣ editUserInfo
> ####����˵��
> + (int)userID : �û�Ψһ��ʶ��ID
> + (JSON)data : ��Ҫ�޸ĵ����ݣ�Ҫ�Ķ����ֶξ��ж����ֶΣ������޸�name�ֶ�Ϊzyw��password�ֶ�Ϊ123456�����������޸ĵĻ���data����{"name":"zyw","password":"123456"}
>
> ####����ֵ˵��
> + (bool)success : �����Ƿ�ɹ��޸�


## 2019-05-20 ��

#### ������ScholarControl.py���鷳���޸�һ��app.py�Ľӿ�

> ���Ľӿ�����
>
> 
>
> ### editScholarInfo(scholarID, data):
>
> data��һ��json��������һ����ѧ��Ҫ�޸ĵ�������Ϣ������ID��������Ҫ�޸�nameΪa��organizationΪb��data����{ "name" : "a","organization" : "b" } ����
>
> ����ֵ��һ��bool��ʾ�Ƿ��޸ĳɹ�
>
> ### authenticate(userID��scholarID, email):
>
> ����ֵΪ�Ƿ�ɹ�����˸���֤��Ϣ�������Ƿ���֤�ɹ���
>
> 
>
> ### addScholar(name):
>
> ͨ��name�ֶ��½�һ���µ�ѧ�ߣ���ʱ�����ֶλ����϶��ǿգ����Ҫ˳����������Ϣ�����editScholarInfo������ֵΪ��ѧ�ߵ�scholarID
>
> 
>
> ### findScholarByKwd(kwd):
>
> ͨ���ؼ��ֲ���ѧ�ߣ��᷵��ȫ����Ϣ����id��kwdΪ''ʱ�᷵��ȫ��ѧ�ߵ���Ϣ��ͨ��������Ի�ȡidȻ��editScholarInfo





## 2019-05-19 ��

#### ������CollectionControl.py

> �����getPaperList(userID,paperListID)����
>
> ͨ��userID��paperListID���ظ�list���������ĵ���ϸ��Ϣ��
>
> ���ظ�ʽ��list
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

> �����getSubscribeList(userID)����
>
> ͨ��userID���ظ�user��ע������ѧ�ߵ���ϸ��Ϣ��
>
> ���ظ�ʽ��list
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





## 2019-05-18 ��

#### ������ResourceControl.py

>�����findComment(resourceID)����
>
>ͨ��Paper��_id�������е����ۡ�
>
>���ظ�ʽ��list
>
>[{
>
>?	"userID" : �������۵��û�,
>
>?	"resourceID" : ��ƪ���ĵ�ID,
>
>?	"content" : ��������,
>
>?	"time" : ���۵�ʱ��
>
>}...]
