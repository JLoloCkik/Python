import os
import paramiko
from scp import SCPClient

class FileTransferManager:
    def __init__(self, source_dir, file_types):
        self.source_dir = source_dir
        self.file_types = file_types
        
    def list_files(self):
        """Listázza az összes fájlt a könyvtárban és almappákban."""
        all_files = []
        for root, dirs, files in os.walk(self.source_dir):
            for file in files:
                all_files.append(os.path.join(root, file))
        return all_files        
    
    def filter_files_by_type(self, all_files):
        """Szűri a fájlokat a megadott típusok szerint."""
        filtered_files = [file for file in all_files if file.endswith(tuple(self.file_types))]
        return filtered_files
    
class SSHSender:
    def __init__(self, hostname, username, destination_path):
        self.hostname = hostname
        self.username = username
        self.destination_path = destination_path
        self.ssh_client = None

    def connect(self):
        """Kapcsolódás SSH-n keresztül."""
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Itt privát kulccsal vagy jelszóval kell autentikálnod
        self.ssh_client.connect(hostname=self.hostname, username=self.username)

    def send_files(self, files):
        """Fájlok másolása SCP-n keresztül."""
        with SCPClient(self.ssh_client.get_transport()) as scp:
            for file in files:
                print(f"Uploading {file} to {self.destination_path}")
                scp.put(file, self.destination_path)

    def close_connection(self):
        """SSH kapcsolat lezárása."""
        if self.ssh_client:
            self.ssh_client.close()

# Ez a függvény lesz a belépési pont
def main():

    manager = FileTransferManager('/path/to/source', ['.txt', '.jpg'])
    
    all_files = manager.list_files()
    filtered_files = manager.filter_files_by_type(all_files)
    

    if filtered_files:
        print(f"Filtered files to send: {filtered_files}")
        

        sender = SSHSender('github.com', 'git', '/path/to/destination')
        sender.connect()
        sender.send_files(filtered_files)
        sender.close_connection()
    else:
        print("Nincsenek megfelelő fájlok a feltöltéshez.")

# A main függvény futtatása
if __name__ == "__main__":
    main()
