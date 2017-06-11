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
    @mock.patch("subprocess.Popen")
    def test_run(self, mock_sub_process, mock_button):
        """
        Check the runner's main function.
        :param mock_sub_process: The fake system call.
        :param mock_button: The button used by the runner.
        :return:
        """
        logging.debug("Mock is " + str(mock_button))
        test_runner = runner.Runner(mock_button)
        test_runner.process()
        mock_button.wait_for_press.assert_called()
        mock_sub_process.assert_called()

    def test_shutdown_command(self):
        """
        Check the runner's shutdown system command.
        :return:
        """
        self.assertEqual("/usr/bin/sudo /sbin/shutdown -h now", runner.Runner.CMD_SHUTDOWN)

    @mock.patch("gpiozero.Button")
    @mock.patch("subprocess.Popen")
    def test_shutdown_method_ko(self, mock_sub_process, mock_button):
        """
        Check the runner's shutdown system command.
        :param mock_sub_process: The fake system call.
        :param mock_button: The button used by the runner.
        :return:
        """
        test_runner = runner.Runner(mock_button)
        test_runner.shutdown(None)
        mock_sub_process.assert_not_called()

