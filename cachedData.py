import threading

def printit():
  threading.Timer(10.0, printit).start()
  print ("Hello, World!")

printit()