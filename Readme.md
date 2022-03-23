## 万门事件我要说的

对于万门童哲疑似跑路事件，大家很恐慌和愤怒，有些VIP用户甚至是一些学生

很多人表示自己VIP刚买没多久，一套课程都没有看完，没想到遇见了这样的事情

这样的事情出现后，很多人表示以后不再相信知识付费，不会再购买虚拟产品，互联网多年经营的诚信瞬间崩塌。

对于万门的员工，多数都是刚出校门的孩子，觉得万门是个很大的企业，放心把自己交给了万门，觉得自己也是为教育事业做贡献，结果...

对于万门的技术人员，我真的看见他们在用心维护、开发这这一个平台，但作为童哲，说不负责就不负责

对于那些录制课程的老师，他们真的在用心的录制，而且据说后期的费用万门都没有给结算。

突然的来临让所有人的舆论指向购买VIP的用户：
```
转自维权群

之前包括今天很多人骂或者嘲讽我们这些VIP学员蠢，贪心，智商欠费，人傻钱多什么的，
我们不违法，
不贪污，不杀人，
不放火，
不女票，
不贝者，
不抽，
我们只是认认真真，花了真金白银和时间，想要努力学习知识技能，
努力提升自己，
只是不幸遇到一个辜负大家信任的卑鄙无耻的人渣而已?
请问那些看客有什么资格来嘲讽，
来戏谑，
来幸灾乐祸，
来雪上加霜，
有时间你去微博，去百度，去帮受害者一起谴责那个卑鄙的落跑校长童哲呀？
躲在网络后面幸灾乐祸算什么东西？

之前的教培行业集体奔溃，现在是网络在职技能教育同样暴雷，
难道这次爆的是不是国人对中国教育，互联网经济和中 国企业家的可信度吗？
原来这些所谓互联网大咖，985/211名校校友也一样的言而无信，恬不知耻，毫无道德底线。

P2P网贷机构暴雷，你们可以幸灾乐祸，因为你不是行内员工，不是用户，不是受害者，你可以夸夸其谈，幸灾乐祸，冷嘲热讽，

互联网共享单车暴雷，你们可以幸灾乐祸，因为你不是行内员工，不是用户，不是受害者，你可以夸夸其谈，幸灾乐祸，冷嘲热讽，

实体教培机构暴雷，你们可以幸灾乐祸，因为你不是行内员工，不是学员，不是受害者，你可以夸夸其谈，幸灾乐祸，冷嘲热讽，

万门这个互联网教育机构暴雷，你们可以幸灾乐祸，因为你不是行内员工，不是学员，不是受害者，你可以夸夸其谈，幸灾乐祸，冷嘲热讽，

我不后悔我自己花钱报读万门VIP，这是我自己做的选择，我有能力承担今天被背叛，被欺骗的后果，
只是我想对那些置身事外的"人间清醒"，"事后诸葛亮"，"三姑老婆"，"苦口婆心一口一个早跟你说了"的观众说一句，谢谢您了，歇着吧。

对童哲说一声，你算什么男人! 你不配玷污"校长"这个词!

最后，希望政府各个部门能够重视这次重大群体性事件(3w多终身VIP用户+散户学员+各地区分公司员工，总金额可能超过五亿多)，不要放走一个坏人，该抓抓，该遣返遣返，该赔偿赔偿，
最低要求: 如果有可以执行的财产在支付万门大学员工拖欠工资之后，全部用于维护万门大学网络平台正常运作，因为里面的课程是很多老师和万门工作者的心血，不应该就此废止，

童哲也许真的是人渣，但是一个基于自我提升美好远景的平台是无辜的。

最后想抱一下我万门大学的同学们，感谢有你们，所以没那么难挨，期盼一切尽快解决，给这次童哲-万门危机一个圆满的结局。
```

### 在热搜上多多少少还是被网络暴力

> 这个世界的残酷在于，为什么受伤和被欺骗的人最后反而要背负伤痛和责任。
> 为什么那么多吃瓜的人面对明星事件正义凌然，而面对万门VIP这样的受害者，却想要冷嘲热讽？
> 最后希望骂我们的人清醒一下，别到时候你遇见不公平事情的时候没有人站出来为你发声。

### 使用
安装python

#### 安装依赖:
```
pip install requests
pip install js2py
pip install json
pip install sqlite3
```

#### 获取信息

Authorization.ini 写入Authorization的信息，注意下面不要带空格

拿一个网址举例：https://api.wanmen.org/4.0/content/courses/60dd2fb05254732b89b106af/catalogue

将60dd2fb05254732b89b106af复制到命令行运行

#### 运行

```
python run.py 60dd2fb05254732b89b106af
```

> 很多人觉得打包后的程序可能有后门/木马，所以大家使用命令行吧

### 包

pip install test-5.2.0.tar.gz
出现Successfully installed test-5.2.0时，你的包就安装好了！进入Python运行试一下
注意，使用包里的文件是使用from test import helloworld而不是直接导入import test