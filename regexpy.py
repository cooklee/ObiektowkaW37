import re

def check_dive(text):
    r = r'\d*[dD]\d+([+-]\d+)?'
    return bool(re.search(r, text))
#
# text = """17d10
# 2d5+12
# 5d5+8
# 4d3
# 8d7+10
# 8s7+10
# 8D7+10 abcdefghijk
# 8d-h"""
# for line in text.split("\n"):
#     print(line, check_dive(line))
import re


with open('text.txt', 'r', encoding='utf8') as fin:
    text_to_search = fin.read()

r1 = 'autor'
# groups = re.finditer(r1,text_to_search)
# for g in groups:
#     print(g)
#
# r2 = ".{10}\d+%.{10}"
#
# groups = re.finditer(r2,text_to_search)
# for g in groups:
#     print(g)
#
# r3 = "\w+\."
#
# groups = re.finditer(r3,text_to_search)
# for g in groups:
#     print(g)

r4 = "\w*polski\w*"

groups = re.finditer(r4,text_to_search, re.I)
for g in groups:
    print(g)