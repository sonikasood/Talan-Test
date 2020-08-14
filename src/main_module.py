from src import java_checks
import subprocess
import os
import glob
import shutil
import time
import json

if __name__ == '__main__':
    print("check if java installed")
    # print(os.environ.items())  # 1. step 1 to check environment variables of system if key has value JAVA
    flag, path = java_checks.check_environ_java()
    if flag == 1:
        print("Java already configured in the system")
        print("The path is:" +  path)
    else:
        print("Java not found in the system")