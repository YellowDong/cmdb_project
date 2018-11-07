#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import platform



def linux_sys_info():
    from client.plugins.linux import sys_info
    return sys_info.collect()


# def windows_sys_info():
#     from client.plugins.windows import sys_info as win_sys_info
#     return win_sys_info.cellect()


class InfoCollection:
    def collect(self):
        try:
            func = getattr(self, platform.system())
            info_data = func()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError:
            sys.exit('不支持当前操作系统: [%s]!' % platform.system())

    def linux(self):
        return linux_sys_info()

    # def windows(self):
    #     return windows_sys_info()

    def build_report_data(self, data):
        return data