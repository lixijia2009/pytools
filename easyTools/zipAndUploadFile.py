import paramiko
import os
import zipfile
import time


def zip_dir(dirname, zipfilename):
    """ 
    压缩文件
    :dirname: 待压缩目录
    :zipfilename: 压缩后文件名
    """
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))

    zf = zipfile.ZipFile(zipfilename, 'w', zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        # print arcname
        zf.write(tar, arcname)
    zf.close()


def sftp_upload_file(host, user, password, server_path, local_path, timeout=10):
    """
    上传文件，注意：不支持文件夹
    :param host: 主机名
    :param user: 用户名
    :param password: 密码
    :param server_path: 远程路径，比如：/home/sdn/tmp.txt
    :param local_path: 本地路径，比如：D:/text.txt
    :param timeout: 超时时间(默认)，必须是int类型
    :return: bool
    """
    try:
        t = paramiko.Transport((host, 22))
        t.banner_timeout = timeout
        t.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(local_path, server_path)
        t.close()
        return True
    except Exception as e:
        print(e)
        return False


class LinuxRemotObj():
    """ 
    执行linx远程命令
    :cmdlist: 命令列表
    """

    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def run_remot_shell(self, cmdlist):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname, port=self.port,
                    username=self.username, password=self.password)
        shell = ssh.invoke_shell()
        for cmd in cmdlist:
            shell.sendall(cmd + '\n')
            pass
        while True:
            data = shell.recv(2048).decode('utf-8', errors='ignore')
            print(data, end='')
            pass
        ssh.close()


if "__main__" == __name__:
    pass
