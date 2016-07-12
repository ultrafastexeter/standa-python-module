import delay_line
import translation_stage

try:
    delay = delay_line.Delay_Line(4298, reverse=True)

    # delay.setHome()
    #
    # print delay.getDelay()
    # print delay.stage.getPosition()
    # print delay.stage.controller.getPosition()

    raw_input("Wait...")

    delay.reset()

    print delay.getDelay()
    print delay.stage.getPosition()
    print delay.stage.controller.getPosition()

    raw_input("Wait...")

    delay.setDelay(10)

    print delay.getDelay()
    print delay.stage.getPosition()
    print delay.stage.controller.getPosition()
except Exception as e:
    print e
finally:
    raw_input("Wait...")
