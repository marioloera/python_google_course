import subprocess

"""
executes comands form the os, or command line
the  the exit code and output can be caputre in a 
variable
"""
print("run subprocess:")
# subprocess.run(["cls"]) does not work

subprocess.run(["date"])
# subprocess.run(["ipconifg"]) does not work

# subprocess.run(["sleep","1"]) # does not work
# result = subprocess.run(["ping","localhost"])
# print('return exit code:<{}>'.format(result.returncode))
print("subprocess finish")

# caputing the output
print()
cmd = "date"
print('cmd to execute:'+cmd)
r = subprocess.run([cmd], capture_output=True)
print('return exit code:<{}>'.format(r.returncode))
print('capture_output:\n{}'.format(r.stdout))
print('stderr:\n{}'.format(r.stderr))

#  the stdout begins with b', tells us that this string is 
#  not a proper string for Python. 
#  It's actually an array of bytes
parts = r.stdout.decode()
print('decode:\n{}'.format(parts))

# we can use decode  
