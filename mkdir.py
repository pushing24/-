import shutil
import os

# 基础路径配置
base_dir = r'E:\introduction_ai\ai_dogcat\data' # 指向你想生成测试集，训练集，验证集的目录
original_dataset_dir = r'E:\introduction_ai\ai_dogcat\dogs-vs-cats-train1\train' # 指向你原始数据集的文件夹目录


# 递归创建所有目录
def setup_dirs():
    # 创建主目录
    os.makedirs(base_dir, exist_ok=True)

    # 创建子目录
    for dir_type in ['train', 'validation', 'test']:
        dir_path = os.path.join(base_dir, dir_type)
        os.makedirs(dir_path, exist_ok=True)
        # 创建猫狗分类目录
        for animal in ['cats', 'dogs']:
            animal_dir = os.path.join(dir_path, animal)
            os.makedirs(animal_dir, exist_ok=True)


# 执行目录创建
setup_dirs()

# 路径定义（自动生成无需重复定义）
train_cats_dir = os.path.join(base_dir, 'train', 'cats')
validation_cats_dir = os.path.join(base_dir, 'validation', 'cats')
test_cats_dir = os.path.join(base_dir, 'test', 'cats')

train_dogs_dir = os.path.join(base_dir, 'train', 'dogs')
validation_dogs_dir = os.path.join(base_dir, 'validation', 'dogs')
test_dogs_dir = os.path.join(base_dir, 'test', 'dogs')


# 文件复制函数
def copy_files(src_dir, dst_dir, prefix, start, end):
    for i in range(start, end):
        fname = f"{prefix}.{i}.jpg"
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(dst_dir, fname)
        if os.path.exists(src):  # 添加安全性检查
            shutil.copy(src, dst)
        else:
            print(f"Warning: Source file not found - {src}")


# 复制猫图片
copy_files(original_dataset_dir, train_cats_dir, 'cat', 0, 1000)
copy_files(original_dataset_dir, validation_cats_dir, 'cat', 1000, 1500)
copy_files(original_dataset_dir, test_cats_dir, 'cat', 1500, 2000)

# 复制狗图片
copy_files(original_dataset_dir, train_dogs_dir, 'dog', 0, 1000)
copy_files(original_dataset_dir, validation_dogs_dir, 'dog', 1000, 1500)
copy_files(original_dataset_dir, test_dogs_dir, 'dog', 1500, 2000)
