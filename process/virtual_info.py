# coding=utf-8

import subprocess


class VirtualSizeInfo(object):
    def __init__(self, cmd, expected_size=10 * 1024 * 1024):
        """
        Check process
        :param cmd: string, run command
        :param expected_size: default 5G size,expected process virtual size,
            unit is KB
        """
        self.cmd = cmd
        self.expected_size = expected_size
        self.info = self.exec_command()

    def exec_command(self, cmdargs=None):
        """
        :param cmdargs: list|tuple, command list
        """
        delimiter = 'grep'
        command = self.cmd if cmdargs is None else cmdargs

        child = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        child.wait()

        if delimiter not in command:
            filtering = command
        else:
            filtering = command[command.index(delimiter):]
        info = [f.strip() for f in child.stdout.readlines() if filtering not in f]
        return info

    @property
    def pid(self):
        if self.info:
            info_list = self.info[0].split(None, 10)
            return info_list[1]
        raise ValueError('No match Process info: \n\t<{}>'.format('\n\t'.join(self.info)))

    @property
    def virtual_size(self):
        """
        parse virtual memory size
        :return: int, unit is KB
        """
        if self.info:
            info_list = self.info[0].split(None, 10)
            return int(info_list[4])
        raise ValueError('No match Process info: \n\t<{}>'.format('\n\t'.join(self.info)))

    @property
    def is_exceed(self):
        return self.virtual_size <= self.expected_size


