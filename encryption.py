import os
from cryptography.fernet import Fernet, InvalidToken

def generate_key():
    new_key = Fernet.generate_key()
    return new_key

def get_save_location(file_type="file"):
    file_type_lower = file_type.lower()

    if "key" in file_type_lower:
        folder_name = "keys"
        default_filename = "encryption.key"
    elif "encrypt" in file_type_lower:
        folder_name = "encrypted"
        default_filename = file_type
    elif "decrypt" in file_type_lower:
        folder_name = "decrypted"
        default_filename = file_type
    else:
        folder_name = "files"
        default_filename = file_type

    print("\nWhere would you like to save the " + file_type + "?\n")
    print("1. Save manually (choose custom location)")
    print("2. Save in Downloads/" + folder_name + " folder")

    user_choice = input("\nEnter your choice (1 or 2): ").strip()

    if user_choice == "1":
        file_name = input("Enter filename for " + file_type + ": ").strip()
        if file_name == "":
            file_name = default_filename

        folder_part = os.path.dirname(file_name)
        if folder_part != "":
            file_name = os.path.basename(file_name)

        folder_path = input("Enter file path: ").strip()
        if folder_path == "":
            if folder_part != "":
                folder_path = folder_part
            else:
                folder_path = "."

        folder_path = os.path.expanduser(folder_path)

        clean_path = folder_path
        if clean_path.endswith("/") or clean_path.endswith("\\"):
            clean_path = clean_path[:-1]

        if os.path.basename(clean_path) == file_name:
            full_save_path = folder_path
        else:
            full_save_path = os.path.join(folder_path, file_name)

        if os.path.isdir(full_save_path) == True:
            print("✗ Error: '" + full_save_path + "' is a directory, not a file.")
            return None

        return full_save_path

    elif user_choice == "2":
        home_dir = os.path.expanduser("~")
        downloads_dir = os.path.join(home_dir, "Downloads")
        destination_folder = os.path.join(downloads_dir, folder_name)

        if os.path.exists(destination_folder) == False:
            os.makedirs(destination_folder)
            print("✓ Created folder: " + destination_folder)

        prompt_text = "Enter filename for " + file_type + " (default: " + default_filename + "): "
        file_name = input(prompt_text).strip()
        if file_name == "":
            file_name = default_filename

        full_save_path = os.path.join(destination_folder, file_name)

        if os.path.isdir(full_save_path) == True:
            print("✗ Error: '" + full_save_path + "' is a directory, not a file.")
            return None

        return full_save_path

    else:
        print("✗ Invalid choice")
        return None

def save_key(key, key_filename):
    if os.path.isdir(key_filename) == True:
        print("✗ Error: '" + str(key_filename) + "' is a directory, not a file.")
        return False

    try:
        dir_name = os.path.dirname(key_filename)
        if dir_name != "":
            if os.path.exists(dir_name) == False:
                os.makedirs(dir_name)

        f = open(key_filename, "wb")
        f.write(key)
        f.close()

        print("✓ Key saved to: " + str(key_filename))
        return True

    except IsADirectoryError:
        print("✗ Error: '" + str(key_filename) + "' is a directory, not a file.")
        return False
    except Exception as err:
        print("✗ Failed to save key: " + str(err))
        return False

def load_key(key_filename):
    if os.path.exists(key_filename) == False:
        print("✗ Key file not found: " + str(key_filename))
        return None

    if os.path.isdir(key_filename) == True:
        print("✗ Error: '" + str(key_filename) + "' is a directory, not a file.")
        return None

    try:
        f = open(key_filename, "rb")
        key_content = f.read()
        f.close()
        return key_content

    except IsADirectoryError:
        print("✗ Error: '" + str(key_filename) + "' is a directory, not a file.")
        return None
    except Exception as err:
        print("✗ Failed to load key: " + str(err))
        return None

