import os

import zhipuai
# zhipuai.api_key = os.getenv("ZHIPUAI_API_KEY")
zhipuai.api_key = ""

result = zhipuai.Completion.create(
  model="glm",
  prompt="问题：冬天，中国哪座城市最适合避寒？问题描述：能推荐一些国内适合冬天避寒的城市吗？回答用户：旅游爱好者 回答",
  iprompt = "冬天，中国哪座城市最适合避寒？",
  max_tokens=512,
  language="zh-CN",
  temperature=0.9,
)
print(result)