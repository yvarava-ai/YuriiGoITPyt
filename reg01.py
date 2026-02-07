import re

text = "Моя електронна адреса: ex am ple@std.com.net.ua"
pattern = r"\w+@\w+\.\+"
match = re.search(pattern, text)

if match:
    print("Електронна адреса:", match.group())
