import re

text = "Python - потужна, універсальна; мова!."
pattern = r"[;,-:!.]"
replacement = ""
modified_text = re.sub(pattern, replacement, text)

print(modified_text)  
