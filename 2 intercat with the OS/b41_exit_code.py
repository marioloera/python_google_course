import sys
import os


if len(sys.argv) > 1:
    filename = sys.argv[1]
    print("file name:" + filename)

else:
    print("no file name")
    sys.exit(1)


# in linux to check last exit code
# echo $?

# in windows 
# echo %errorlevel%