# flasytry 
这是 Yukun Dong 于 2022/6/4 创建的GitHub仓库，用于存储代码，记录学习进程。
进度没跟上的成员可以参考这里的代码进行体会。同时，本仓库的最大作用是分享自己操作和代码，后续希望能够实现共同编辑。

## 分工情况

2022/6/4

现在组内学习情况两极分化严重，积极的已经学了不少内容，而有的成员几乎为零。在这里，**所有成员在6月5日之前务必确立自己的定位**：

**1.摆烂者**  你在组内不用承担任何责任，可以把时间用在别处，最终与我们共享大作业成果，贡献度统一给为3%。

**2.追随者**  你不需要学习太多的知识，浅学一下以示态度，最终与我们共享大作业成果，贡献度依照学习情况给5%-8%。

**3.建设者**  首先，成为建设者需要门槛！！！如果你ddl很多且在后期无法保证足够的时间投入（每周至少15-20小时），我不建议你选择成为建设者。建设者与大作业项目本身直接挂钩，而且建设者之间水平差异不应太大，能力欠缺或者跟不上进度的组员不会被认为是建设者。建设者内部共享至少80%的贡献度。

现在，时间紧迫，请小组成员快速明确自己的定位，一旦确定，不能更改。请各位慎重考虑。

-----------------------------

[2022/6/5 凌晨更新]

根据组员的情况，可以确定的是本小组**无摆烂者**,人员分配情况综合个人意愿和前期的学习状况综合安排如下：

### 建设者

**[组长]董宇坤 PB21000237** 前期学习时长约25h,在组内接触Python较早，具有一定解决问题的能力；

**刘兆宸 PB21061373** 前期学习时长约30h，肯钻研，肯付出时间精力，接触过cpp，Python等，是小组的中坚力量；

**黄万超 PB21000209** 前期学习时长接近10h，对前端页面设计抱有兴趣，学习积极性高，编程基础好。

建设者内部任务分配再行商讨，方向上面黄万超在前端上面应有更多侧重，而另外二位则需要尽力顾及全栈。

### 追随者

**胡琦浩 PB21000235** 前期学习时长约3h；

**王悦果 PB21000236** 前期学习时长约3h；

**祝子涵 PB21000244** 前期学习时长约3h。

**追随者们的任务：** 不熟悉Python的同学建议先熟悉一下Python。大致了解flask框架，定性了解什么是数据库，能对一个Web应用的基本结构有一定认知即可。不需要投入过多时间,
**但也不要一问三不知**。后续可能在已有的博客系统上会衍生出我们个性化的功能，到时候需要各位追随者们出谋划策，提出宝贵想法和实践方案。

**附注：** 成员分工主要考虑的指标是成员**前期投入情况和现阶段的编程能力**，以上分工经过了慎重的考虑，不会做大的更改。

-----------------------------

目前，小组还处于学习阶段，有一套体系较为完备的博客系统可作为我们的参考：https://github.com/miguelgrinberg/flasky

后期在该博客系统的大框架之下，可以衍生出我们需要的功能。

## 代码说明
2022/6/4

利用`flask run`指令运行`main.py`可以在本地看到简单的欢迎页。试试看！

后续会不断更新。

2022/6/6

新增`mail_config.py`和`send_mail.py`。前者是发送邮件平台及端口的设置，运行后者即可实现邮件的发送。使用qq邮箱发送时请注意，要在邮箱内部启用smtp服务！

## 日志
before 2022/6/4

广泛查阅资料，确立小组的方向（Python+flask）；

环境搭建，学习flask和数据库的基本知识，做一些较为简单的操作；

修bug。

2022/6/4 

解决了cmd上跑`flask shell`的不少bug，能通过指令进行基本的创建和删除操作；

创建了本仓库；

参考书阅读推进到了Chapter 6，不久后可以上手博客系统。

2022/6/5

确定了小组分工。

2022/6/6

终于掌握了利用flask-mail发送电子邮件！
