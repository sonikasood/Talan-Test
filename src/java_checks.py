import platform
import subprocess
import smtplib, ssl
import os
import getpass

def check_system_os():
    """
     Function to check Operating system
     :return:
     os_type: String
     """
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

def darwin_check_environ_java():
    """
        Function to check java installation in Mac Os
        :return:
        found_path (str): returns the Java version if found
        """
    print("1. checking if jre present")
    cmd_out = subprocess.run(['java', '-version'], capture_output=True).stderr.decode('utf-8')
    if 'java version' not in cmd_out:  # if java runtime not present
        found_path = 'Java not found'
    else:
        found_path = cmd_out.splitlines()[0].split()[2].strip('""')
    return found_path

def check_java_linux():
    """
        Function to check java installation in Linux environment
        :return:
        flag (int): 0 Java installed, 1 Java not installed

        """
    flag = 1
    print("checking java installed in linux")
    try:
        subprocess.run(['java', '-version'],check = True)
        flag = 0
    except subprocess.CalledProcessError:
        print("inside exception")
        print("Java  not installed in the system")

    finally:
        print("inside finally")
        return flag



def java_version():
    """
        Function to check java version if aleady installed
        :return:
        java_version = Returns java version

        """


    java_version = ""
    print("checking java installed in Windows")
    try:
         cmd_out = subprocess.run(['java', '-version'], capture_output=True).stderr.decode('utf-8')
         java_version = cmd_out.splitlines()[0].split()[2].strip('""')
         print(java_version)

    except subprocess.CalledProcessError as grepex:
          print("Java not installed in this system")

    finally:
        return java_version



def install_Java():
    """
        Function to install java version 8 openJDK

        """
    try:
      print("install_openJDK java")
      package_name = "openjdk-8-jre"
      cmd_out = subprocess.run(['sudo','apt','install', "-y",package_name], check=True)
      print(cmd_out.stdout)
    except subprocess.CallProcessError as grepexc:
        print("error code", grepexc.returncode)
    finally:
        cmd_out.returncode


def win_install_Java():
    """
    Function to install Java online from oracle link to Windows system
    directly silent installation if Java not present

            """
    try:

        cur_user = getpass.getuser()  # downloading Java for current user
        print(cur_user)
        out_path = "C:/Users"+"'/'"+cur_user
        input_path = "C:/Users"+'/'+cur_user+'/Java_install.exe'
        print("downlaoding Java 8 for windows system and installing it")
        cmd_out_dwn = subprocess.run(['Powershell','Invoke-WebRequest https://javadl.oracle.com/webapps/download/AutoDL?xd_co_f=NGEwMGRhYjMtNjg2OS00MTQ2LWJmNTQtMmZiMGE4MWZkYTM5"&"BundleId=242987_a4634525489241b9a9e1aa73d9e118e6', '-OutFile', out_path+'\Java_install.exe'])
        print("Installing Java 8 in Windows...")
        cmd_out_install = subprocess.run(['Powershell', 'Start-Process -Wait -FilePath '+ input_path + ' -ArgumentList "/s" -PassThru'],shell=True,capture_output=True)
        print(cmd_out_install)
        return cmd_out_install.returncode

    except subprocess.CalledProcessError as grepexc:
        print("Helloo exception" + grepexc)


def update_Java(version):
    """
        Function to update java installation to the version of user

        """
    try:
        print("update java")
        if version == 8:
            package_name = "openjdk-8-jre"
        elif version == 7:
            package_name = "openjdk-7-jre"
        elif version == 6:
            package_name = "openjdk-6-jre"
        cmd_out = subprocess.run(['sudo', 'apt', 'install', "-y", package_name], check=True)
        print(cmd_out.stdout)
    except subprocess.CallProcessError as grepexc:
        print("error code", grepexc.returncode)

def extract_number(version):
    """
        Function to extrcat the java version number from string
        :return:
        minor (int): Version number

        """
    major, minor, _ = version.split('.')
    return int(minor)

def send_email(msg):
    """
        Function to send email after installation from google smtp server account

        """
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "javainstallation@gmail.com"  # Enter your address
    receiver_email = "sonikasood94@gmail.com"  # Enter receiver address
    password = input("Type your password and press enter: ")
    message = """\
    Subject: This is the email notification for Java installation 

    Java Status:""" + msg

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)