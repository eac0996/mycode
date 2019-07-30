#!/usr/bin/env python3

import shutil
import os
os.chdir('/home/student/mycode/')
shutil.move('raynor.obj','ceph_storage/')
xname=input('What is the name for kerrigan.obj?')
#the following will rename a file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/'+ xname)
