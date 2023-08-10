import os

# { part name: chapter range }
parts = {
        "career": range(2, 19),
        "self_marketing": range(19, 27),
        "lerning": range(27, 36),
        "productivity": range(36, 49),
        "asset_building": range(49, 56),
        "fitness": range(56, 66),
        "mindset": range(66, 75),
    }
# ディレクトリとファイルを作成
def make_dir_and_files():
    for index, (key, value) in enumerate(parts.items()):
        part_dir_path = f'parts/part{index+1}_{key}'
        os.makedirs(part_dir_path, exist_ok=True)
        for i in value:
            chapter_dir_path = f'{part_dir_path}/chapter{i}'
            os.makedirs(chapter_dir_path, exist_ok=True)
            summary_path = os.path.join(chapter_dir_path, "summary.md")
            tasks_path = os.path.join(chapter_dir_path, "tasks.md")
            with open(summary_path, "w") as file:
                file.write(f'# Chapter{i} Summary')
            with open(tasks_path, "w") as file:
                file.write(f'# Chapter{i} Tasks')
        print(f'created directory: {part_dir_path}')

if __name__ == "__main__":
    make_dir_and_files()