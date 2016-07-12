import Standa_USBhF

try:
    newStage = Standa_USBhF.ControllerInterface(Standa_USBhF.ListDevices.getDeviceID(4298))
    newStage.powerOn()
    newStage.step(5000)
    print newStage.getPosition()
    newStage.step(-5000)
except Exception as e:
    print e
finally:
    raw_input("Wait...")
