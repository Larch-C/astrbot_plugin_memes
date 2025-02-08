import os
import random

memes_dict = {"高兴":"happy",
              "悲伤":"sad",
              "生气":"angry",
              "震惊":"surprise",
              "打招呼":"hello",
              "嘲讽":"taunt",
              "无奈":"helpless",
              "害怕":"fear",
              "厌恶":"dislike",
              "告别":"bye",
              "羞愧":"shame"}

def to_memes(memes_name):
    memes_name1 = memes_dict.get(memes_name, None)
    if memes_name1 is None:
        return None
    # 构建目录路径  
    memes_dir = os.path.join("data", "memes", memes_name1)
    # 检查目录是否存在
    if not os.path.exists(memes_dir):
        return None
    # 获取目录下所有图片文件的路径
    img_urls = [os.path.join(memes_dir, f) for f in os.listdir(memes_dir) if f.endswith((".png", ".jpg", ".bmp", ".gif"))]
    # 检查目录是否为空
    if not img_urls:
        return None
    # 随机选择一个图片文件路径
    return random.choice(img_urls)