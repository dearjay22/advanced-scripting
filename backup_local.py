import os
import subprocess
import datetime

MYSQL_HOST = "127.0.0.1"
MYSQL_USER = "root"
MYSQL_PASSWORD = "Secret123"
MYSQL_DB = "prog8850"
BACKUP_DIR = "azure_backup_storage"

def main():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    backup_filename = f"mysql-{MYSQL_DB}-{ts}.sql"
    backup_path = os.path.join(BACKUP_DIR, backup_filename)
    
    print(f"Creating backup: {backup_path}")
    
    cmd = [
        "mysqldump",
        f"-h{MYSQL_HOST}",
        f"-u{MYSQL_USER}",
        f"-p{MYSQL_PASSWORD}",
        MYSQL_DB
    ]
    
    result = subprocess.run(
        cmd,
        stdout=open(backup_path, "w"),
        stderr=subprocess.PIPE,
        text=True
    )
    
    if result.returncode != 0:
        print("Backup failed!")
        print("Error:", result.stderr)
        if os.path.exists(backup_path):
            os.remove(backup_path)
    else:
        print("Backup completed successfully.")
        print(f"File saved to: {backup_path}")

if __name__ == "__main__":
    main()
