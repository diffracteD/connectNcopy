import paramiko
import os

def connect_and_copy_files():
    # Greeting
    print("Greetings from Abhisek Mondal!")
    
    # User inputs
    domain = input("Enter the domain address (username@domain:PATH): ")
    username, rest = domain.split("@")
    host, remote_path = rest.split(":")
    
    password = input(f"Enter password for {username}@{host}: ")
    file_extension = input("Enter the file extension to search for (e.g., .txt): ")
    destination_path = os.getcwd()  # Default to current working directory
    
    print(f"Connecting to {host} as {username}...")
    
    try:
        # Create an SSH client and connect
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password)
        print("Connected successfully.")
        
        # Create an SFTP session
        sftp = ssh.open_sftp()
        
        # List files in the remote path
        print(f"Looking for files in {remote_path} with extension {file_extension}...")
        files = sftp.listdir(remote_path)
        matching_files = [f for f in files if f.endswith(file_extension)]
        
        if not matching_files:
            print("No matching files found.")
        else:
            print("🏃 Starting download...")
            for file in matching_files:
                remote_file_path = os.path.join(remote_path, file)
                local_file_path = os.path.join(destination_path, file)
                print(f"Copying {file} to {destination_path}...")
                sftp.get(remote_file_path, local_file_path)
            print("😊 File transfer complete!")
        
        # Close SFTP and SSH connections
        sftp.close()
        ssh.close()
    
    except Exception as e:
        print("😞 An error occurred:", e)

if __name__ == "__main__":
    connect_and_copy_files()
