# from tensorflow.keras import models
# from tensorflow.keras import layers
# from tensorflow.keras import optimizers
# from tensorflow.keras import losses
# from tensorflow.keras import metrics
#
# model = models.Sequential()
# model.add(layers.Conv2D(32, (3, 3), activation='relu',
#      input_shape=(150, 150, 3)))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(128, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Conv2D(128, (3, 3), activation='relu'))
# model.add(layers.MaxPooling2D((2, 2)))
# model.add(layers.Flatten())
# model.add(layers.Dropout(0.5))
# model.add(layers.Dense(512, activation='relu'))
# model.add(layers.Dense(1, activation='sigmoid'))
# model.compile(loss='binary_crossentropy',
#     optimizer=optimizers.RMSprop(learning_rate=1e-4),
#     metrics=['acc'])
from tensorflow.keras import models, layers
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.optimizers import Adam

# 使用预训练的ResNet50作为基础模型（包含顶部全连接层）
base_model = ResNet50(
    weights='imagenet',
    include_top=False,  # 不包含顶部的全连接层
    input_shape=(150, 150, 3)  # 适配原始输入尺寸
)

# 冻结预训练层的权重（可选，根据是否要微调决定）
for layer in base_model.layers:
    layer.trainable = False  # 冻结所有层

# 构建自定义顶部分类层
model = models.Sequential()
model.add(base_model)  # 添加ResNet主干网络

# 添加自定义分类头
model.add(layers.GlobalAveragePooling2D())  # 替代Flatten
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1, activation='sigmoid'))  # 二分类输出

# 编译模型
model.compile(
    loss='binary_crossentropy',
    optimizer=Adam(learning_rate=1e-4),  # 更适合ResNet的优化器
    metrics=['acc']
)

# 打印模型结构
model.summary()