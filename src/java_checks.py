import os
import platform
import subprocess


def check_system_os():
    os_type = str(platform.system())
    return os_type


def win_check_environ_java():
    """
    Function to check java installation in Windows OS
    :return:
    flag (int): 0 if no Java, 1 if Java
    found_path (str): returns the Java Path
    """
    flag = 0
    found_path = ""
    for item in os.environ['PATH'].split(';'):

        if (item.__contains__('Java')) or (item.__contains__('JAVA')):  # if environment variable java exist
            if item.__contains__('jdk'):  # regex for jdk
                # print("Java configured in the system" + ": " + item)
                flag = 1
                found_path = item

    return flag, found_path

