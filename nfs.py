import os
import subprocess
import sys

# Define shared directory and allowed clients
shared_dir = "/temp/shared"
allowed_clients = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]  # Replace with actual client IPs from CE hosts

def install_nfs_server():
    """Installs NFS server if it's not already installed."""
    print("Checking for NFS server installation...")
    try:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "nfs-kernel-server"], check=True)
    except subprocess.CalledProcessError:
        print("Error installing NFS server.")
        sys.exit(1)

def configure_shared_directory():
    """Creates shared directory and updates /etc/exports for NFS configuration."""
    print(f"Creating shared directory at {shared_dir}...")
    os.makedirs(shared_dir, exist_ok=True)

    # Prepare export entry with client IP permissions
    client_permissions = " ".join([f"{ip}(rw,no_subtree_check)" for ip in allowed_clients])
    export_entry = f"{shared_dir} {client_permissions}\n"

    # Add export entry to /etc/exports if not already there
    with open("/etc/exports", "r+") as exports_file:
        exports = exports_file.read()
        if export_entry not in exports:
            print("Adding export entry to /etc/exports...")
            exports_file.write(export_entry)

    # Apply export changes
    print("Exporting shared directory...")
    subprocess.run(["sudo", "exportfs", "-ra"], check=True)

def main():
    print("Setting up NFS server...")
    install_nfs_server()
    configure_shared_directory()
    print("NFS server setup complete. Shared directory:", shared_dir)
    print("To use this NFS share, clients must mount the directory using:\n"
          f"  sudo mount <server_ip>:{shared_dir} <local_mount_point>")

if __name__ == "__main__":
    main()
