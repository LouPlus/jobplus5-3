# jobplus5-3

LouPlus Team 3 <https://www.shiyanlou.com/louplus/python>

## Contributors

- [ZFane](https://github.com/Z-Fane)

- [大鸡脖](https://github.com/liuzhibo)

- [jerry123je](https://github.com/jerry123je)

## Databases

> user表

字段           | 类型           | 注解
:----------- | :----------- | :---
userId       | INT(10)      | 用户ID
userEmail    | VARCHAR(255) | 登录邮箱
userPassword | VARCHAR(255) | 登录密码
userRole     | INT(10)      | 用户角色

> jobseeker表

字段             | 类型           | 注解
:------------- | :----------- | :----
jobseekerId    | INT(10)      | 求职者ID
jobseekerName  | VARCHAR(255) | 求职者名称
jobseekerPhone | VARCHAR(20)  | 求职者电话

> company表

字段                  | 类型            | 注解
:------------------ | :------------ | :-------
companyId           | INT(10)       | 公司ID
companyName         | VARCHAR(255)  | 公司名称
companyCity         | VARCHAR(20)   | 公司所在城市
companyLogo         | VARCHAR(255)  | 公司Logo链接
companyIntroduction | VARCHAR(1024) | 公司一句话简介
companyDescription  | VARCHAR(4096) | 公司详细描述
                    |               |
