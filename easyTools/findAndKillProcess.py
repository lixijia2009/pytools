import psutil
import subprocess


def query_pid_list(process_name):
    process_list = psutil.process_iter(['name', 'pid'])
    process_list_find = []
    for item in process_list:
        if p_name in str(item.info['name']):
            print(item.info['pid'], item.info['name'])
            process_list_find.append(item.info['pid'])
    if len(process_list_find) == 0:
        print('process is not exit !')
    return process_list_find


def kill_pid(pid, os='windows'):
    if pid == '':
        print('pid is not exit !')
        return False
    else:
        if os == 'windows':
            subprocess.Popen('taskkill /f /t /im ' + pid, shell=True)
        else:
            subprocess.Popen('kill -9 ' + pid, shell=True)
        return True


def kill_pid_set(p_list):
    is_exit_flag = True
    while is_exit_flag:
        p_id = input('please inpu p_id needing to kill, a to kill all, exit to return : ')
        if p_id == 'exit':
            is_exit_flag = False
        elif p_id == '':
            pass
        elif p_id == 'a':
            for i in p_list:
                kill_pid(str(i))
                is_exit_flag = False
        else:
            kill_pid(p_id)
    pass


if __name__ == '__main__':
    flag = True
    p_list = []
    while flag:
        p_name = input('please inpu p_name or p_name_key needing to query, exit to close this window : ')
        if p_name == 'exit':
            flag = False
        elif p_name == '':
            pass
        else:
            p_list = query_pid_list(p_name)
            if len(p_list) > 0:
                kill_pid_set(p_list)
    subprocess.Popen('pause', shell=True)
