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
userId       | INT(10)      | 用户ID
userEmail    | VARCHAR(255) | 登录邮箱
userPassword | VARCHAR(255) | 登录密码
userRole     | INT(10)      | 用户角色
created      | DATETIME     | 数据创建时间
updated      | DATETIME     | 数据修改时间

> jobseeker表

字段              | 类型            | 注解
:-------------- | :------------ | :-----
jobseekerId     | INT(10)       | 求职者ID
jobseekerName   | VARCHAR(255)  | 求职者名称
jobseekerPhone  | VARCHAR(20)   | 求职者电话
jobseekerResume | VARCHAR(1024) | 简历链接
created         | DATETIME      | 数据创建时间
updated         | DATETIME      | 数据修改时间

> company表

字段                  | 类型            | 注解
:------------------ | :------------ | :-------
companyId           | INT(10)       | 公司ID
companyName         | VARCHAR(255)  | 公司名称
compangHomepage     | VARCHAR(1024) | 公司主页
companyField        | VARCHAR(20)   | 公司领域
companyFinancing    | VARCHAR(20)   | 公司融资情况
companyCity         | VARCHAR(20)   | 公司所在城市
companyLogo         | VARCHAR(255)  | 公司Logo链接
companyIntroduction | VARCHAR(1024) | 公司一句话简介
companyDescription  | VARCHAR(4096) | 公司详细描述
created             | DATETIME      | 数据创建时间
updated             | DATETIME      | 数据修改时间

> job表

字段             | 类型            | 注解
:------------- | :------------ | :-----
jobId          | INT(10)       | 工作ID
jobName        | VARCHAR(255)  | 工作名称
jobTag         | VARCHAR(255)  | 工作标签
jobDescription | VARCHAR(4096) | 工作描述
jobAddress     | VARCHAR(1024) | 工作地点
jobSalaryL     | INT(10)       | 最低工资
jobSalaryU     | INT(10)       | 最高工资
jobExperience  | VARCHAR(255)  | 工作经历
jobEducation   | VARCHAR(255)  | 学历要求
jobCompany     | INT(10)       | 所属公司ID
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
