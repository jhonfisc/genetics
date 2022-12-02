def init():
     global tabuMemory, tabuMemory2
     tabuMemory = []
     tabuMemory2 = []

def setTabuMemory(data):
    global tabuMemory
    tabuMemory = data

def getTabuMemory():
    return tabuMemory

def setTabuMemory2(data):
    global tabuMemory2
    tabuMemory2 = data

def getTabuMemory2():
    return tabuMemory2