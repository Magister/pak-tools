#!/usr/bin/env python
# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys
import os
from grit.format.data_pack import DataPack

BINARY, UTF8, UTF16 = range(3)

def main():
    if len(sys.argv) > 1:
        directory = sys.argv[1]
        out_file = directory+".pak"
        files = os.listdir(directory)
        data = {}
        print "Reading files..."
        for file in files:
            id = int(os.path.splitext(file)[0])
            with open(os.path.join(directory, file), "rb") as file:
                contents = file.read()
            data[id] = contents
        print "Writing data..."
        DataPack.WriteDataPack(data, out_file, BINARY)
        print "Finished."

if __name__ == '__main__':
    main()
