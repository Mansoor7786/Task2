import argparse
import unittest
from unittest.suite import TestSuite
from runner import execute
import subprocess

#creating the argument parser
parser = argparse.ArgumentParser()

parser.add_argument("--disk",nargs='+', help = "disk name")
parser.add_argument('--lvname', help="name of the logical volume")
parser.add_argument('--size', help="size of the lv")
parser.add_argument('--vgname', help="volume group name to allocate lv")
parser.add_argument('--fs', help="Filesystem")
args = parser.parse_args()

#getting the values from argument parser

disk_name = args.disk
lvname = args.lvname
size = args.size
vgname = args.vgname
fs = args.fs

if __name__ == '__main__':
    import test_file
    suite = TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromName("test_file.Task2.test_check"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

