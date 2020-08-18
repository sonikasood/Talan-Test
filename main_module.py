from src.java_checks import *
import subprocess
import os
import glob
import shutil
import time
import json

if __name__ == '__main__':
    print("Checking system os type...")
    OS = check_system_os()
    cur_java_version = 8
    print("Checking if java installed...")
    # print(os.environ.items())  # 1. step 1 to check environment variables of system if key has value JAVA
    # TO DO: Check for Ubuntu/linux
    if OS == 'Windows':  # check for windows
        flag, path = win_check_environ_java()
        if flag == 1:
            print("Java already configured in the system")
            print("The path is: " + path)
            version = java_version()  # getting java version for windows system
            print("Java version: " + version)
        else:
            print("Java not found in the system")

    elif OS == 'Darwin':  # check Java installed on Mac OS
        path = darwin_check_environ_java()
        if path != 'Java not found':
            print('java exist -version ' + path)
        else:                                         #java not found install java
            print("Java not installed, Installing Java...")

    elif OS == 'Linux':  # check Java installed on Mac OS
        flag = check_java_linux()
        print("Flag- ", flag)
        if flag == 1:
            print("Java not installed ")
            install_Java()
            print("java installed on This system")
            send_email()
        elif flag == 0:
            print("Java already configured in the system")
            version = java_version()  # getting java version for windows system
            print("Java version: " + version)
            number_version = extract_number(version)
            if number_version < cur_java_version:
                print("More recent Java version available")
                version_input = input("Type your Java version you want to update to (6,7,8): ")
                update_Java(int(version_input))











