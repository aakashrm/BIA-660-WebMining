import re

text = 'The quick brown fox jumps over the lazy dog.'

Return a match object.
m = re.search('(\w*) dog', text)
print(m)
print(m.group(0))
print(m.group(1))

m2 = re.findall('[Tt]he (\w*) ', text)
print(m2)

m3 = re.finditer('[Tt]he (\w*) ', text)

for _m in m3:
    print(_m.group(1))
