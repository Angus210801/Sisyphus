import os
from ftplib import FTP

# 远程FTP服务器地址
server = '192.168.140.95'

# 本地文件夹路径和远程文件夹名称
local_folder = 'D:/Project_JX_old_rc/JX_SR40DB1/evolve250mono'
remote_folder = 'new_folder'

# 连接到远程FTP服务器
ftp = FTP(server)
ftp.login()

# 切换到新创建的文件夹
ftp.mkd(remote_folder)
ftp.cwd(remote_folder)

# 递归上传文件夹中的文件
def upload_folder(folder_path):
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                ftp.storbinary('STOR ' + file, f)
        elif os.path.isdir(file_path):
            ftp.mkd(file)
            ftp.cwd(file)
            upload_folder(file_path)
            ftp.cwd('..')

# 上传文件夹
upload_folder(local_folder)

# 关闭FTP连接
ftp.quit()
