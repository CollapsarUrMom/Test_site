import os
import shutil
import subprocess
import zipfile
import json
import time

class Prefs:
    prefs_file = os.path.join(os.path.dirname(__file__), "preferences.json")
    preferences = {}

    @staticmethod
    def init():
        if os.path.exists(Prefs.prefs_file):
            with open(Prefs.prefs_file, 'r', encoding='utf-8') as file:
                Prefs.preferences = json.load(file)
        else:
            raise FileNotFoundError(f"Файл настроек {Prefs.prefs_file} не найден.")

    @staticmethod
    def get(key):
        return Prefs.preferences.get(key)

def create_directory_if_not_exists(path):
    if not os.path.exists(path):
        print(f"Создание директории: {path}")
        os.makedirs(path)

def extract_dex_files(apk_path, extract_dir):
    dex_files = []
    print(f"Извлечение DEX файлов из APK: {apk_path}")
    with zipfile.ZipFile(apk_path, 'r') as apk:
        for file in apk.namelist():
            if file.startswith("classes") and file.endswith('.dex'):
                dex_path = os.path.join(extract_dir, file)
                apk.extract(file, extract_dir)
                dex_files.append(dex_path)
    return dex_files

def decode_dex(dex_path, output_dir, temp_dir, apktool_jar):
    try:
        temp_apk_path = os.path.join(temp_dir, "temp.apk")
        with zipfile.ZipFile(temp_apk_path, 'w') as temp_apk:
            temp_apk.write(dex_path, os.path.basename(dex_path))
        
        print(f"Запуск декомпиляции DEX: {dex_path}")
        command = f'java -jar "{apktool_jar}" d "{temp_apk_path}" -o "{output_dir}" -f'
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        output = result.stdout + result.stderr
        
        print(f"Результат декомпиляции DEX: {dex_path}")
        print(output)
        
        output_file = os.path.join(output_dir, "apktool_output.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output)
        
        if "Exception" in output or "ERROR" in output:
            return True
        else:
            return False
    except Exception as e:
        print(f"Ошибка при декомпиляции файла {dex_path}: {e}")
        return True

def clear_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            shutil.rmtree(os.path.join(root, dir))

def check_apk_for_dex_errors(apk_path, temp_dir, apktool_jar):
    clear_directory(temp_dir)
                
    dex_files = extract_dex_files(apk_path, temp_dir)
    if dex_files:
        print(f"Найденные DEX файлы в {apk_path}:")
        for dex_file in dex_files:
            print(dex_file)
    else:
        print(f"DEX файлы не найдены в {apk_path}")
        return [], []

    valid_dex_files = []
    problematic_dex_files = []

    for dex_file in dex_files:
        dex_output_dir = os.path.join(temp_dir, os.path.basename(dex_file) + "_out")
        if not os.path.exists(dex_output_dir):
            os.makedirs(dex_output_dir)
        has_error = decode_dex(dex_file, dex_output_dir, temp_dir, apktool_jar)
        if has_error:
            print(f"Ошибка в DEX файле: {dex_file} в APK: {apk_path}")
            problematic_dex_files.append(dex_file)
        else:
            print(f"Проверен DEX файл {dex_file} в APK: {apk_path}, ошибок не обнаружено.")
            valid_dex_files.append(dex_file)
    
    return valid_dex_files, problematic_dex_files

def replace_strings_in_smali_files(temp_dir, replacements):
    modified_files = []
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            if file.endswith(".smali"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                modified = False
                for old, new in replacements.items():
                    if old in content:
                        content = content.replace(old, new)
                        print(f"Найдено и заменено в {file_path}: '{old}' на '{new}'")
                        modified = True
                if modified:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Заменены строки в {file_path}")
                    modified_files.append(file_path)
    return modified_files

def repackage_dex_files(apk_path, dex_files, temp_dir, output_apk_path, modified_dex_files):
    with zipfile.ZipFile(apk_path, 'r') as apk:
        with zipfile.ZipFile(output_apk_path, 'w', compression=zipfile.ZIP_DEFLATED) as new_apk:
            for item in apk.infolist():
                if item.filename.startswith('classes') and item.filename.endswith('.dex'):
                    dex_file_path = os.path.join(temp_dir, item.filename)
                    if dex_file_path in modified_dex_files:
                        print(f"Добавление модифицированного DEX файла в APK: {dex_file_path}")
                        new_apk.write(dex_file_path, item.filename)
                    else:
                        new_apk.writestr(item, apk.read(item.filename))
                else:
                    new_apk.writestr(item, apk.read(item.filename))

def replace_files_in_apk(apk_path, replacements_dir):
    temp_apk_path = f"{apk_path}.temp"
    print(f"Замена файлов в APK {apk_path} из {replacements_dir}")

    with zipfile.ZipFile(apk_path, 'r') as apk:
        with zipfile.ZipFile(temp_apk_path, 'w', zipfile.ZIP_DEFLATED) as temp_apk:
            for item in apk.infolist():
                replacement_path = os.path.join(replacements_dir, item.filename)
                if os.path.exists(replacement_path):
                    print(f"Замена {item.filename} с {replacement_path}")
                    temp_apk.write(replacement_path, item.filename)
                else:
                    temp_apk.writestr(item, apk.read(item.filename))
    
    os.remove(apk_path)
    os.rename(temp_apk_path, apk_path)

def update_crc_and_timestamp(original_apk, modified_apk, output_apk):
    if not os.path.exists(modified_apk):
        raise FileNotFoundError(f"Модифицированный APK файл не найден: {modified_apk}")

    with zipfile.ZipFile(modified_apk, 'r') as zip_in, zipfile.ZipFile(output_apk, 'w') as zip_out:
        with zipfile.ZipFile(original_apk, 'r') as zip_orig:
            for item in zip_in.infolist():
                with zip_in.open(item.filename) as source:
                    data = source.read()

                if item.filename.endswith(('.dex', '.so', 'AndroidManifest.xml')):
                    try:
                        orig_item = zip_orig.getinfo(item.filename)
                        item.CRC = orig_item.CRC
                        date_time = orig_item.date_time
                        date_time = (max(1980, min(date_time[0], 2107)),  # Year between 1980 and 2107
                                     max(1, min(date_time[1], 12)),     # Month between 1 and 12
                                     max(1, min(date_time[2], 31)),     # Day between 1 and 31
                                     max(0, min(date_time[3], 23)),     # Hour between 0 and 23
                                     max(0, min(date_time[4], 59)),     # Minute between 0 and 59
                                     max(0, min(date_time[5], 59)))     # Second between 0 and 59
                        item.date_time = date_time
                    except KeyError:
                        print(f"{item.filename} не найден в {original_apk}")

                zip_out.writestr(item, data)

def align_apk(input_apk, output_apk):
    zipalign_path = os.path.join(os.path.dirname(__file__), "sys", "zipalign")
    print(f"Выровняйте {input_apk} до {output_apk}")
    result = subprocess.run([
        zipalign_path, "-v", "4",
        input_apk,
        output_apk
    ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise Exception("zipalign не удался")

def sign_apk(input_apk, output_apk):
    apksigner_path = os.path.join(os.path.dirname(__file__), "sys", "apksigner.jar")
    key_path = os.path.join(os.path.dirname(__file__), "sys", "testkey.pk8")
    cert_path = os.path.join(os.path.dirname(__file__), "sys", "testkey.x509.pem")
    print(f"Подписываем {input_apk} до {output_apk}")
    result = subprocess.run([
        "java", "-jar", apksigner_path, "sign",
        "--v1-signing-enabled", "true",
        "--v2-signing-enabled", "true",
        "--v3-signing-enabled", "true",
        "--v4-signing-enabled", "false",
        "--key", key_path,
        "--cert", cert_path,
        "--out", output_apk,
        input_apk
    ], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise Exception("apksigner не удался")

def verify_apk(apk_file):
    apksigner_path = os.path.join(os.path.dirname(__file__), "sys", "apksigner.jar")
    print(f"Проверка подписи {apk_file}")
    result = subprocess.run([
        "java", "-jar", apksigner_path, "verify",
        "--verbose",
        apk_file
    ], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise Exception("Проверка не удалась")

def compile_dex(output_dir, apktool_jar):
    temp_apk_path = os.path.join(output_dir, "temp_recompiled.apk")
    command = f'java -jar "{apktool_jar}" b "{output_dir}" -o "{temp_apk_path}"'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    output = result.stdout + result.stderr
    print(f"Результат компиляции DEX: {output_dir}")
    print(output)
    if "Exception" in output or "ERROR" in output:
        raise Exception("Ошибка при компиляции")

def extract_compiled_dex(output_dir, temp_dir):
    temp_apk_path = os.path.join(output_dir, "temp_recompiled.apk")
    with zipfile.ZipFile(temp_apk_path, 'r') as apk:
        for item in apk.infolist():
            if item.filename.startswith('classes') and item.filename.endswith('.dex'):
                dex_file_path = os.path.join(temp_dir, item.filename)
                with apk.open(item.filename) as source, open(dex_file_path, "wb") as target:
                    shutil.copyfileobj(source, target)
                print(f"Извлечен скомпилированный DEX файл: {dex_file_path}")

def show_notification(title, message):
    script = f'''
    Set objShell = CreateObject("WScript.Shell")
    objShell.Popup "{message}", 10, "{title}", 64
    '''
    # Сохранение скрипта во временный файл
    with open("notify.vbs", "w") as f:
        f.write(script)
    # Запуск скрипта
    subprocess.run(["cscript", "//NoLogo", "notify.vbs"])
    # Удаление временного файла
    os.remove("notify.vbs")

def main():
    Prefs.init()

    base_dir = os.path.dirname(__file__)
    input_dir = os.path.join(base_dir, "in")
    output_dir = os.path.join(base_dir, "out")
    temp_dir = os.path.join(base_dir, "temp")
    replacements_dir = os.path.join(base_dir, "replacements")
    apktool_jar = os.path.join(os.path.dirname(__file__), "sys", "apktool.jar")

    create_directory_if_not_exists(input_dir)
    create_directory_if_not_exists(output_dir)
    create_directory_if_not_exists(temp_dir)

    apk_files = [f for f in os.listdir(input_dir) if f.endswith(".apk")]
    if not apk_files:
        print("APK файлы не найдены в директории 'in'.")
        return

    replacements = dict(zip(Prefs.get("replace_old"), Prefs.get("replace_new")))

    for apk_file in apk_files:
        print("###############################################################################################")
        print("###############################################################################################")
        
        start_time = time.time()

        apk_path = os.path.join(input_dir, apk_file)
        temp_output_dir = os.path.join(temp_dir, os.path.splitext(apk_file)[0])

        print(f"Обработка {apk_file}...")
        
        valid_dex_files, problematic_dex_files = check_apk_for_dex_errors(apk_path, temp_dir, apktool_jar)
        
        modified_dex_files = []
        
        for dex_file in valid_dex_files:
            dex_output_dir = os.path.join(temp_dir, os.path.basename(dex_file) + "_out")
            
            # Замена файлов в APK
            replace_files_in_apk(apk_path, replacements_dir)
            
            modified_files = replace_strings_in_smali_files(dex_output_dir, replacements)
            if modified_files:
                compile_dex(dex_output_dir, apktool_jar)
                extract_compiled_dex(dex_output_dir, temp_dir)
                modified_dex_files.append(os.path.join(temp_dir, os.path.basename(dex_file)))

        modified_apk_path = os.path.join(temp_dir, "modified.apk")
        repackage_dex_files(apk_path, valid_dex_files, temp_dir, modified_apk_path, modified_dex_files)

        # Update CRC and timestamps
        updated_apk_path = os.path.join(temp_dir, "updated.apk")
        update_crc_and_timestamp(apk_path, modified_apk_path, updated_apk_path)

        # Align the APK
        aligned_apk_path = os.path.join(temp_dir, "aligned.apk")
        align_apk(updated_apk_path, aligned_apk_path)

        signed_apk_path = os.path.join(output_dir, apk_file)
        sign_apk(aligned_apk_path, signed_apk_path)

        if os.path.exists(temp_output_dir):
            shutil.rmtree(temp_output_dir)
        if os.path.exists(modified_apk_path):
            os.remove(modified_apk_path)

        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        print(f"Время обработки {apk_file}: {int(minutes)} минут {seconds:.2f} секунд")
        
        print("###############################################################################################")
        print("###############################################################################################")
        print(f"Завершена обработка {apk_file}")

    # Clear the temp directory after processing all APK files
    clear_directory(temp_dir)

    # Уведомление о завершении работы скрипта
    show_notification("Script Completed", "Патчер APK завершил работу")

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")


