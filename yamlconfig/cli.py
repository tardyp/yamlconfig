#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.yamlconfig import YamlConfig, YamlError
import argparse
import sys

def columnSeparatedPath(s):
    return s.split(":")


def main():
    parser = argparse.ArgumentParser(description='Validate yamlconfigs')
    parser.add_argument('--meta',
                        help='meta file to use to validate the yaml files', default=None)
    parser.add_argument('--path', type=columnSeparatedPath,
                        help='List of directories where to find meta.yaml files', default=[])
    parser.add_argument('yamls', nargs='+',
                        help='files to validate')

    args = parser.parse_args()
    ret = 0
    for fn in args.yamls:
        try:
            YamlConfig(fn, specfn=args.meta, yamltypes_dirs=args.path)
            print fn, "looks good!"
        except YamlError as e:
            print >>sys.stderr, e.message
            ret = 1
    return ret

if __name__ == "__main__":
    sys.exit(main())
