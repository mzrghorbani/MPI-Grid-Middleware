#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, glob
data_path = '/home/gridpp/mydata'
lfn_dir = '/gridpp/user/m/maziar.ghorbani/mydata'
se = 'UKI-LT2-Brunel-disk'
s = "#!/bin/bash\n"
for my_file in sorted(glob.glob(data_path + "/*")):
    base_name  = os.path.basename(my_file)
    upload_lfn = os.path.join(lfn_dir, base_name)
    s += "dirac-dms-add-file %s %s %s\n" % (upload_lfn, my_file, se)
with open("upload_script.sh", "w") as sf:
    sf.write(s)