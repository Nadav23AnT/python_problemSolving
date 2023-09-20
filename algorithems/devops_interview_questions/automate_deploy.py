import paramiko
import os

def deploy_application(package_path, servers):
    # Prompt the user for SSH credentials
    ssh_username = input("Enter SSH username: ")
    ssh_password = input("Enter SSH password: ")

    for server in servers:
        try:
            # Create an SSH client
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Connect to the server using SSH
            print(f"Connecting to {server}...")
            ssh_client.connect(server, username=ssh_username, password=ssh_password)

            # Upload the application package to the server
            print(f"Uploading application package to {server}...")
            sftp = ssh_client.open_sftp()
            sftp.put(package_path, '/tmp/app_package.zip')
            sftp.close()

            # Extract the package and replace existing files
            print(f"Extracting and deploying application on {server}...")
            ssh_client.exec_command('unzip -o /tmp/app_package.zip -d /var/www/app')
            
            # Restart the application server on the remote server
            print(f"Restarting application server on {server}...")
            ssh_client.exec_command('sudo systemctl restart app-service')

            # Close the SSH connection
            ssh_client.close()

            print(f"Deployment to {server} completed successfully.")
        except Exception as e:
            print(f"Deployment to {server} failed: {str(e)}")

# Prompt the user for the path to the application package and target servers
package_path = input("Enter the path to the application package (ZIP file): ")
server_list = input("Enter a list of target server IP addresses or hostnames (comma-separated): ").split(',')

# Call the deploy_application function with the provided inputs
deploy_application(package_path.strip(), server_list)
