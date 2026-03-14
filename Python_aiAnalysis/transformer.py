# transformer.py
# ✅ 簡化版，不載入模型，只回傳簡單回應
import re

def BART(batch_msgs):
    """
    模擬回應函數：
    目前只是把訊息合併後返回固定字串。
    
    如果要使用模型：
    1. 將下面程式碼解除註解
    2. pip install transformers torch
    3. 載入你的 BART 模型
    """
    
    # --------------------------
    # 模型可加入位置（目前註解）
    # from transformers import BartForConditionalGeneration, AutoTokenizer, Text2TextGenerationPipeline
    # MODEL_NAME = "IDEA-CCNL/Randeng-BART-139M-SUMMARY"
    # tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    # model = BartForConditionalGeneration.from_pretrained(MODEL_NAME)
    # summarizer = Text2TextGenerationPipeline(model, tokenizer)
    # --------------------------

    # 這裡只回傳簡單的回應
    text = " ".join(batch_msgs)
    # 去除多餘空白
    text = text.replace(" ", "")
    # 可以加些簡單處理，例如去掉中文冒號
    text = re.sub(r"[\u4e00-\u9fff]+：", "", text)
    
    # ✅ 模擬回應
    return f"[簡單回應] {text[:50]}"  # 最多返回50字
