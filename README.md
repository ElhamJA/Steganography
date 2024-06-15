
# Crypto-Steganography-AES

Fernet symmetric encryption is a Python-based application that combines cryptography and steganography to securely hide messages within images. This project uses Least Significant Bit (LSB) steganography to embed encrypted messages into images and Fernet symmetric encryption for message security.

## Features

- **Encryption**: Uses Fernet symmetric encryption to secure the message.
- **Steganography**: Embeds the encrypted message into the image using LSB steganography.
- **Decryption**: Extracts and decrypts the hidden message from the image.

## Requirements

- Python 3.x
- OpenCV
- cryptography library

## Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/Crypto-Steganography-AES.git
```

2. Navigate to the project directory:

```sh
cd Crypto-Steganography-AES
```

3. Create and activate a virtual environment:

```sh
python -m venv cryptoenv
source cryptoenv/bin/activate  # For Windows use `cryptoenv\Scriptsctivate`
```

4. Install the required libraries:

```sh
pip install -r requirements.txt
```

## Usage

Run the main script to start the application:

```sh
python main.py
```

### Encoding a Message

1. Select the `Encode` option.
2. Enter the image file name (e.g., `image.png`).
3. Enter the message to be encoded.
4. Enter the password for encryption.
5. Enter the name of the new encoded image file (e.g., `encoded_image.png`).

### Decoding a Message

1. Select the `Decode` option.
2. Enter the image file name containing the hidden message (e.g., `encoded_image.png`).
3. Enter the password used for encryption.

## How It Works

### Encryption and Decryption

- **Encryption**: The message is encrypted using Fernet encryption, which requires a password to generate a secure key.
- **Decryption**: The encrypted message is decrypted using the same password.

### Steganography

- **LSB Steganography**: The encrypted message is converted to a binary format and embedded into the least significant bits of the image's pixel values.
- **Data Embedding**: The length of the encrypted message is also embedded into the first 32 bits (4 bytes) of the image to facilitate the extraction process.
- **Data Extraction**: The length of the encrypted message is first extracted, followed by the extraction of the actual encrypted message using the retrieved length.

## Project Structure

- `main.py`: Main script that handles the encoding and decoding processes.
- `README.md`: Project documentation.
- `requirements.txt`: Required Python libraries.

## Example

### Encoding

```sh
1. Encode the data
2. Decode the data
3. Exit
Select the option: 1
Enter image name (with extension): image.png
Enter data to be encoded: Hello, this is a secret message!
Enter password: mypassword
Enter the name of the new encoded image (with extension): encoded_image.png
Data encoded in image successfully.
```

### Decoding

```sh
1. Encode the data
2. Decode the data
3. Exit
Select the option: 2
Enter image name (with extension): encoded_image.png
Enter password: mypassword
Hello, this is a secret message!
```


## Acknowledgements

- [OpenCV](https://opencv.org/)
- [cryptography](https://cryptography.io/)
