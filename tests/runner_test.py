#!/usr/bin/env python
# -*- coding: utf-8 -*-

from snapabird import runner

import logging
import mock
import unittest


class RunnerTestCase(unittest.TestCase):
    """
    Unit Test case for the main Runner.
    """

    @mock.patch("gpiozero.Button")
    @mock.patch("os.system")
    def test_run(self, mock_system, mock_button):
        """
        Check the runner's main function.
        :param mock_system: The fake system call.
        :param mock_button: The button used by the runner.
        :return:
        """
        logging.debug("Mock is " + str(mock_button))
        test_runner = runner.Runner(mock_button)
        test_runner.run()
        mock_button.wait_for_press.assert_called()
        mock_system.assert_called()
