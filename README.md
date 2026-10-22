# World AI School · 全球AI学习资源网站

精选全球AI学习资源，持续更新，让每个家庭，都能共享全球AI学习资源。

## 当前版本

- 目前，精选了全球100个AI网站的学习资源。
- 覆盖AI教育、WorkBuddy、豆包工作、千问办公、百度搭子与AI资讯。
- 支持关键词搜索、语言及获取方式筛选。
- 本站导航全部免费；原站课程、工具的注册与收费条件以原站为准。
- 网站代码采用MIT许可证，允许在保留版权和许可声明的条件下修改、分发和商用。

## 快速开始

直接用浏览器打开根目录的 `index.html` 即可查看，不需要安装依赖。


## 目录结构

```text
worldAIschool/
├── README.md
├── LICENSE
├── THIRD_PARTY_NOTICES.md
├── CONTRIBUTING.md
├── .gitignore
├── .nojekyll
├── index.html                 # 可直接展示的公开版本，自动生成
├── src/template.html          # 页面模板，样式和交互源代码
├── data/resources.json        # 精选资源目录，100条初始记录
├── config/site.example.json   # 不含二维码的通用示例配置
├── config/site.public.json    # 本站维护者明确授权公开的二维码配置
├── assets/                    # 当前Logo、插画及素材权利说明
├── scripts/build.py           # 可移植构建脚本，不依赖原始Excel
├── docs/
│   ├── deployment.md          # 发布到WorkBuddy或静态托管服务
│   ├── data-schema.md         # 字段与更新约定
│   ├── release-checklist.md   # 首次公开前检查
│   └── licensing-options.md  # 已确认的MIT许可范围
└── .github/ISSUE_TEMPLATE/
    └── resource.yml           # 新增资源、纠错及失效链接反馈
```

`dist/` 是忽略的构建产物。根目录 `index.html` 作为首次静态展示入口保留在仓库，更新资源后须重新生成并一并提交。

## 更新和参与贡献

欢迎全球开发人士来参与共创，提交新的资源、修正简介及报告失效链接。不要提交付费文件、他人凭据或不明授权的素材。

## 社群与自愿支持

本项目全部AI学习资源免费开放。同时，构建了相关“AI交流学习群”，供大家学习交流，如果想进群，可扫描下方二维码，然后备注"AI交流"联系入群；

 <img src="assets/personal-wechat.png" width="300" alt="个人微信二维码">

最后，如果本项目对你有用的话，如果想捐款，支持网站运维，持续更新全球AI学习资源，可扫描下方二维码，扫码捐款，感谢支持。

 <img src="assets/wechat-donation-payment.png" width="300" alt="微信捐款二维码">


## 许可证和权利边界

本项目由维护者有权许可的网站程序代码及工程文档采用 **MIT许可证**，版权署名为承宇。MIT允许修改、分发及商业使用，但须保留版权和许可声明，不要求衍生版本必须免费或公开源码。

本项目的许可不会改变外部课程、仓库、文章、品牌标志及图片的原有许可。资源字段中的 `license` 记录原页面明确的信息；“未明确”不表示可以自由复制或商用。资源目录尚未单独指定数据许可证，不应把本站许可证当作外部内容的授权。

许可正文见 [LICENSE](LICENSE)，适用范围见 [许可说明](docs/licensing-options.md)，素材边界见 [素材及第三方说明](THIRD_PARTY_NOTICES.md)。生成的HTML同时包含代码、目录数据和图片，其中代码适用MIT，其余部分按各自的权利说明处理。
