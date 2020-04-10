# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "git",
    "url": "https://github.com/Kepontry/Maverick-Theme-Galileo.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "kepontry/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "Kee's Diary"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-03-21T16:51+08:00"
author = "Kee"
email = "1431629699@qq.com"
author_homepage = "http://diary.kepontry.xyz"
description = "Be Yourself,Be Prepared!"
key_words = ['Kee', 'Diary']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "Kee's Blog",
        "url": "http://blog.kepontry.xyz",
        "brief": "Taste The World."
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
#    {
#        "name": "Twitter",
#        "url": "https://twitter.com/AlanDecode",
#        "icon": "gi gi-twitter"
#    },
    {
        "name": "GitHub",
        "url": "https://github.com/Kepontry",
        "icon": "gi gi-github"
    },
#    {
#        "name": "Weibo",
#        "url": "https://weibo.com/5245109677/",
#        "icon": "gi gi-weibo"
#    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
