import json

#剥洋葱挑战

#json字符串
complex_json = """
{
    "data": {
        "user": {"id": 1001, "name": "pwt"},
        "history": [
            {"role": "user", "content": "什么是JSON？"},
            {"role": "ai", "content": "它是一种数据格式。"}
        ]
    }
}
"""

#转换为python字典
python_dict=json.loads(complex_json)

#
data_dict=python_dict["data"]
history_dict=data_dict["history"]
content_dict=history_dict[0]
print(content_dict["content"])