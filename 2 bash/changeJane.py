#!/usr/bin/env python3
import sys
import subprocess

def main():
    oldfile = sys.argv[1]
    with open(oldfile, 'r') as f:
        for line in f:
            #print()
            oldname = line.strip()
            newname = oldname.replace('jane', 'jdoe')
            print(oldname)
            print(newname)
            #subprocess.run(["mv", oldname, newname])
        f.close()

main()
