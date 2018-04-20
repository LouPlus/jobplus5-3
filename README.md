# jobplus5-3

LouPlus Team 3 <https://www.shiyanlou.com/louplus/python>

## Contributors

- [ZFane](https://github.com/Z-Fane)

- [大鸡脖](https://github.com/liuzhibo)

- [jerry123je](https://github.com/jerry123je)

## Databases

> user表

字段           | 类型           | 注解
:----------- | :----------- | :-----
id       | INT(10)      | 用户ID
user_name     | VARCHAR(255) | 用户姓名
user_email    | VARCHAR(255) | 登录邮箱
_user_password | VARCHAR(255) | 登录密码
user_role     | INT(10)      | 用户角色
user_phone    | VARCHAR(255) | 用户电话
user_experience|VARCHAR(255) | 求职者工作经验
user_resume|VARCHAR(255) | 求职者简历链接
created      | DATETIME     | 数据创建时间
updated      | DATETIME     | 数据修改时间

>company表

字段           | 类型           | 注解
:----------- | :----------- | :-----
id       | INT(10)      | 用户ID
company_homepage |VARCHAR(20)|公司主页
company_field|VARCHAR(20)|公司领域
company_financing|VARCHAR(20)|公司融资情况
company_city|VARCHAR(20)|公司所在城市
company_logo|VARCHAR(20)|公司Logo链接
company_introduction|VARCHAR(1024)|公司一句话简介
company_description|VARCHAR(4096)|公司详细描述
company_slug|VARCHAR(20)|公司固定链接
user_id|INT(10)|对应用户
created      | DATETIME     | 数据创建时间
updated      | DATETIME     | 数据修改时间

> job表

字段             | 类型            | 注解
:------------- | :------------ | :-----
id          | INT(10)       | 工作ID
job_name        | VARCHAR(255)  | 工作名称
job_tag         | VARCHAR(255)  | 工作标签
job_description | VARCHAR(4096) | 工作描述
job_address     | VARCHAR(1024) | 工作地点
job_salary_l     | INT(10)       | 最低工资
job_salary_h     | INT(10)       | 最高工资
job_experience  | VARCHAR(255)  | 工作经历
job_education   | VARCHAR(255)  | 学历要求
job_company     | INT(10)       | 所属公司ID
created        | DATETIME      | 数据创建时间
updated        | DATETIME      | 数据修改时间

> delivery表

字段                | 类型       | 注解
:---------------- | :------- | :------
deliveryId        | INT(10)  | 投递ID
deliveryJob       | INT(10)  | 投递工作的ID
deliveryCompany   | INT(10)  | 投递公司的ID
deliveryJobseeker | INT(10)  | 投递人的ID
deliveryStatus    | INT(10)  | 投递状态
created           | DATETIME | 数据创建时间
updated           | DATETIME | 数据修改时间
