# HMTL

## HTML是什么
    HTML是HyperText Mark-up Language的首字母缩写，即超文本标记语言
    HTML不是编程语言，而是一种标记语言
    超文本指的是超链接，标记指的是标签，是一种用来制作网页的语言，这种语言由一个个标签组成
    用这种语言制作的文件保存的是一个文本文件，文件的扩展名为.html或者.htm
    html文档也叫Web页面，其实就是一个网页，html文件用编辑器打开显示的是文本，可以用文本的方式编辑它
    如归用浏览器打开，浏览器会按照标签描述内容将文件渲染成网页，显示的网页可以从一个网页链接跳转到另外一个网页

## HTML基本结构
    HTML是由：标签和内容构成
    HTML标签(标记)的语法是由"<"和">"括起来
    HTML标签有两种：
        双标签：<标签名>....</标签名>
        单标签：<标签名/>
    HTML标签中还可以添加属性：
        <标签名 属性名1 = "值1" 属性名2 = "值2" 属性名n = "值n"> ....</标签名>
    HTML标签规范：
        标签名小写，属性使用双引号、标签要闭合。规范不遵守浏览器不会报错，会尽量解析，大不了不显示效果
## HTML举例
```html
<!DOCTYPE html>
<html lang="en">
    <head> <!--head对当前网页进行说明，不会呈现在页面中-->
        <meta charset="UTF-8">
        <title>网页标题</title>
        <!-- 此处可以写各种网页头属性、CSS样式和JavaScript脚本等...-->
    </head>
    <body>
        <h1>我的第一个网页</h1> <!--该段文字将显示在网页中-->
        <a href="https://www.baidu.com">百度</a>
    </body>
</html>
```

## HTML注释
    html文档代码中可以插入注释，注释是对代码的说明和解释
    <!--这就是唯一的一种HTML的注释了, 可以多行注释-->

## HTML中head头部信息设置
    设置网页编码：<meta charset="utf-8"/>
    关键字：<meta name="Keywords" contene="关键字"/>
    描述：<meta name="Description" content="简介、描述"/>
    网页标题：<title>本网页标题</title>
    导入CSS文件：<link type="text/css" rel="stylesheet" href="**.css"/>
    CSS代码：<style type>="text/css"嵌入css样式代码</style>
    JS文件或代码：<script>...</script>
    ......

