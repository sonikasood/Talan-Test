from src.java_checks import *

if __name__ == '__main__':
    print("Checking system os type...")
    OS = check_system_os()
    cur_java_version = 8
    print("Checking if java installed...")

    # TO DO: Install Java for Windows and Darwin
    if OS == 'Windows':  # check for windows
        flag, path = win_check_environ_java()
        if flag == 1:
            print("Java already configured in the system")
            print("The path is: " + path)
            msg = "Java already configured in the system" + "The path is: " + path


            version = java_version()  # getting java version for windows system
            if version != "":
              print("Java version: " + version)
              msg = "Java installed with: " + "Java version: " + version
              send_email(msg)
            else:
                print("Java Path configured but no Java found on this system")
                msg = "Setting up Java..."

                if(win_install_Java() == 0):
                    msg = "Java downlaoded and installed succesfully"
                    send_email(msg)
                elif win_install_Java() == 1:
                    msg = "Java could not be installed successfully"
                    send_email(msg)



        else:
            print("Java not found in the system")
            if (win_install_Java() == 0):
                msg = "Java downlaoded and installed succesfully"
                send_email()
            elif win_install_Java() == 1:
                msg = "Java could not be installed successfully"
                send_email(msg)



    elif OS == 'Darwin':  # check Java installed on Mac OS
        path = darwin_check_environ_java()
        if path != 'Java not found':
            print('java exist -version ' + path)
        else:                                         # java not found install java
            print("Java not installed")

    elif OS == 'Linux':  # check Java installed on Ubuntu system
        flag = check_java_linux()
        print("Flag- ", flag)
        if flag == 1:
            print("Java not installed ")
            if(install_Java() == 0):
              print("java installed on This system")
              send_email("Java Installed Sucessfully")
            else:
                send_email("Could not install Java Succesfully exception occurred")
        elif flag == 0:
            print("Java already configured in the system")
            version = java_version()  # getting java version
            print("Java version: " + version)
            number_version = extract_number(version)
            if number_version < cur_java_version:
                print("More recent Java version available")
                version_input = input("Type your Java version you want to update to (6,7,8): ")
                update_Java(int(version_input))
                send_email("Updated Java succesfully")