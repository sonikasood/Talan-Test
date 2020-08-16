import os
import platform
import subprocess
import urllib.request

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

# java -version // this will check your jre version
# javac -version // this will check your java compiler version if you installed
def darwin_check_environ_java():  # check for MAC
    print("1. checking if jre present")
    cmd_out = subprocess.run(['java', '-version'], capture_output=True).stderr.decode('utf-8')
    if 'java version' not in cmd_out:  # if java runtime not present
        found_path = 'Java not found'
    else:
        found_path = cmd_out.splitlines()[0].split()[2].strip('""')
    return found_path

def check_java_linux():  # check for Linux
    try:
       print("checking java installed in linux")
       cmd_out = subprocess.check_output(['java', '-version'], shell=True)
       flag = 0
    except subprocess.CalledProcessError as grepexc:
        print("error code", grepexc.returncode)
        flag = 1
        return flag


def java_version():
    cmd_out = subprocess.run(['java', '-version'], capture_output=True).stderr.decode('utf-8')
    java_version = cmd_out.splitlines()[0].split()[2].strip('""')
    return java_version