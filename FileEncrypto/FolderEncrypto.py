import os
from cryptography.fernet import Fernet

class FileEncrypto:
    def __init__(self):
        self.keys = []  

    def encrypt_directory(self, directory_path):
        if not os.path.isdir(directory_path):
            print(f"{directory_path} nem létezik!")
            return
        
        for file_name in os.listdir(directory_path):
            if file_name.endswith('.py'):  
                file_path = os.path.join(directory_path, file_name)
                
                key = Fernet.generate_key()
                cipher = Fernet(key)
                
                with open(file_path, 'rb') as file:
                    file_data = file.read()
                encrypted_data = cipher.encrypt(file_data)
                
                with open(file_path + '', 'wb') as encrypted_file:
                    encrypted_file.write(encrypted_data)

                self.keys.append((file_name, key.decode()))  

        with open(os.path.join(directory_path, 'file.key'), 'w') as key_file:
            for file_name, key in self.keys:
                key_file.write(f"{file_name} {key}\n")



class FileDecryptor:
    def __init__(self, keys):
        self.ciphers = {}
        for file_name, key in keys:
            self.ciphers[file_name] = Fernet(key)

    def decrypt_directory(self, directory_path):
        
        for file_name, cipher in self.ciphers.items():
            encrypted_file_path = os.path.join(directory_path, file_name + '')
            try:
                with open(encrypted_file_path, 'rb') as file:
                    encrypted_data = file.read()
                
                decrypted_data = cipher.decrypt(encrypted_data)
                
                with open(os.path.join(directory_path, file_name), 'wb') as decrypted_file:
                    decrypted_file.write(decrypted_data)

            except Exception as e:
                print(f"Hiba a {file_name} fájl dekódolása során: {e}")

if __name__ == "__main__":
    directory_path = os.path.expanduser('folder') 

    # TITKOSÍTÁS    
    file_encrypto = FileEncrypto()
    file_encrypto.encrypt_directory(directory_path)

    keys = []
    with open(os.path.join(directory_path, 'file.key'), 'r') as key_file:
        for line in key_file:
            file_name, key = line.strip().split(' ', 1)
            keys.append((file_name, key.encode()))

    # DEKÓDOLÁS
    file_decryptor = FileDecryptor(keys)
    file_decryptor.decrypt_directory(directory_path)
