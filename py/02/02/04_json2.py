import json

file_path="/home/eprot/py/sample2.json"

data={}
data["posts"]=[]
data["posts"].append({
    "title":"google",
    "url":"https://www.google.com"
})
data["posts"].append({
    "title":"naver",
    "url":"https://www.naver.com"
})
print(data)
with open(file_path, 'w') as outfile:
    json.dump(data, outfile, indent=2, ensure_ascii=False)