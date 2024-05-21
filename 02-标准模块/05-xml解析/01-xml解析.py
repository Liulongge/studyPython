# 参考:
# https://www.runoob.com/python/python-xml.html
# http://t.csdnimg.cn/NY3oz

# 什么是 XML？
# XML 指可扩展标记语言（EXtensible Markup Language）。
# XML 是一种很像HTML的标记语言。
# XML 的设计宗旨是传输数据，而不是显示数据。
# XML 标签没有被预定义。您需要自行定义标签。
# XML 被设计为具有自我描述性。
# XML 是 W3C 的推荐标准

# XML 和 HTML 之间的差异
# XML 不是 HTML 的替代。
# XML 和 HTML 为不同的目的而设计：
# XML 被设计用来传输和存储数据，其焦点是数据的内容。
# HTML 被设计用来显示数据，其焦点是数据的外观。

# XML 用途
# XML 应用于 Web 开发的许多方面，常用于简化数据的存储和共享。
# 1.XML 把数据从 HTML 分离
# 如果您需要在 HTML 文档中显示动态数据，那么每当数据改变时将花费大量的时间来编辑 HTML。
# 通过 XML，数据能够存储在独立的 XML 文件中。这样您就可以专注于使用 HTML/CSS 进行显示和布局，
# 并确保修改底层数据不再需要对 HTML 进行任何的改变。
# 通过使用几行 JavaScript 代码，您就可以读取一个外部 XML 文件，并更新您的网页的数据内容。

# 2.XML 简化数据共享
# 在真实的世界中，计算机系统和数据使用不兼容的格式来存储数据。
# XML 数据以纯文本格式进行存储，因此提供了一种独立于软件和硬件的数据存储方法。
# 这让创建不同应用程序可以共享的数据变得更加容易。

# 3.XML 简化数据传输
# 对开发人员来说，其中一项最费时的挑战一直是在互联网上的不兼容系统之间交换数据。
# 由于可以通过各种不兼容的应用程序来读取数据，以 XML 交换数据降低了这种复杂性。

# XML 树结构
# XML 文档形成了一种树结构，它从"根部"开始，然后扩展到"枝叶"。

# 简单示例
# <?xml version="1.0" encoding="UTF-8"?>
# <note>
# <to>Tove</to>
# <from>Jani</from>
# <heading>Reminder</heading>
# <body>Don't forget me this weekend!</body>
# </note>
import xml.etree.ElementTree as ET  
  
# 解析XML文件  
tree = ET.parse('./00-test.xml')  
root = tree.getroot()  
  
# 遍历所有的<person>元素  
for person in root.findall('person'):  
    name = person.find('name').text  
    age = person.find('age').text  
    email = person.find('email').text  

    # 打印提取的信息  
    print(f"Name: {name}, Age: {age}, Email: {email}")