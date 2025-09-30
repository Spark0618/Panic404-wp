> Markdown 是一种轻量级标记语言，用简单直观的符号就能实现标题、列表、链接、代码等排版效果，它语法易学、跨平台通用、文件是纯文本便于版本管理，并且能方便地转换成 HTML、PDF 等多种格式，因此既能让作者专注内容创作，又能快速得到美观、结构清晰的文档。

## 要求&注意事项

1. 该静态网站使用mkdocs工具生成，Writeup**必须使用md文件编写**，关于markdown语法可以自行搜索学习，五分钟左右便可掌握基本语法，只需会**多级标题、图片链接、多级列表**即可。

2. 编写的md文件需要通过 `lint-md` 进行语法校验，该步骤未来会考虑加入github workflow自动审查，目前你只需要保证你的md编辑器能正确渲染就行。

3. 编写的wp最后需要**加上署名**，即在文件的最后另起一行粘贴如下代码，其中[username]替换为你的github用户名，实现效果可参考已上传wp [unfinish](../../web/unfinish)末尾，未来也考虑使用github workflow进行自动化署名。
   ```markdown
   <p style="text-align: right;">
   by. [username]
   </p>
   ```

4. 注意md文件并不内嵌图片，因此图片链接推荐使用网络图片或将本地图片上传至图床（记得**脱敏！！！**），或者将图片同时上传至wp仓库中（**临时方案**），前期我们统一在各方向的writeup同级目录下的Images文件夹下，新建一个与你的writeup同名的文件夹，用于存放引用图片（**临时方案**，我们会尽快将图片转移至另一个专门用于存放图片的仓库中，并简化上传流程），参考已上传wp结构如下
   ```shell
   docs
   ├─assets
   │  └─js
   ├─data
   ├─web
   │  │  unfinish.md
   │  │  unseping.md
   │  └─images # 这个文件夹下面新建对应文件夹放图片
   │      ├─unfinish
   │      │    flag输出.png
   │      │    hackbar.png
   │      │    注册页.png
   │      └─unseping
   │           topic.png
   └─帮助
   ```

5. 静态网站的标题默认为md文件名，**文件名需要为题目名称**（参考已上传wp），wp中不要使用一级标题，会覆盖静态网站默认标题

6. 提交pr前可在仓库下使用 `mkdocs serve` 指令预览，出现报错可复制询问LLM

## 推荐的md编辑器

- Typora（可自行搜索免费版教程）

- Obsidian （注意其独有的图片链接格式）
- VsCode + markdown插件