#!/usr/bin/python2
# -*- coding: utf-8 -*-
import subprocess
import argparse
import sys
import json
import re
import os


def get_service_info(service_name):
    """获取服务信息"""
    command = "systemctl status %s.service" % (service_name)
    data = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
    return data


def parse_args(args):
    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument(
        '--help',
        default=False,
        action='store_true',
        help='help.'
    )
    parser.add_argument(
        '--service',
        type=str,
        help='please input service name!'
    )

    (options, argv) = parser.parse_known_args(args)
    if not args or options.help or argv:
        parser.print_help()
        return 0
    return 1, options


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parsed = parse_args(args)
    if 0 == parsed:
        return 1
    api_version, args_parsed = parsed

    service = args_parsed.service
    if service is None:
        print 'please input service name !'
        return 1
    else:
        # 检查相应服务是否正常
        data = get_service_info(service)
        if len(re.findall("Active: active", data)) > 0:
            data = "OK"
        print data


if __name__ == '__main__':
    sys.exit(main())
