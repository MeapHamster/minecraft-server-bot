import settings

# Server Online
def setOnline():
    settings.serverOnline = True

def setOffline():
    settings.serverOnline = False

def getServerStatus():
    return settings.serverOnline

## Command Running
def setRunning():
    settings.commandRunning = True

def setWaiting():
    settings.commandRunning = False

def getRunning():
    return settings.commandRunning