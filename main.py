#!/usr/bin/env python3

import os
import sys
from encryption import (
    generate_key, save_key, load_key,
    encrypt_file, decrypt_file,
    encrypt_multiple_files, decrypt_multiple_files,
    get_save_location
)

def print_banner():
    print("\n" + "=" * 50)
    print("  FILE ENCRYPTION/DECRYPTION TOOL")
    print("=" * 50 + "\n")

def print_menu():
    print("\nWhat do you want to do?\n")
    print("1. Generate a new encryption key")
    print("2. Encrypt a file")
    print("3. Decrypt a file")
    print("4. Encrypt multiple files")
    print("5. Decrypt multiple files")
    print("6. Exit")
    print()

def get_user_choice():
    valid_options = ["1", "2", "3", "4", "5", "6"]
    while True:
        choice = input("Enter your choice (1-6): ").strip()
        if choice in valid_options:
            return choice
        else:
            print("✗ Invalid choice. Please enter 1-6.")

def handle_generate_key():
    print("\n--- Generate New Key ---")
    key = generate_key()
    key_str = str(key.decode())
    first_part = key_str[0:20]
    print("New key generated: " + first_part + "...")

    save_location = get_save_location("encryption key")

    if save_location == None:
        print("✗ Key not saved.")
        return

    save_key(key, save_location)

def handle_encrypt_file():
    print("\n--- Encrypt a File ---")

    file_to_encrypt = input("Enter file path to encrypt: ").strip()
    key_file = input("Enter key file path (default: encryption.key): ").strip()
    if key_file == "":
        key_file = "encryption.key"

    key = load_key(key_file)
    if key != None:
        encrypt_file(file_to_encrypt, key)

def handle_decrypt_file():
    print("\n--- Decrypt a File ---")

    file_to_decrypt = input("Enter encrypted file path: ").strip()
    key_file = input("Enter key file path (default: encryption.key): ").strip()
    if key_file == "":
        key_file = "encryption.key"

    key = load_key(key_file)
    if key != None:
        decrypt_file(file_to_decrypt, key)

def handle_encrypt_multiple():
    print("\n--- Encrypt Multiple Files ---")

    num_input = input("How many files to encrypt? ").strip()
    try:
        num_files = int(num_input)
    except ValueError:
        print("✗ Invalid number")
        return

    file_list = []
    for i in range(num_files):
        file_num = i + 1
        file_path = input("Enter file " + str(file_num) + " path: ").strip()
        if file_path != "":
            file_list.append(file_path)

    if len(file_list) == 0:
        print("✗ No files provided")
        return

    key_file = input("Enter key file path (default: encryption.key): ").strip()
    if key_file == "":
        key_file = "encryption.key"

    key = load_key(key_file)
    if key != None:
        encrypt_multiple_files(file_list, key)

def handle_decrypt_multiple():
    print("\n--- Decrypt Multiple Files ---")

    num_input = input("How many files to decrypt? ").strip()
    try:
        num_files = int(num_input)
    except ValueError:
        print("✗ Invalid number")
        return

    file_list = []
    for i in range(num_files):
        file_num = i + 1
        file_path = input("Enter file " + str(file_num) + " path: ").strip()
        if file_path != "":
            file_list.append(file_path)

    if len(file_list) == 0:
        print("✗ No files provided")
        return

    key_file = input("Enter key file path (default: encryption.key): ").strip()
    if key_file == "":
        key_file = "encryption.key"

    key = load_key(key_file)
    if key != None:
        decrypt_multiple_files(file_list, key)

def main():
    print_banner()

    while True:
        print_menu()
        choice = get_user_choice()

        if choice == "1":
            handle_generate_key()
        elif choice == "2":
            handle_encrypt_file()
        elif choice == "3":
            handle_decrypt_file()
        elif choice == "4":
            handle_encrypt_multiple()
        elif choice == "5":
            handle_decrypt_multiple()
        elif choice == "6":
            print("\nGoodbye! Your files are safe.\n")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user.\n")
        sys.exit(0)
