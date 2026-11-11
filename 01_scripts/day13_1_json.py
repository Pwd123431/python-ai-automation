import json

## 这就是一个 JSON 格式的字符串（注意，最外面有单引号，里面是双引号)
json_str='{"name":"pwt","age":25,"skills":["Python","AI"]}'
print('转换前它的字符类型是：',type(json_str))

#json.loads(),转换为字典
python_dict=json.loads(json_str)

print('转换后的字符类型是：',type(python_dict))
print("提取名字:", python_dict["name"])
print("提取第一个技能:", python_dict["skills"][0])

# 我们自己建一个字典
my_data = {"status": "success", "code": 200}

# 用 json.dumps() 把字典变成字符串
json_result = json.dumps(my_data, ensure_ascii=False)

print("\n转换回字符串:", json_result)
print("它的类型又是:", type(json_result))

#写入文件用dump()
with open ('./02_data/test.json','w',encoding='utf-8') as f:
    # indent=4 是为了让文件里排版好看，像树形结构一样
    json.dump(my_data,f,ensure_ascii=False,indent=4)
print('文件已保存：./02_data/test.json')

with open('./02_data/test.json', 'r', encoding='utf-8') as f:
    load_dict = json.load(f)

print('从文件中读取数据：',load_dict)
print('文件类型是：',type(load_dict))

