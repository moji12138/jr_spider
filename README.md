# jr_spider
今日头条文章爬取 生成docx文档
## 功能：
将今日头条的文章和悟空问答的页面生成docx格式的文档
- 头条文章 √
- 悟空问答 √
- 头条图集 ×
- 付费文章 ×
## 目录结构
```bash
|-JRspider.py   [spider类]
| 
|-documnet      [存放生成的docx文档]
|   xxx.docx
|   xxxxx.docx
|-img           [存放爬到的图片 文件名以MD5方式命名]
|   img1.jpeg
|   img2.jpeg
```
## 使用方法
1. import spider模块
```python3
  from JRspider import *
```
2. 调用工厂类
```python3 
  jrobj = JinRi.get(url)
```
