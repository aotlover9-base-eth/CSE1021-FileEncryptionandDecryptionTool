# Problem Statement: File Encryption/Decryption Tool

## Problem

In today's digital world, protecting sensitive files from unauthorized access is critical. Whether it's personal documents, financial records, or confidential information, many users struggle with:

1. **Data Security:** How to keep personal files safe from hackers and unauthorized access
2. **File Protection:** Manual methods are unreliable and time-consuming
3. **Key Management:** No easy way to manage encryption keys
4. **Accessibility:** Existing tools are often complex and technical

Users need a **simple, intuitive tool** that lets them:
- Encrypt files without being a cryptography expert
- Decrypt files using the same key
- Manage multiple files at once
- Keep their encryption keys safe

## Solution

This **File Encryption/Decryption Tool** solves the problem by providing:

### Core Features

1. **Key Generation**
   - Automatically generates strong, cryptographically-secure encryption keys
   - No need to manually create keys
   - Keys are saved in simple files

2. **File Encryption**
   - Single-click encryption for any file type
   - Original file remains unchanged
   - Encrypted file created with `.encrypted` extension
   - Shows file size and confirmation

3. **File Decryption**
   - Restore encrypted files using the same key
   - Verifies the correct key is used
   - Creates decrypted copy with `.decrypted` extension
   - Error handling for wrong keys

4. **Batch Processing**
   - Encrypt multiple files at once
   - Decrypt multiple files at once
   - Saves time and reduces errors

5. **User-Friendly Interface**
   - Simple text-based menu
   - Clear prompts and messages
   - Success/error indicators
   - No technical knowledge required

## Technology Used

### AES-128 Encryption (Fernet)
- Industry-standard encryption
- Part of cryptography library
- Produces base64-encoded encrypted files
- Secure and reliable

### Python
- Simple and readable code
- Easy to understand for beginners
- Cross-platform (Windows, Mac, Linux)
- No GUI needed

### File I/O
- Works with any file type
- Binary file handling
- Safe file operations

## Use Cases

1. **Student Projects:** Protect assignment files from plagiarism checkers
2. **Personal Documents:** Encrypt personal records, medical files
3. **Financial Information:** Secure banking documents, tax returns
4. **Sensitive Work:** Protect confidential business documents
5. **Privacy:** Keep private communication logs and journals

## How It Works (High Level)

```
User Input (File Path + Key)
         ↓
   Encryption Module
    (Fernet/AES-128)
         ↓
Encrypted/Decrypted Output
```

## Why This Solution?

✅ **Simple** - Anyone can use it without technical knowledge
✅ **Secure** - Uses industry-standard AES encryption
✅ **Fast** - Quick encryption and decryption
✅ **Reliable** - No data loss or corruption
✅ **Educational** - Clear code to learn from
✅ **Free & Open** - No hidden costs

## Project Objectives

1. Create a working encryption/decryption tool
2. Implement user-friendly command-line interface
3. Support single and batch file operations
4. Provide key management functionality
5. Include proper error handling
6. Document the code clearly
7. Make it accessible to non-technical users

---

**Conclusion:** This tool bridges the gap between security needs and usability, making file encryption accessible to everyone.
