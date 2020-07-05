#!/bin/bash

# First parameter is the ID, second parameter is the filename
FILEID=$1
FILENAME=$2

# This script downloads the drive file with the given ID and saves it with t$

COOKIE_FILE=$(mktemp cookiesXXXX.txt)

# First get the confirmation prompt because the file is too big
CONFIRM=$(wget --quiet --save-cookies ${COOKIE_FILE} --keep-session-cookies $

# Then download the file using the confirmation prompt
wget --load-cookies ${COOKIE_FILE} "https://docs.google.com/uc?export=downlo$

# Finally, delete the cookie file
rm ${COOKIE_FILE}
