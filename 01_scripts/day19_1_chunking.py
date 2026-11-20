


def split_text(text, chunk_size=200, overlap=50):
    """
    将长文本切分成小块。
    :param text: 要切分的长文本
    :param chunk_size: 每个小块的最大字符数
    :param overlap: 相邻块之间重叠的字符数（防止一句话被硬生生切断）
    """
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        # 算出当前块的结束位置
        end = start + chunk_size
        
        # 截取文本（Python 的切片是左闭右开，所以直接取到 end）
        chunk = text[start:end]
        chunks.append(chunk)
        
        # 核心逻辑：下一次的开始位置 = 当前位置 + 块大小 - 重叠部分
        start = end - overlap
        
    return chunks


# 模拟一段长文本（我们来一首李白的《将进酒》）
long_text = "君不见黄河之水天上来，奔流到海不复回。君不见高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。烹羊宰牛且为乐，会须一饮三百杯。岑夫子，丹丘生，将进酒，杯莫停。与君歌一曲，请君为我倾耳听。"

print(f"原文本总长度: {len(long_text)} 字符\n")

# 调用我们写的切分函数（为了演示，我们把块设得小一点：每块20字，重叠5字）
chunks = split_text(long_text, chunk_size=30, overlap=6)

print(f"共切分成了 {len(chunks)} 个小块：\n")

# 打印每一个切分出来的块，观察“重叠”的效果
for i, chunk in enumerate(chunks):
    print(f"--- 块 {i+1} (长度: {len(chunk)}) ---")
    print(chunk)
    print()