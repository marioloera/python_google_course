#!/usr/bin/env python3
import psutil


# checking CPU usage
print('cpu_percent:', psutil.cpu_percent())

# byte read and byte write for disk I/O
print('disk_io_counters:', psutil.disk_io_counters())

# For checking the network I/O bandwidth:
# byte received and byte sent for the network I/O
print('net_io_counters:', psutil.net_io_counters())