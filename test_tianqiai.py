import os

import tianqiai
# tianqiai.api_key = os.getenv("tianqiai_API_KEY")
tianqiai.api_key = ""

result = tianqiai.Completion.create(
  model="glm",
  prompt="问题：冬天，中国哪座城市最适合避寒？问题描述：能推荐一些国内适合冬天避寒的城市吗？回答用户：旅游爱好者 回答：",
  iprompt = "冬天，中国哪座城市最适合避寒？",
  max_tokens=512,
  language="zh-CN",
  temperature=0.9,
)
print(result)