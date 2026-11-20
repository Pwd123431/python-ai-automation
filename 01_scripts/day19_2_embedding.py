import requests
import json
import math

api_url = "https://api.deepseek.com/chat/completions"
api_key = "sk-fde4e297a9064baab0292addeeb9404c"  # 👈 务必换成你自己的

# 1. 这是你的知识库（昨天切出来的小块）
chunks = [
    "生物炭是一种由农业废弃物制备的碳材料。",
    "四环素是一种常见的抗生素，广泛存在于水体中。",
    "利用生物炭降解水体中的四环素效果显著。",
    "机器学习模型在预测材料性质方面有重要作用。"
]

# 2. 定义一个函数，让 AI 把文本变成“带分数的特征向量”
def get_simple_embedding(text):
    # 我们利用大模型的 JSON 强约束，强行提取与几个核心词的相关度得分
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一个向量化工具。必须返回 JSON。"},
            {"role": "user", "content": f"请评估以下文本与[生物炭, 四环素, 降解, 机器学习]这四个词的关联度（0到1之间的小数），返回 JSON 格式，键名为 'biochar', 'tetracycline', 'degradation', 'ml'。文本：{text}"}
        ],
        "response_format": {"type": "json_object"}
    }
    
    res = requests.post(api_url, headers={"Authorization": f"Bearer {api_key}"}, json=payload)
    if res.status_code == 200:
        data = json.loads(res.json()["choices"][0]["message"]["content"])
        # 把返回的字典变成列表 [得分1, 得分2, 得分3, 得分4]
        return [data["biochar"], data["tetracycline"], data["degradation"], data["ml"]]
    else:
        return [0, 0, 0, 0]

# 3. 模拟相似度计算公式（余弦相似度）
def cosine_similarity(v1, v2):
    dot_product = sum(a * b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a * a for a in v1))
    mag2 = math.sqrt(sum(b * b for b in v2))
    if mag1 == 0 or mag2 == 0: return 0
    return dot_product / (mag1 * mag2)

# ================= 开始测试 =================
print("正在将知识库文本变成向量...")
chunk_vectors = []
for c in chunks:
    vec = get_simple_embedding(c)
    chunk_vectors.append(vec)
    print(f"文本: {c[:10]}... | 向量: {vec}")

# 用户提问
query = "怎么利用碳材料去掉水里的抗生素？"
print(f"\n用户提问: {query}")

print("正在将用户问题变成向量...")
query_vec = get_simple_embedding(query)
print(f"问题向量: {query_vec}")

# 计算相似度并排序
results = []
for i in range(len(chunks)):
    score = cosine_similarity(query_vec, chunk_vectors[i])
    results.append((score, chunks[i]))

results.sort(reverse=True)

print("\n=== 语义搜索排名 ===")
for score, text in results:
    print(f"得分: {score:.4f} | {text}")