import os
from bestconfig import Config
import shutil


config = Config()

def update_files() -> bool:
    drive_letter = "K:"
    server = config['share_path']
    user = config['user']
    passwd = config['passwd']
    users_1c = config['users']
    file_1c = config['1c_file']
    appdata = config['appdata']


    # Монтируем шару
    os.system(f'net use {drive_letter} {server} /user:{user} {passwd}')

    # Заменяем файлы
    for usr in users_1c:
        #os.makedirs(directory)
        user_1c_dir = appdata.replace("%s", usr["user"])
        user_file = user_1c_dir + "\\" + file_1c
        needed_file = f"{drive_letter}\\{usr["path"]}"
        # print(f"{user_file} - {needed_file}")
        try:
            os.makedirs(user_1c_dir)
            print(f"folder does not exist, creating...{user_1c_dir}")
        except:
            pass
        
        try:
            
            shutil.copy2(needed_file, user_file)
            print(f"{user_file} success!")
        except Exception as e:
            print(f"Cannot replace file {user_file} - {e}")

    # Отключаем шару
    os.system(f'net use {drive_letter} /delete')

if __name__ == "__main__":
    update_files()

