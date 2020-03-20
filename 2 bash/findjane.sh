

#!/bin/bash

oldFiles='oldFiles.txt'

>$oldFiles
#grep " jane " ../data/list.txt | cut -d ' ' -f 3 >$oldFiles
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)
for f in $files;
do
        x="..${f}"
        if test -e $x;
        then
                echo $x>>$oldFiles;
        fi
done
echo "file content:"
cat $oldFiles
