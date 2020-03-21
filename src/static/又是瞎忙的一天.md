# 又是瞎忙的一天

先来总结一下今天做的事吧

- 将博客迁移至洛杉矶VPS，并成功安装[VOID主题](https://github.com/AlanDecode/Typecho-Theme-VOID)（~~说多了都是泪~~）
- 将上次（~~也就是上周~~）未完成的基于GitHub和[Maverick](https://github.com/AlanDecode/Maverick)的个人日记整好了，用的是默认的[Galileo](https://github.com/AlanDecode/Maverick)主题
- 利用Typora的新功能，将PicGo和Typora结合，实现图片的自动上传和复制链接

一件一件来说吧

## 迁移博客

入坑Typecho已经5天了，回想一下具体怎么入的坑，也确实觉得有些好玩。首先是不知道怎么在Bing搜索结果中找到了[风也](https://eas1.cn/)的博客，然后觉得网站做的很不错，就深入浏览了一下，当时我看到了它的一篇文章，[从零开始免费搭建个人博客](https://eas1.cn/posts/94.html)，便知道了Typecho这个轻量级博客程序。之前被GitHub Pages和Hexo整的心累，一个是访问速度极慢（当时还不知道有cdn这个东西），一个是国内的百度爬虫到不了GitHub Pages，写的东西国内搜索引擎收录不了，所以不太想在那上面写了。碰巧博文中介绍了一种免费的方法，于是抱着试一试的心态就入坑了。

起初用的是[HoRain](https://webs.horain.net/)的虚拟主机，100M数据库，100M存储空间，香港服。但博客网站访问速度时好时坏，主机控制界面响应太慢，到后面忍受不了就自己租服务器了，用的还是他家的。

系统选择的是Ubuntu16.04，按照Typecho中文网的[教程](https://www.typechodev.com/servers/nginx_or_apache.html)来做的，有几个坑折磨了我好久。

- 不知道为什么，安装软件的时候默认选择的是阿里云的镜像源，然后无法访问，不知道是不是因为墙的原因，我后面换了美国的源就好了

- 这个配置文件最好不要带`.`，否则nginx好像识别不出他是个配置文件
  ![image-20200322001041167](https://cdn.jsdelivr.net/gh/kepontry/picbed/img/20200322001042.png)
  
- 启用VOID插件需要安装mbstring模块

- 眼瞎了，我一直把上面的那个包看成了标题，把底下两个源码包上传了

- ![image-20200322001800195](https://cdn.jsdelivr.net/gh/kepontry/picbed/img/20200322001801.png)

## 个人日记

  这个是按照[《完全用 GitHub 写博客》](https://blog.imalan.cn/archives/blog-with-github/)这篇文章写的，文章写的不算是教程吧，更算是原理讲述吧，他的git仓中讲的才是step-by-step的教程。他采用了一种不同于Hexo的博客构建方式，但是对于我这个小白用户来说，我主要是看中了它集成了jsDelivr的cdn服务，然后主题也很好看。

不过在使用过程中，发现了几处问题

- 在绑定自己的域名的时候，应该要把这个前缀改成`/`，原来这样写应该是针对`username.github.io`默认域名的情况
- 绑定的域名在GitHub Actions构建后就没了，猜测是提交的时候把CNAME文件给搞掉了，后续在想一想该怎么搞

![image-20200321233623321](https://cdn.jsdelivr.net/gh/kepontry/picbed/img/20200321233624.png)

## Typora加入PicGo联动功能

这个真的是markdown玩家的一大福音啊，直接将图片拖到Typora中再点击上传图片，就可以自动填充图片链接。如果结合Snipaste，还可以直接将截图从剪贴板复制过来，不用将截图存在本地，真的太方便了。

![image-20200321233421179](https://cdn.jsdelivr.net/gh/kepontry/picbed/img/20200321233506.png)

## 最后

写了快四五十分钟，有些累了，反过头来发现这更像一篇技术型的文章了。小半年没写博客了，文思如泉涌，一下挡不住。后续我将记录一下生活中的事。