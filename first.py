import re
content = """
白日依19989881888山尽，黄河45645546468798978入海流。
欲穷12345千里目，更上15619292345一层楼。
"""

pattern = r"1\d{10}"
results = re.findall(pattern, content)

for result in results:
    print(result)

# r"1\d{10}"可以匹配11位数字，第一个字母是数字1; r意思是raw—string, 方便编写正则表达式
# re.findall方法，可以搜索文本中的所有匹配的模式
