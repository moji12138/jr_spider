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
1. 安装requests，python-docx，beautifulsoup库
```bash
  # python3 -m pip install requests
  # python3 -m pip install python-docx
  # python3 -m pip install BeautifulSoup4
```
2. 调用
```python3
  from JRspider import *
  url = "https://www.toutiao.com/a6691121448884371982/"   #今日头条或悟空问答(回答)的链接
  jrobj = JinRi.get(url)  #调用工厂类的get方法
  docName = jrobj.get_docx()    #调用get_docx()方法生成文档 返回文档名字符串
  print(docName)    #打印文件名 非None即为已经生成
```
3. 查看文件
在docment目录中查看 不再赘述
