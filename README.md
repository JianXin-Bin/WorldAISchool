# World AI School · 全球AI学习资源网站

精选全球AI学习资源，持续更新，为每个家庭打开AI学习之门。

项目标识与GitHub仓库名：`worldAIschool`。英文名：**World AI School**。中文名：**全球AI学习资源网站**。

一个面向家庭、家长、教师和学习者的 AI 学习资源导航网站。提供资源简介、主题分类、搜索和原站链接，帮助用户发现课程、教材、创造项目、公开代码项目与实操教程。

项目仓库：[JianXin-Bin/worldAIschool](https://github.com/JianXin-Bin/worldAIschool)。素材与第三方权利范围见 [素材与第三方说明](THIRD_PARTY_NOTICES.md)。网页演示地址将在部署及访问检查完成后补充。

## 当前版本

- 收录100条唯一资源，沿用原有 `RES-...` 稳定ID。
- 覆盖AI教育、WorkBuddy、豆包工作、千问办公、百度搭子与AI资讯，并提供GitHub项目等形式分类。
- 中文优先排序，支持关键词搜索、语言及获取方式筛选。
- 静态 HTML、CSS 和 JavaScript，无需数据库或支付后台。
- 本站导航全部免费；原站课程、工具的注册与收费条件以原站为准。
- 网站代码采用MIT许可证，允许在保留版权和许可声明的条件下修改、分发和商用。
- 本站维护者已于2026年10月22日明确要求公开其个人微信二维码和自愿支持1元的收款二维码，当前公开首页包含这两个入口。

“收录”不代表已逐项体验或担保质量。页面原有核验状态、来源更新日期、获取条件和访问提示被保留；本次打包没有重新核验100个外部网站。

## 快速开始

直接用浏览器打开根目录的 `index.html` 即可查看，不需要安装依赖。

如需修改资源数据：

1. 编辑 `data/resources.json`，保留已有资源ID。
2. 在项目根目录执行 `python scripts/build.py --config config/site.public.json --publish-owner-qr`，生成保留本站维护者二维码的 `index.html` 和 `dist/index.html`。如制作自己的副本，使用不含二维码的默认配置：`python scripts/build.py`。
3. 在浏览器检查分类、搜索和资源跳转，再提交修改。

构建脚本只使用 Python 标准库。建议安装当前仍受支持的 Python 3；本地还检查了旧版 Python 的构建兼容性。

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

## 部署

- WorkBuddy：将根目录 `index.html` 作为网页产物导入，按实际账号提供的轻量发布入口发布，核实费用、访问条件及有效期。
- GitHub Pages：可以把公开仓库的根目录设置为发布来源，不需要运行 Node 服务。
- 其他静态网站托管：上传生成的 `index.html` 即可。

具体步骤见 [部署说明](docs/deployment.md)。公开代码与生产网站托管可以分开选择；在 GitHub 公开代码并不要求将正式网站托管在 GitHub。

## 更新和参与贡献

欢迎提交新的资源、修正简介及报告失效链接。请保留原始来源，说明获取条件和实际核验状态。不要提交课程全文、付费文件、他人凭据或不明授权的素材。

请阅读 [贡献说明](CONTRIBUTING.md) 和 [资源字段说明](docs/data-schema.md)。

## 社群与自愿支持

本项目全部导航资源免费开放。本站维护者明确授权在此公开仓库及网页中展示以下两张图片：`assets/personal-wechat.png` 用于添加维护者、备注“AI交流”联系入群；`assets/wechat-donation-payment.png` 用于微信扫码自愿支持1元。支持不影响资源访问，不建立会员或自动扣款。

图片是静态收款码，页面提示的是建议金额1元，不代表二维码已经强制固定金额，也不代表本站可以自动核验到账。维护者未提供支付密钥，项目不包含支付后台。

Fork本项目时，请切换为自己的二维码或执行默认构建以隐藏相关入口，不要将本站维护者身份和收款信息冒充为自己的。

如需本地配置自己的二维码，可把图片放到 `assets/private/`，复制示例配置为 `config/site.local.json`，填入两个不同用途的图片相对路径，然后执行：

```sh
python scripts/build.py --config config/site.local.json --private-preview
```

此命令只写入被忽略的 `private-preview/index.html`，不覆盖公开入口。发布带二维码的公开页面必须显式传入 `--publish-owner-qr`。忽略规则无法清除历史提交中的内容，公开前仍须检查实际上传文件。

## 许可证和权利边界

本项目由维护者有权许可的网站程序代码及工程文档采用 **MIT许可证**，版权署名为承宇。MIT允许修改、分发及商业使用，但须保留版权和许可声明，不要求衍生版本必须免费或公开源码。

本项目的许可不会改变外部课程、仓库、文章、品牌标志及图片的原有许可。资源字段中的 `license` 记录原页面明确的信息；“未明确”不表示可以自由复制或商用。资源目录尚未单独指定数据许可证，不应把本站许可证当作外部内容的授权。

许可正文见 [LICENSE](LICENSE)，适用范围见 [许可说明](docs/licensing-options.md)，素材边界见 [素材及第三方说明](THIRD_PARTY_NOTICES.md)。生成的HTML同时包含代码、目录数据和图片，其中代码适用MIT，其余部分按各自的权利说明处理。
