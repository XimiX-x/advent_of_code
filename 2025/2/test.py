import re

#Return a list containing every occurrence of "ai":

txt = "23235"
x = re.search(r"^0|\A(\d+)\1\Z", txt)
print(x)
