import os
import PyPDF2
import requests
import json
import math
import time

deepseek_api_key = "sk-fde4e297a9064baab0292addeeb9404c" 
pdf_folder = "./02_data/biochar_pdfs/"  

# === 1. 读取并切分（优化：只读第一页，块数锐减） ===
def extract_and_chunk_pdfs(folder, chunk_size=500, overlap=100):
    chunks = []
    for filename in os.listdir(folder):
        if not filename.endswith('.pdf'): continue
        file_path = os.path.join(folder, filename)
        try:
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                full_text = ""
                # 👇 优化：只读第 1 页！
                for i in range(min(1, len(reader.pages))): 
                    full_text += reader.pages[i].extract_text() + "\n"
            
            start = 0
            while start < len(full_text):
                end = start + chunk_size
                chunks.append({"text": full_text[start:end], "source": filename})
                start = end - overlap
        except Exception as e:
            pass
    return chunks

# === 2. 批量向量化（优化：一次发 50 块） ===
def get_batch_vectors(text_list):
    url = "https://api.jina.ai/v1/embeddings"
    headers = {"Content-Type": "application/json"}
    payload = {"model": "jina-embeddings-v2-base-zh", "input": text_list}
    try:
        res = requests.post(url, headers=headers, json=payload, timeout=30)
        if res.status_code == 200:
            # 返回的是一个列表，里面包含每一段文本的向量
            return [item["embedding"] for item in res.json()["data"]]
    except:
        pass
    return [[0.0]*768 for _ in text_list]

def cosine_similarity(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a * a for a in v1))
    mag2 = math.sqrt(sum(b * b for b in v2))
    return dot / (mag1 * mag2) if mag1 and mag2 else 0

# ================= 核心逻辑 =================
print("🚀 解析 PDF...")
chunks = extract_and_chunk_pdfs(pdf_folder)
print(f"✅ 共切分出 {len(chunks)} 个文本块。")

print("🔄 正在批量转换为向量（速度起飞）...")
# 👇 优化：每次取 50 块作为一批
batch_size = 50
for i in range(0, len(chunks), batch_size):
    batch_chunks = chunks[i:i+batch_size]
    batch_texts = [c["text"] for c in batch_chunks]
    
    # 获取这一批的向量
    batch_vectors = get_batch_vectors(batch_texts)
    
    # 把向量塞回给对应的字典
    for j in range(len(batch_chunks)):
        batch_chunks[j]["vector"] = batch_vectors[j]
    
    print(f"  已处理 {min(i+batch_size, len(chunks))}/{len(chunks)} 块...")
    time.sleep(1) # 稍微休息一下，防止被 API 封 IP

print("✅ 向量化完成！知识库已就绪。\n")

while True:
    user_q = input("\n👤 你想问什么？（输入 q 退出）: ")
    if user_q.lower() == 'q': break
    
    print("🕵️ 正在检索...")
    query_vec = get_batch_vectors([user_q])[0]
    
    scores = []
    for chunk in chunks:
        score = cosine_similarity(query_vec, chunk["vector"])
        scores.append((score, chunk["text"], chunk["source"]))
    
    scores.sort(reverse=True, key=lambda x: x[0])
    top_3 = scores[:3]
    
    print("📚 找到相关段落：")
    context = ""
    for score, text, src in top_3:
        print(f"  - [{src}] 匹配度: {score:.3f}")
        context += text + "\n\n"
    
    print("🤖 DeepSeek 正在思考...")
    headers = {"Authorization": f"Bearer {deepseek_api_key}"}
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一个学术助手。请严格根据参考资料回答，不知道就说不知道。"},
            {"role": "user", "content": f"参考：\n{context}\n问题：{user_q}"}
        ]
    }
    res = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=payload)
    if res.status_code == 200:
        print(f"\n✨ AI 回答:\n{res.json()['choices'][0]['message']['content']}")
    else:
        print("AI 报错", res.text)