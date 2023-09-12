import os

# REQUIRES CRACKMAPEXEC TO BE IN PATH
def cme(users, password, target):
    cmd = "crackmapexec"
    cmd += " smb"
    cmd += " " + target
    cmd += " -u " + users
    cmd += " -p \"" + password + "\""
    #optional parameters (these are not all the parameters of crackmapexec but are some sane defaults, you can add or remove what you need below)
    #cmd += " -d DOMAIN" #specify domain
    #cmd += " --local-auth" #enforce local auth
    print("Executing command: " + cmd)
    os.system(cmd)