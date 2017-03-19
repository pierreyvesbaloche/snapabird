#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gpiozero
import logging
import os

PIN_STOP_BUTTON = 2


class Runner(object):
    def __init__(self, button):
        """
        Runner init method.
        @param button: The button in charge of stopping the Runner.
        @type button: int
        """
        self.button = button
        logging.debug("-- Constructor done with button "+str(self.button))

    def run(self):
        """
        Main method of the runner.
        @return:
        """
        logging.info("-- run() started")
        self.button.wait_for_press()
        logging.info("-- run() done")
        os.system("shutdown now -h")

if __name__ == '__main__':
    """
    Main Loop.
    """
    runner = Runner(gpiozero.Button(PIN_STOP_BUTTON))
    runner.run()
