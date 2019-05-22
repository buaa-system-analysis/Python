## 2019-05-22:

#### 前端新需求：
> id非自定义情况下返回时强制转化为string或者干脆不返回

> ScholarControl中编辑学者信息缺接口，只预留了一个不明确的data

> CollectionControl

> manageCollection中，添加其他人的列表的接口不对，应当设立额外的字段，userID为主用户id，还应该有一个userID字段与paperListID联合确立一个paperList

> 缺少getPaperList的接口，即根据userID得到他的所有paperList，分为createList和collectionList（自己创建的和收藏的他人的）

## 2019-05-21:

#### 前端新需求：
> 需要修改用户个人信息，包括：姓名、生日、性别、email、电话、introduction、密码；
> 原来接口包括： introduction 和 organization，其中 organization 前端暂时不需要
> 希望接口是对单个信息进行修改
