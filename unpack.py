#!/usr/bin/env python
# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys
import os
import shutil
from grit.format.data_pack import DataPack

BINARY, UTF8, UTF16 = range(3)


def main():
    if len(sys.argv) > 1:
        file = sys.argv[1]
        directory = os.path.splitext(file)[0] + "\\"
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.makedirs(directory)
        print "Reading file..."
        data = DataPack.ReadDataPack(sys.argv[1])
        print "File encoding: " + str(data.encoding)
        print "Saving data..."
        for (resource_id, text) in data.resources.iteritems():
            filetype = 'bin'
            fileheader = text.strip()[0:3]
            if fileheader[0:1] == '<':
                filetype = 'html'
            elif fileheader[0:1] == '\x89':
                filetype = 'png'
            elif fileheader[0:1] == '/':
                filetype = 'js'
            elif fileheader[0:1] == '.':
                filetype = 'css'
            elif fileheader == 'GIF':
                filetype = 'gif'
            elif text.find("function(") > 0:
                filetype = 'js'
            elif text.find("body {") > 0:
                filetype = 'css'
            elif text.find("font-size:") > 0:
                filetype = 'css'
            elif fileheader == 'RIF':
                filetype = 'wav'
            output_file = "%s/%s.%s" % (directory, resource_id, filetype)
            with open(output_file, "wb") as file:
                file.write(text)
        print "Finished."


if __name__ == '__main__':
    main()
