import cv2
import numpy as np
from cryptography.fernet import Fernet
import base64
from hashlib import sha256
from getpass import getpass

def generate_key(password):
    return base64.urlsafe_b64encode(sha256(password.encode()).digest())

def encrypt_msg(msg, key):
    return Fernet(key).encrypt(msg.encode())

def decrypt_msg(encrypted_msg, key):
    try:
        return Fernet(key).decrypt(encrypted_msg).decode()
    except Exception as e:
        print(f"Decryption error: {e}")
        return None

def to_bin(data):
    return ''.join(format(byte, '08b') for byte in data)

def to_bytes(bin_data):
    return bytes(int(bin_data[i:i+8], 2) for i in range(0, len(bin_data), 8))

def int_to_bin(num, length=32):
    return format(num, '0' + str(length) + 'b')

def bin_to_int(bin_data):
    return int(bin_data, 2)

def embed_data(img, bin_data):
    data_len = len(bin_data)
    idx = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):
                if idx < data_len:
                    img[i, j, k] = int(format(img[i, j, k], '08b')[:-1] + bin_data[idx], 2)
                    idx += 1
    return img

def extract_data(img, data_len):
    bin_data = ''
    idx = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):
                if idx < data_len:
                    bin_data += format(img[i, j, k], '08b')[-1]
                    idx += 1
    return bin_data

def hide_data(img, msg, password):
    key = generate_key(password)
    encrypted_msg = encrypt_msg(msg + '#####', key)
    msg_len = len(encrypted_msg)
    
    if (msg_len * 8) + 32 > img.size * 3:
        raise ValueError("Insufficient bytes, need bigger image or less data!")

    length_bin = format(msg_len, '032b')
    img = embed_data(img, length_bin + to_bin(encrypted_msg))
    return img

def reveal_data(img, password):
    length_bin = extract_data(img, 32)
    msg_len = int(length_bin, 2)
    bin_data = extract_data(img, (msg_len * 8) + 32)[32:]
    encrypted_msg = to_bytes(bin_data)
    key = generate_key(password)
    decrypted_msg = decrypt_msg(encrypted_msg, key)
    return decrypted_msg.split('#####')[0] if decrypted_msg else "Failed to decode the message."

def handle_io(action):
    img_name = input("Enter image name (with extension): ")
    img = cv2.imread(img_name)
    if img is None:
        raise FileNotFoundError("Image not found.")
    
    password = getpass("Enter password: ")

    if action == 'encode':
        msg = input("Enter data to be encoded: ")
        new_img = hide_data(img, msg, password)
        file_name = input("Enter the name of the new encoded image (with extension): ")
        cv2.imwrite(file_name, new_img)
        print("Data encoded in image successfully.")
    elif action == 'decode':
        decrypted_msg = reveal_data(img, password)
        print(decrypted_msg if decrypted_msg else "Failed to decode the message.")

def main():
    choice = input("1. Encode the data\n2. Decode the data\n3. Exit\nSelect the option: ")
    if choice == '1':
        handle_io('encode')
    elif choice == '2':
        handle_io('decode')
    elif choice == '3':
        print("Exiting...")

if __name__ == "__main__":
    main()
