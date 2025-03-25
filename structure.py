import os

def print_tree(start_path='.', prefix=''):
    items = os.listdir(start_path)
    items.sort()  # 排序讓輸出一致
    for index, name in enumerate(items):
        path = os.path.join(start_path, name)
        connector = '└── ' if index == len(items) - 1 else '├── '
        print(prefix + connector + name)
        if os.path.isdir(path):
            extension = '    ' if index == len(items) - 1 else '│   '
            print_tree(path, prefix + extension)

# 執行
print("📁 專案結構：")
print_tree('.')
