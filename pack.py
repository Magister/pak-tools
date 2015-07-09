#!/usr/bin/env python
# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys
import os
from grit.format.data_pack import DataPack

BINARY, UTF8, UTF16 = range(3)

def main(*args):
    if len(args) < 2:
        return 1

    directory = args[1]
    out_file = directory+".pak"
    files = os.listdir(directory)
    data = {}
    print "Reading files..."
    for fp in files:
        id_str = int(os.path.splitext(fp)[0])
        with open(os.path.join(directory, fp), "rb") as fp:
            contents = fp.read()
        data[id_str] = contents
    print "Writing data..."
    DataPack.WriteDataPack(data, out_file, BINARY)
    print "Finished."
    return 0

if __name__ == '__main__':
    main(*sys.argv)
