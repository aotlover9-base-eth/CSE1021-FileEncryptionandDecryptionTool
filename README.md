# File Encryption & Decryption Tool 🔐

Hey! This is my Python project for encrypting and decrypting files. I made this because I wanted to learn how encryption actually works and how to protect secret files or notes so nobody else can open and read them without a key.

It runs in the terminal and gives you a simple menu where you just press numbers to do stuff.

---

## What does this project do?

Basically, it takes any normal file (like a text file, image, pdf, whatever) and turns it into complete random scrambled nonsense using AES encryption (through Python's `cryptography` / `Fernet` library).

To turn it back into the original file, you need the secret key that was used to lock it. If someone tries to open the locked file with the wrong key or without a key, it won't let them.

Here is what you can do with it:
- Make a new secret key (`.key` file)
- Encrypt a single file
- Decrypt an encrypted file back to normal
- Encrypt multiple files all at once if you have a bunch
- Decrypt multiple files at once
- Auto-organize files into `Downloads/keys`, `Downloads/encrypted`, and `Downloads/decrypted` so you don't lose them!

---

## Things you need before running (Requirements)

- Python 3 installed on your computer (Python 3.7 or newer works great)
- The `cryptography` Python package

To install the cryptography library, just open your terminal in this folder and run:

```bash
pip install -r requirements.txt
```

or you can just do:

```bash
pip install cryptography
```

---

## How to run it

1. Open your terminal or command prompt.
2. Go to the project folder:
   ```bash
   cd CSE1021-FileEncryptionandDecryptionTool
   ```
3. Run the python file:
   ```bash
   python3 main.py
   ```
   *(If you're on Windows and `python3` doesn't work, just type `python main.py`)*

---

## How to use it (Quick Walkthrough)

When you run `python3 main.py`, you will see a menu like this:

```text
==================================================
  FILE ENCRYPTION/DECRYPTION TOOL
==================================================

What do you want to do?

1. Generate a new encryption key
2. Encrypt a file
3. Decrypt a file
4. Encrypt multiple files
5. Decrypt multiple files
6. Exit
```

### Step 1: Generate your key first!
Before you can encrypt anything, you need a key.
1. Type `1` and hit Enter.
2. It asks where you want to save it:
   - **Option 1**: Enter your own custom path and filename.
   - **Option 2**: Just pick option 2! It will automatically save it in your `Downloads/keys` folder (and creates the folder for you if it's not already there).
3. **IMPORTANT**: Do not lose this key! If you lose the key file, you literally cannot get your encrypted file back.

### Step 2: Encrypting a file
1. Type `2` and hit Enter.
2. Enter the path of the file you want to hide/lock (for example: `secret.txt` or `/home/user/Documents/secret.txt`).
3. Enter the path to your key file (if you put it in the same folder or in `Downloads/keys`, just type the path).
4. Now it will ask where to save the locked file:
   - Choose **Option 2** if you want it neatly saved inside `Downloads/encrypted/`.
   - Or choose **Option 1** to save it anywhere else you want.
5. Done! Your file is now encrypted and safe.

### Step 3: Decrypting the file back to normal
1. Type `3` and hit Enter.
2. Enter the path to the encrypted file.
3. Enter the path to the same key you used to encrypt it.
4. Choose where you want the restored file to go:
   - Choose **Option 2** to save it in `Downloads/decrypted/`.
   - Or choose **Option 1** for custom path.
5. Boom! Your original file is restored.

### Doing multiple files (Options 4 & 5)
If you have 3 or 4 files you want to lock at once, pick option 4. It will ask how many files you have, let you type in the paths one by one, and encrypt all of them with your key. Option 5 does the same thing for decrypting.

---

## Where files get saved (The Downloads folder feature)

I added a shortcut so you don't have to keep typing long complicated paths every time:
- **Keys** go to: `~/Downloads/keys/`
- **Encrypted files** go to: `~/Downloads/encrypted/`
- **Decrypted files** go to: `~/Downloads/decrypted/`

If those folders don't exist yet, the program makes them for you automatically.

---

## Project Structure

Here are the files in this folder:

- `main.py` - The main file with the menu and user inputs. You run this one!
- `encryption.py` - Contains all the encryption, decryption, and key handling functions.
- `requirements.txt` - Just lists the cryptography library.
- `example_files/` - Has a sample file you can test with so you don't mess up your real files.
- `screenshots/` - Actual screenshots of the program in action!
- `Statement.md` - The problem statement for my class assignment.
- `README.md` - This file right here!

---

## Errors & Troubleshooting (Stuff that happened to me while testing)

- **"Key file not found"**
  Make sure you actually generated a key first and typed the right filename. If it's in Downloads, type the full path like `~/Downloads/keys/encryption.key`.
- **"Wrong key! Cannot decrypt file"**
  This happens if you generated a new key and tried to use it on a file encrypted with an older key. Keys only unlock files they originally encrypted!
- **"ModuleNotFoundError: No module named 'cryptography'"**
  You forgot to install cryptography. Just run `pip install cryptography` and try again.

---
