import re

text = "Вивчення Python може бути веселим."
pattern = r"в\w*м"  # пошук слова, що починається на "в" та закінчується на "м"
match = re.search(pattern, text, re.IGNORECASE)

if match:
    print("Знайдено:", match.group())
