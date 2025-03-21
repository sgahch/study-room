---

# 基于Django的自习室预约管理系统

## 项目简介

本项目是第二十四届“中国软件杯”校赛参赛作品，旨在开发一个基于Django的自习室预约管理系统，帮助高校学生和教务管理人员高效管理自习室资源。系统提供用户注册与登录、自习室查询、预约与取消、签到打卡等功能，支持实时监控自习室使用情况，优化资源分配。

## 目录

1. [需求分析](#需求分析)
2. [概要设计](#概要设计)
3. [详细设计](#详细设计)
4. [测试报告](#测试报告)
5. [安装及使用](#安装及使用)
6. [项目总结](#项目总结)

## 需求分析

### 1.1 开发背景

随着高校学生人数的增加，自习室资源的需求不断上升，传统的人工管理方式效率低下。本项目旨在开发一个智能化的自习室预约系统，帮助学生快速预约空闲自习室，减少排队等待时间，提高资源使用率。

### 1.2 面向用户

• **学生**：需要一个简单易用的预约平台。
• **教务管理人员**：需要一个高效管理自习室资源的工具。

### 1.3 主要功能

1. 用户注册与登录
2. 自习室查询
3. 预约与取消
4. 签到打卡

### 1.4 主要性能

1. 响应速度：系统应保证在高并发情况下仍能快速响应用户请求。
2. 数据处理：系统需要能够处理大量用户数据，保证数据的准确性和安全性。
3. 流畅的用户交互体验：界面设计需简洁易用，使用户操作直观明了。

### 1.5 竞品分析

| 维度 | 我们的系统 | 竞品A (timing) | 竞品B(番鱼) | 竞品C(同桌) |
| --- | --- | --- | --- | --- |
| 功能完整性 | 卓越 | 良好 | 基础 | 一般 |
| 用户体验 | 极佳 | 中等 | 较差 | 中等 |
| 响应速度 | 迅速 | 缓慢 | 缓慢 | 中等 |
| 数据安全 | 坚固 | 脆弱 | 中等 | 脆弱 |

### 1.6 总结

我们的自习室预约系统在功能完整性、用户体验和数据安全方面具有明显优势。未来，我们将继续优化系统性能，增强用户满意度。

## 概要设计

### 2.1 功能模块结构图

通过对需求分析的调查研究，确定了系统的总体功能结构。

### 2.2 调用关系

#### 2.2.1 用户模块

• **登录注册**：用户输入登录信息，系统验证后授予登录权限。
• **预约座位**：用户选择预约时间和座位，系统更新座位状态。
• **警告记录**：记录用户违反自习室规则的行为。
• **签到**：用户到达自习室后进行签到操作。
• **修改密码**：用户可以修改自己的登录密码。

#### 2.2.2 管理员模块

• **预约管理**：管理员可以查看、修改和取消用户的预约。
• **自习室管理**：管理员可以查看、修改自习室的设置。
• **签到码管理**：管理员可以生成和重置签到码。
• **用户管理**：管理员可以增加、删除和查询用户信息。
• **提示管理**：管理员可以发布和管理自习室的通知信息。
• **警告记录**：管理员可以查询和增删警告信息。

## 详细设计

### 3.1 界面设计

#### 3.1.1 用户界面

• **登录注册界面**：简洁的登录表单，包含用户名和密码输入框。
• **预约座位界面**：显示自习室列表，用户选择自习室和座位后完成预约。
• **签到界面**：用户输入签到码签到，显示签到成功或失败的提示信息。
• **修改密码界面**：用户输入旧密码和新密码，确认后提交修改。

#### 3.1.2 管理员界面

• **管理员登录界面**：简洁的登录表单，包含用户名和密码输入框。
• **管理预约界面**：显示所有用户的预约列表，提供查看、修改和取消操作。
• **管理自习室界面**：显示自习室的详细信息，提供表单用于更新自习室设置。
• **管理签到码界面**：显示当前签到码。
• **管理用户界面**：显示用户列表，提供查看、修改和取消操作。
• **管理通知界面**：提供文本框用于输入通知内容，并发布。

### 3.2 数据库设计

#### 3.2.1 数据表结构

• **用户表(Student)**：存储用户信息。
• **预约表(Bookings)**：存储预约信息。
• **自习室表(Rooms)**：存储自习室信息。
• **签到码表(SignCodes)**：存储签到码信息。
• **警告表(Intergal)**：存储警告记录。
• **通知表(Text)**：存储通知信息。

#### 3.2.2 ER关系图

• **用户 - 预约**：一对多关系，一个用户可以创建多个预约。
• **预约 - 自习室**：多对一关系，多个预约可以关联到同一个自习室。
• **预约 - 签到码**：一对多关系，一个预约可以使用多个签到码。
• **警告记录 - 学生**：一对多关系，一个学生可以发出多个警告记录。
• **通知 - 学生**：一对多关系，一个学生可以收到多个通知。

### 3.3 关键技术

#### 3.3.1 前端技术

• HTML、CSS、JavaScript：用于构建用户界面。
• Django 模板引擎：用于生成动态网页。

#### 3.3.2 后端技术

• Django 框架：构建系统的业务逻辑。
• Python 语言：编写业务逻辑代码。

#### 3.3.3 Django 框架

• 模型-视图-模板（MVT）架构：快速高效开发 Web 应用。
• ORM（对象关系映射）：简化数据库操作。

#### 3.3.4 MySQL 数据库

• 事务管理：确保数据的一致性和完整性。
• 索引优化：提高查询效率。

## 测试报告

### 4.1 测试概述

本测试报告概述了自习室预约管理系统的主要测试过程、结果及其修正措施。

### 4.2 测试的意义

测试确保软件产品的质量，通过发现和修复缺陷来提高软件的稳定性和可靠性。

### 4.3 系统测试

#### 4.3.1 测试环境

• 软件环境：Python3.12，Django5.1，MySQL8.0。
• 网络环境：100Mbps 宽带连接。

#### 4.3.2 PC 端测试过程

• **功能测试**：用户注册与登录、座位预约、签到功能、密码修改、管理员功能。
• **性能测试**：并发用户测试、数据库查询性能。
• **可用性测试**：界面友好性、错误处理。

#### 4.3.3 移动端测试过程

• **功能测试**：用户注册与登录、座位预约、签到功能、密码修改、管理员功能。
• **问题**：防火墙设置、网络配置问题、权限问题。

## 安装及使用

### 5.1 安装环境要求

• 操作系统：Windows10。
• Python 版本：Python3.6 及以上版本。
• 数据库：MySQL5.7 或更高版本。

### 5.2 安装过程

1. 安装 Python 和 pip。
2. 安装 Django：`pip install django`。
3. 设置数据库：安装 MySQL 服务器，并创建一个新的数据库。
4. 配置数据库：编辑 `your_project/settings.py` 文件，更新数据库配置。
5. 数据库迁移：`python manage.py makemigrations`，`python manage.py migrate`。
6. 创建管理员用户：`python manage.py createsuperuser`。
7. 运行开发服务器：`python manage.py runserver`。

### 5.3 主要流程

1. 开发环境搭建。
2. 代码开发：遵循 Django 的 MVT 架构。
3. 部署到生产环境：确保数据库、静态文件和媒体文件正确配置。
4. 日常维护：监控应用性能，定期备份数据库。

### 5.4 典型使用流程

1. 用户访问：通过浏览器访问自习室预约系统的网址。
2. 用户注册/登录：注册账户或使用已有账户登录系统。
3. 自习室查询与预约：查询自习室的实时状态，并进行预约操作。
4. 签到打卡：到达自习室后进行签到操作。
5. 管理员管理：登录后台，进行预约管理、自习室设置、用户管理、签到码等操作。

## 项目总结

### 6.1 项目协调与任务分解

采用敏捷开发方法，将项目分解为多个小的、可管理的迭代周期。

### 6.2 技术难题

在实现高并发用户访问和数据库性能优化方面遇到技术难题，通过技术研讨会和开源社区资源解决。

### 6.3 水平提升

团队成员的技术能力显著提升，加深了对 Web 开发的理解。

### 6.4 升级演进

计划引入人工智能技术，预测自习室的使用高峰，并探索移动端应用的开发。

### 6.5 商业推广

通过校园宣传和社交媒体平台提高项目知名度，与学校管理部门合作推广。

### 6.6 结语

本项目是技术挑战和团队协作的平台，未来将继续优化产品，提升用户体验，积极探索新技术。

---
