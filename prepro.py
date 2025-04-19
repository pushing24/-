from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import preprocess_input


train_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=10,           # 减小旋转角度
    # width_shift_range=0.2,
    # height_shift_range=0.2,
    shear_range=0.15,            # 降低剪切强度
    # zoom_range=[0.8, 1.2],       # 允许缩小20%和放大20%
    # horizontal_flip=True,
    # vertical_flip=False,         # 明确禁用垂直翻转
    # fill_mode='reflect',         # 使用镜像填充边缘
    # brightness_range=[0.9,1.1]   # 添加亮度调整
)

test_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)

train_dir = r'E:\introduction_ai\ai_dogcat\data\train'
validation_dir = r'E:\introduction_ai\ai_dogcat\data\validation'
test_dir = r'E:\introduction_ai\ai_dogcat\data\test'



train_generator = train_datagen.flow_from_directory(
    # 目标数据所在位置
    train_dir,
    # 图像转化为 150x150 的数据s
    target_size=(150, 150),
    batch_size=20,
    # 分类模式为 binary，即 0 或 1
    class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
    validation_dir,
    target_size=(150, 150),
    batch_size=20,
    class_mode='binary')