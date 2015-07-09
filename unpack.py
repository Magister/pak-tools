#!/usr/bin/env python
# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys
import os
import shutil
from grit.format.data_pack import DataPack

BINARY, UTF8, UTF16 = range(3)


def main(*args):
    if len(args) < 2:
        return 1
    fp = args[1]
    directory = os.path.splitext(fp)[0] + os.sep
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)
    print "Reading file..."
    data = DataPack.ReadDataPack(fp)
    print "File encoding: " + str(data.encoding)
    print "Saving data..."
    for (resource_id, text) in data.resources.iteritems():
        ftype = 'bin'
        fheader = text.strip()[0:3]
        if fheader[0:1] == '<':
            ftype = 'html'
        elif fheader[0:1] == '\x89':
            ftype = 'png'
        elif fheader[0:2] == '//':
            ftype = 'js'
        elif fheader[0:1] == '.' or fheader[0:2] == '/*':
            ftype = 'css'
        elif fheader == 'GIF':
            ftype = 'gif'
        elif text.find("function(") > 0:
            ftype = 'js'
        elif text.find("body {") > 0:
            ftype = 'css'
        elif text.find("font-size:") > 0:
            ftype = 'css'
        elif fheader == 'RIF':
            ftype = 'wav'
        output_file = "%s/%s.%s" % (directory, resource_id, ftype)
        with open(output_file, "wb") as fd:
            fd.write(text)
    print "Finished."
    return 0


if __name__ == '__main__':
    main(*sys.argv)
