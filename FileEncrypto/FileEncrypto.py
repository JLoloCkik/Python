from cryptography.fernet import Fernet

class FileEncrypto:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, file_path):
     
        with open(file_path, 'rb') as file:
            file_data = file.read()
        
        encrypted_data = self.cipher.encrypt(file_data)
        
        with open(file_path + '.encrypted', 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        with open(file_path + '.key', 'wb') as key_file:
            key_file.write(self.key)


class FileDecryptor:
    def __init__(self, key):

        self.cipher = Fernet(key)

    def decrypt(self, file_path):

        with open(file_path, 'rb') as file:
            encrypted_data = file.read()

        decrypted_data = self.cipher.decrypt(encrypted_data)

     
        with open(file_path.replace('.encrypted', ''), 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)


if __name__ == "__main__":
    file_encrypto = FileEncrypto()
    file_encrypto.encrypt('~/folder/.py')


    with open('keylog.txt.key', 'rb') as key_file:
        key = key_file.read()

    file_decryptor = FileDecryptor(key)
    file_decryptor.decrypt('keylog.txt.encrypted') 