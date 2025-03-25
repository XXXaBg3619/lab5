import os

def read_gitignore(path):
    ignore_set = set()
    try:
        with open(os.path.join(path, '.gitignore'), 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_set.add(line.rstrip('/'))
    except FileNotFoundError:
        pass
    return ignore_set

def print_tree(start_path='.', prefix='', ignore=None):
    if ignore is None:
        ignore = set()

    items = [item for item in os.listdir(start_path) if item not in ignore and item != '.git']
    items.sort()

    for index, name in enumerate(items):
        path = os.path.join(start_path, name)
        connector = '└── ' if index == len(items) - 1 else '├── '
        print(prefix + connector + name)
        if os.path.isdir(path):
            extension = '    ' if index == len(items) - 1 else '│   '
            print_tree(path, prefix + extension, ignore)

# 執行
print("📁 專案結構（不包含 .gitignore 中的項目）：")
ignore_set = read_gitignore('.')
print_tree('.', ignore=ignore_set)