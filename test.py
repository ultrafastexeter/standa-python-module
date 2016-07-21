import devices.delay_line
import devices.translation_stage
from devices.Standa_8MR151 import Standa_8MR151


try:
    stage = Standa_8MR151(4298)
    stage.powerOn()
    print stage.getAngle()
    raw_input("Wait...")
    stage.setHome()
    print stage.getAngle()
    raw_input("Wait...")
    stage.setAngle(360)
    print stage.getAngle()

    # delay = delay_line.Delay_Line(4298, reverse=True)
    #
    # # delay.setHome()
    # #
    # # print delay.getDelay()
    # # print delay.stage.getPosition()
    # # print delay.stage.controller.getPosition()
    #
    # raw_input("Wait...")
    #
    # delay.reset()
    #
    # print delay.getDelay()
    # print delay.stage.getPosition()
    # print delay.stage.controller.getPosition()
    #
    # raw_input("Wait...")
    #
    # delay.setDelay(10)
    #
    # print delay.getDelay()
    # print delay.stage.getPosition()
    # print delay.stage.controller.getPosition()
except Exception as e:
    print e
finally:
    raw_input("Wait...")
