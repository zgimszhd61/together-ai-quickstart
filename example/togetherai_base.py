# 导入所需的库
import together
import base64
import io
from PIL import Image
import datetime

# 获取当前日期的函数
def getToday():
    today = datetime.date.today()
    formatted_date = today.strftime("%Y-%m-%d")
    return formatted_date

# 设置Together.ai的API密钥
together.api_key = ''

# 定义模型名称
model_name = 'prompthero/openjourney'

# 生成图像
output = together.Complete.create(
    prompt="a girl",  # 提供的文本提示
    model=model_name,  # 使用的模型名称
    max_tokens=256,  # 生成文本的最大长度
    temperature=0.8,  # 控制生成文本的多样性，值越高越多样化
    top_k=60,  # 从模型预测的词汇概率分布中保留的前k个值
    top_p=0.6,  # 用于剪枝的一个阈值，确保累积概率超过阈值的所有token的总和
    repetition_penalty=1.1,  # 控制模型生成重复token的程度
)

# 从生成的输出中提取图像的Base64编码
base64_image = output['output']['choices'][0]['image_base64']

# 解码Base64编码的图像数据
image_bytes = base64.b64decode(base64_image)

# 使用PIL库打开图像
image = Image.open(io.BytesIO(image_bytes))

# 保存生成的图像，文件名包括当前日期
image.save('output{}.jpg'.format(getToday()))
