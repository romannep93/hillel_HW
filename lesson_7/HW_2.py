import os
import pickle


path = input("Введите путь для поиска (для всей системы - введите / для Linux/MacOS или C:/ для Windows): ")
max_files_count = int(input("Введите максимальное количество файлов и папок для обработки: "))
max_file_size = int(input("Введите максимальный размер файла (в байтах), который будет обработан: "))


processed_paths = set()
if os.path.exists('processed_paths.pkl'):
    with open('processed_paths.pkl', 'rb') as f:
        processed_paths = pickle.load(f)


dirs_info = []
files_info = []


unprocessed_paths = [path]


while len(unprocessed_paths) > 0 and len(dirs_info) + len(files_info) < max_files_count:
    path = unprocessed_paths.pop()
    try:

        if os.path.isdir(path) and not os.path.islink(path) and path not in processed_paths:
            unprocessed_paths.extend([os.path.join(path, p) for p in os.listdir(path)])
        elif os.path.isfile(path) and os.path.getsize(path) <= max_file_size and path not in processed_paths:
            files_info.append((path, os.path.getsize(path), len(os.path.basename(path))))
    except OSError:
        continue


processed_paths.update(unprocessed_paths)
processed_paths.update([f[0] for f in files_info])
with open('processed_paths.pkl', 'wb') as f:
    pickle.dump(processed_paths, f)


if files_info:
    min_size_file = min(files_info, key=lambda x: x[1])
    max_size_file = max(files_info, key=lambda x: x[1])
    min_name_file = min(files_info, key=lambda x: x[2])
    max_name_file = max(files_info, key=lambda x: x[2])
    print(f"Минимальный файл: {min_size_file[0]} ({min_size_file[1]} байт)")
    print(f"Максимальный файл: {max_size_file[0]} ({max_size_file[1]} байт)")
    print(f"Файл с самым коротким именем: {min_name_file[0]}")
    print(f"Файл с самым длинным именем: {max_name_file[0]}")


print(f"Количество папок: {len(dirs_info)}")
print(f"Количество файлов: {len(files_info)}")
