# 发布与部署

本目录是独立静态网站项目，不依赖原知识库、原始Excel或 Node 服务端。公开仓库地址和生产网站网址是两件事，可分别管理。

## 发布前

先查看 release-checklist.md，核对实际上传范围及素材权利说明。Logo和首页插画同时嵌入生成的HTML。项目仓库为 https://github.com/JianXin-Bin/worldAIschool ，具体网页部署状态以Pages设置和实际访问结果为准。

## WorkBuddy

把根目录 index.html 交给 WorkBuddy，要求沿用现有文件、优先使用轻量发布、实际打开公网链接并核验分类和搜索。平台是否免费、链接有效期、访问限制和域名支持，以当前账号和官方规则为准，不承诺永久免费。

维护者已明确要求公开个人微信及自愿支持1元的收款二维码，当前根目录HTML包含这两个入口。更新本站资源时执行 `python scripts/build.py --config config/site.public.json --publish-owner-qr`；如发布自己的副本，执行不带参数的 `python scripts/build.py` 生成不含维护者二维码的通用版本。`private-preview/index.html` 仍用于另行配置的私人预览，不提交到仓库。

官方依据：[WorkBuddy轻量发布](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Library/Lightweight-Publish)。

## GitHub Pages

1. 在GitHub创建公开仓库，命名 worldAIschool。展示名称为World AI School，中文名为全球AI学习资源网站。
2. 将本项目根目录下的文件和子目录上传到仓库根目录，保留点开头的配置文件；不要把整个知识库或ZIP本身作为源码上传。
3. 打开仓库 Settings → Pages，选择可用的分支发布方式，选实际主分支和根目录作为发布来源，保存。
4. 等待GitHub显示发布结果，使用其实际提供的网址。项目站点常见地址为 https://用户名.github.io/worldAIschool/，不是已经替你注册的网址。
5. 用未登录的浏览器和手机检查访问、图片、分类、搜索、资源链接及404情况。

根目录包含生成的 index.html 和 .nojekyll，不需要额外配置Python构建工作流。修改 data/resources.json 后在本地重新构建并提交 index.html。

GitHub官方确认Pages可托管静态HTML、CSS与JavaScript，GitHub Free支持公开仓库使用；访问表现需以目标用户实际网络为准。

官方依据：[GitHub Pages介绍](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)。

## 上传方式

初次使用可以通过GitHub网页上传此项目目录中的文件。熟悉Git后，在这个独立项目目录中初始化和提交；不要在完整Obsidian知识库根目录执行全量上传。

本文是部署说明。仓库、提交和网页发布是否成功，均须以平台实际状态为准；自定义域名没有自动注册或绑定。
