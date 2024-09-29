# Задание 1.  Функцию группового переименования файлов.
# Напишите функцию группового переименования файлов. Она должна:
# 1. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# 2. принимать параметр количество цифр в порядковом номере.
# 3. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# 4. принимать параметр расширение конечного файла.
# 5. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик
# файлов и расширение. 3.Соберите из созданных на уроке и в рамках домашнего
# задания функций пакет для работы с файлами.

import os


def batch_rename_files(directory, final_name, num_digits, old_extension, new_extension, name_range):
    # Проверяем существование каталога
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Каталог '{directory}' не найден.")
    # Получаем список файлов с указанным расширением
    files = [f for f in os.listdir(directory) if
             f.endswith(old_extension)]
    if not files:
        print("Файлы с указанным расширением не найдены.")
        return


# Определяем формат номера с ведущими нулями
    format_string = f"{{:0{num_digits}d}}"
# Перебираем файлы и переименовываем их
    for index, file_name in enumerate(files, start=1):
        base_name: str = os.path.splitext(file_name)[0]
# Извлекаем часть имени файла по заданному диапазону
    if name_range:
        start, end = name_range
        extracted_name = base_name[start - 1:end]
    else:
        extracted_name = base_name
# Формируем новое имя файла
    new_file_name = f"{extracted_name}{final_name}{format_string.format(index)}{new_extension}"
# Полные пути для старого и нового файла
    old_file_path = os.path.join(directory, file_name)
    new_file_path = os.path.join(directory, new_file_name)
# Переименование файла
    os.rename(old_file_path, new_file_path)
    print(f"Переименован '{file_name}' в '{new_file_name}'")


if __name__ == "__main__":

    import sys

    # Проверяем количество аргументов командной строки
    if len(sys.argv) != 6:
        print(f"Usage: python file_rename.py <directory> <final_name> < num_digits > < old_extension > < new_extension > ")
        sys.exit(1)
        directory = sys.argv[1]
        final_name = sys.argv[2]
        num_digits = int(sys.argv[3])
        old_extension = sys.argv[4]
        new_extension = sys.argv[5]
        # Например, диапазон [3, 6]
        name_range = [3, 6]

batch_rename_files(directory, final_name, num_digits, old_extension, new_extension, name_range)

# #
# Задача 2. Создание архива каталога
# Напишите скрипт, который создает архив каталога в формате .zip.
# Скрипт должен принимать путь к исходному каталогу и путь к целевому архиву.
# Архив должен включать все файлы и подпапки исходного каталога.

#
# import os
# import time
# import zipfile
#
#
# def zipdir(path, zip):
#    # ziph is zipfile handle
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             zip.write(os.path.join(root, file),
#                        os.path.relpath(os.path.join(root, file),
#                                        os.path.join(path, '..')))
#
#
# with zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
#     zipdir(f'D:\погружение семинары python\HWSEM7\pythonProject7\dir1.1',zipf)

# Задача 3. Удаление старых файлов
# Напишите скрипт, который удаляет файлы в указанном каталоге, которые не
# изменялись более заданного количества дней.
# Скрипт должен принимать путь к каталогу и количество дней.

#
# import os.path
# import time
#
#
# def delete_old_files(directory, days_old):
#     now = time.time()
#     cutoff = now - (days_old * 86400)
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             file_path = os.path.join(root, file)
#             file_mod_time = os.path.getmtime(file_path)
#             if file_mod_time < cutoff:
#                 os.remove(file_path)  # Удаляем файл
#             print(f"Удален файл: {file_path}")
#
#
# # Пример использования функции
# if __name__ == "__main__":
# delete_old_files('D:\погружение семинары python\HWSEM7\pythonProject7\dir1', 30)
#
# """
# Удален файл: D:\погружение семинары python\HWSEM7\pythonProject7\dir1\.gitignore
# Удален файл: D:\погружение семинары python\HWSEM7\pythonProject7\dir1\ tema.txt
#
# """

# Задача 4. Поиск файлов по расширению
# Напишите функцию, которая находит и перечисляет все файлы с заданным расширением в указанном каталоге и всех его подкаталогах.
# Функция должна принимать путь к каталогу и расширение файла.

import os


# def find_files_by_extension(directory, extension):
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.endswith(extension):
#                 print(os.path.join(root, file))
#
# if __name__ == "__main__":
# find_files_by_extension(f'D:\погружение семинары python\HWSEM7\pythonProject7\dir1.1','.txt')
#
#
# """
# D:\погружение семинары python\HWSEM7\pythonProject7\dir1.1\ abba.txt
# D:\погружение семинары python\HWSEM7\pythonProject7\dir1.1\mem.txt
#
# """