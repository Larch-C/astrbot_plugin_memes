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

def to_memes(memes_name, persona_name=None):
    memes_name1 = memes_dict.get(memes_name, None)
    if memes_name1 is None:
        return None
    current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    # 公共目录
    public_directory = os.path.join(current_dir, 'data', 'memes', 'public', memes_name1)
    # 人格目录
    persona_directory = os.path.join(current_dir, 'data', 'memes', persona_name, memes_name1) if persona_name else None

    all_image_files = []
    # 收集公共目录中的图片文件
    if os.path.exists(public_directory):
        public_image_files = [os.path.join(public_directory, f) for f in os.listdir(public_directory) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        all_image_files.extend(public_image_files)
    # 收集人格目录中的图片文件
    if persona_directory and os.path.exists(persona_directory):
        persona_image_files = [os.path.join(persona_directory, f) for f in os.listdir(persona_directory) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        all_image_files.extend(persona_image_files)

    if all_image_files:
        # 随机选择一个图片文件
        return random.choice(all_image_files)
    else:
        return None