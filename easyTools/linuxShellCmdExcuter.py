import paramiko


class LinuxRemotObj():


    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
    '''
    持续接收命令执行结果
    '''
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
    '''
    一次性接收命令执行结果
    '''
    def run_remot_shell2(self, cmdlist):
        cmd_str = ''
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.hostname, port=self.port,
                    username=self.username, password=self.password)
        for cmd in cmdlist:
            cmd_str = cmd_str + cmd + ';'
            pass
        stdin, stdout, stderror = ssh.exec_command(cmd_str)
        res = stdout.read()
        err = stderror.read()
        result = res if res else err
        data = result.decode()
        ssh.close()
        return data
        pass


if __name__ == '__main__':
    pass
