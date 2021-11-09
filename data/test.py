import json,random
fp = open('eu_country.json', 'r',encoding='UTF-8')
data = json.load(fp)
l = list(data.items())
random.shuffle(list(data.items()))
data = dict(l)
print(data.popitem())