from src import java_checks
import subprocess
import os
import glob
import shutil
import time
import json

if __name__ == '__main__':
    print("Checking system os type...")
    OS = java_checks.check_system_os()
    print("Checking if java installed...")
    # print(os.environ.items())  # 1. step 1 to check environment variables of system if key has value JAVA
    # TO DO: Check for Ubuntu/linux
    if OS == 'Windows':  # check for windows
        flag, path = java_checks.win_check_environ_java()
        if flag == 1:
            print("Java already configured in the system")
            print("The path is: " + path)
            version = java_checks.win_java_version()  # getting java version for windows system
            print("Java version: " + version)
        else:
            print("Java not found in the system")

    elif OS == 'Darwin':  # check Java installed on Mac OS
        path = java_checks.darwin_check_environ_java()
        if path != 'Java not found':
            print('java exist -version ' + path)
        else:                                         #java not found install java
            print("Java not installed, Installing Java...")