def encrypt_file(file_path, key):
    if os.path.exists(file_path) == False:
        print("✗ File not found: " + str(file_path))
        return False

    if os.path.isdir(file_path) == True:
        print("✗ Error: '" + str(file_path) + "' is a directory, not a file.")
        return False

    try:
        cipher = Fernet(key)

        f = open(file_path, "rb")
        raw_data = f.read()
        f.close()

        scrambled_data = cipher.encrypt(raw_data)

        destination_path = get_save_location("encrypted file")
        if destination_path == None:
            return False

        if os.path.isdir(destination_path) == True:
            print("✗ Error: '" + str(destination_path) + "' is a directory, not a file.")
            return False

        dir_part = os.path.dirname(destination_path)
        if dir_part != "":
            if os.path.exists(dir_part) == False:
                os.makedirs(dir_part)

        out_file = open(destination_path, "wb")
        out_file.write(scrambled_data)
        out_file.close()

        file_bytes = os.path.getsize(file_path)
        file_kb = file_bytes / 1024
        rounded_kb = round(file_kb, 2)

        print("\n✓ File encrypted successfully!")
        print("  Original: " + str(file_path))
        print("  Encrypted: " + str(destination_path))
        print("  Size: " + str(rounded_kb) + " KB")
        return True

    except IsADirectoryError:
        print("✗ Error: Cannot encrypt a directory.")
        return False
    except Exception as err:
        print("✗ Encryption failed: " + str(err))
        return False

def decrypt_file(encrypted_file_path, key):
    if os.path.exists(encrypted_file_path) == False:
        print("✗ File not found: " + str(encrypted_file_path))
        return False

    if os.path.isdir(encrypted_file_path) == True:
        print("✗ Error: '" + str(encrypted_file_path) + "' is a directory, not a file.")
        return False

    try:
        cipher = Fernet(key)

        f = open(encrypted_file_path, "rb")
        locked_data = f.read()
        f.close()

        restored_data = cipher.decrypt(locked_data)

        destination_path = get_save_location("decrypted file")
        if destination_path == None:
            return False

        if os.path.isdir(destination_path) == True:
            print("✗ Error: '" + str(destination_path) + "' is a directory, not a file.")
            return False

        dir_part = os.path.dirname(destination_path)
        if dir_part != "":
            if os.path.exists(dir_part) == False:
                os.makedirs(dir_part)

        out_file = open(destination_path, "wb")
        out_file.write(restored_data)
        out_file.close()

        decrypted_bytes = os.path.getsize(destination_path)
        decrypted_kb = decrypted_bytes / 1024
        rounded_kb = round(decrypted_kb, 2)

        print("\n✓ File decrypted successfully!")
        print("  Encrypted: " + str(encrypted_file_path))
        print("  Decrypted: " + str(destination_path))
        print("  Size: " + str(rounded_kb) + " KB")
        return True

    except InvalidToken:
        print("✗ Wrong key! Cannot decrypt file.")
        return False
    except IsADirectoryError:
        print("✗ Error: Cannot decrypt a directory.")
        return False
    except Exception as err:
        print("✗ Decryption failed: " + str(err))
        return False

def encrypt_multiple_files(file_list, key):
    success_count = 0
    failed_count = 0
    total_files = len(file_list)

    print("\nEncrypting " + str(total_files) + " files...\n")

    for f_path in file_list:
        status = encrypt_file(f_path, key)
        if status == True:
            success_count = success_count + 1
        else:
            failed_count = failed_count + 1
        print()

    print("Summary: " + str(success_count) + " encrypted, " + str(failed_count) + " failed")
    return success_count, failed_count

def decrypt_multiple_files(file_list, key):
    success_count = 0
    failed_count = 0
    total_files = len(file_list)

    print("\nDecrypting " + str(total_files) + " files...\n")

    for f_path in file_list:
        status = decrypt_file(f_path, key)
        if status == True:
            success_count = success_count + 1
        else:
            failed_count = failed_count + 1
        print()

    print("Summary: " + str(success_count) + " decrypted, " + str(failed_count) + " failed")
    return success_count, failed_count
