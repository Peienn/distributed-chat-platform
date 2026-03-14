# transformer.py
from transformers import BartForConditionalGeneration, AutoTokenizer, Text2TextGenerationPipeline
import re

# ✅ 只載入一次
MODEL_NAME = "IDEA-CCNL/Randeng-BART-139M-SUMMARY"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = BartForConditionalGeneration.from_pretrained(MODEL_NAME)
summarizer = Text2TextGenerationPipeline(model, tokenizer)

def BART(batch_msgs):
    text = "summary:" + " ".join(batch_msgs)  # ✅ 這個模型需要加 "summary:" 前綴

    result = summarizer(
        text,
        max_length=80,
        do_sample=False
    )

    summary = result[0]["generated_text"]
    summary = summary.replace(" ", "")
    summary = re.sub(r"[\u4e00-\u9fff]+：", "", summary)

    return summary