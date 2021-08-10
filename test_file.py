import unittest
import cli
from runner import execute,fio
import subprocess

class Task2(unittest.TestCase):
    disk = " ".join(cli.disk_name)
    
    def tearDown(self):
        #destroying pv ater running the test
        disk = " ".join(cli.disk_name)
        execute("umount /data")
        execute("rmdir /data")

        execute("lvremove {}".format(cli.vgname),inp="y\n")
        execute("vgremove {}".format(cli.vgname))
        execute("pvremove {}" .format(disk))
                

    def test_check(self):
        execute("pvcreate {}".format(Task2.disk))
        execute("vgcreate {} {}".format(cli.vgname, Task2.disk))
        execute("lvcreate --size {} --name {} {}".format(cli.size,cli.lvname,cli.vgname))
        
        self.lvpath = "/dev/{}/{}" .format(cli.vgname, cli.lvname)
        execute("mkfs -t {} {}" .format(cli.fs,self.lvpath))
        execute("mkdir /data")
        execute("mount {} /data" .format(self.lvpath))

        self.outpv = execute("pvdisplay")
        self.outvg = execute("vgdisplay")
        self.outlv = execute("lvdisplay")
        
        self.fspath = "dev/mapper/{}-{}" .format(cli.vgname, cli.lvname)
        self.outmnt = execute("df -hP /data")

        self.fio_fun = fio("fio --filename={} --minimal --direct=1 --size=1G --rw=randrw --bs=4k --ioengine=libaio --iodepth=256 --runtime=5 --numjobs=32 --time_based --group_reporting --name=iops-test-job --allow_mounted_write=1".format(self.lvpath))


        for i in cli.disk_name:
            self.assertRegex(self.outpv,i, "{} is not present, physical volume not created" .format(i))
        
        self.assertRegex(self.outvg,cli.vgname)
        self.assertRegex(self.outlv,cli.lvname)
        self.assertRegex(self.outmnt, self.fspath)
        #self.assertTrue(self.fio_fun)

