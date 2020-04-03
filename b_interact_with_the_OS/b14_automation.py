import shutil #disk usage
import psutil #procesor ussage

def check_disk_usage(disk):
    """Check the usage of a given disk, return True if at least 20 is free """
    du = shutil.disk_usage(disk)
    free = du.free/du.total
    return free >= .2

print(help(check_disk_usage))
print(check_disk_usage('/'))

def check_cpu_usage():
    """Check the cpu usage return True if is less 75% """
    usage = psutil.cpu_percent(.1)
    print(usage)
    return usage < 75

print(help(check_cpu_usage))
print(check_cpu_usage())

if not check_disk_usage('/') or not check_cpu_usage():
    print('ERROR!')
else:
    print('Everything is ok')


# adding  execute permission (x) in linux
# sudo chmod +x health_checks.py