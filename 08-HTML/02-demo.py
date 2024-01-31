from html.parser import HTMLParser

# 定义一个 HTML 解析器
class MyHTMLParser(HTMLParser):
    def __init__(self, target_tag):
        super().__init__()
        self.target_tag = target_tag  # 目标标签
        self.found_target_tag = False  # 是否找到目标标签
        self.target_data = []  # 目标标签的内容列表

    def handle_starttag(self, tag, attrs):
        if tag == self.target_tag:
            self.found_target_tag = True

    def handle_endtag(self, tag):
        if tag == self.target_tag:
            self.found_target_tag = False

    def handle_data(self, data):
        if self.found_target_tag:
            self.target_data.append(data.strip())

# HTML 示例
html = """
<html>
    <body>
        <h1>这是一个标题</h1>
        <p>这是一个段落。</p>
        <div>
            <p>这是一个 div 中的段落。</p>
            <p>这也是一个 div 中的段落。</p>
        </div>
    </body>
</html>
"""

# 获取用户输入的标签名
target_tag = input("请输入要查找的标签名：")

# 使用自定义的 HTML 解析器解析 HTML
parser = MyHTMLParser(target_tag)
parser.feed(html)

# 输出目标标签的内容
if parser.target_data:
    print("目标标签的内容：")
    for data in parser.target_data:
        print(data)
else:
    print("没有找到标签 %s" % target_tag)
