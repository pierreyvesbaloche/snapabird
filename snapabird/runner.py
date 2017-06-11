#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gpiozero
import logging


class Runner(object):
    """
    Runner class for the SnapABird project.
    """

    # Command : Shutdown
    CMD_SHUTDOWN = "/usr/bin/sudo /sbin/shutdown -h now"

    # PIN : Stop Button
    PIN_STOP_BUTTON = 2

    # Setting up the log configuration
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s %(threadName)s] %(message)s',
                        datefmt='%H:%M:%S')

    def __init__(self, button):
        """
        Runner init method.
        @:param button: The button in charge of stopping the Runner.
        @:type button: int
        @:return None
        """
        self.button = button
        logging.debug("-- Constructor done with button "+str(self.button))

    def shutdown(self, cmd):
        """
        Shutdown method to terminate completly the Pi's activity.
        @:param cmd: The shutdown command to run.
        @:type cmd: str
        @:return The output of the command.
        @:rtype str if defined, None otherwise.
        """
        if cmd:
            logging.info("-- __shutdown() started")
            import subprocess
            process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
            logging.info("-- __shutdown() processing with %s".format(process))
            output = process.communicate()[0]
            logging.info("-- __shutdown() done with %s".format(output))
            return output
        else:
            logging.warning("-- __shutdown() done with no command.")
            return None

    def process(self):
        """
        Main method of the runner.
        @:return None
        """
        logging.info("-- process() started")
        self.button.wait_for_press()
        logging.info("-- process() done")
        self.shutdown(self.CMD_SHUTDOWN)

if __name__ == '__main__':  # pragma: no cover
    """
    Main Loop.
    """
    runner = Runner(gpiozero.Button(Runner.PIN_STOP_BUTTON))
    runner.process()
