# Create a simple Python monitoring script incorporating the psutil module used to get system metrics
import psutil, os, datetime

# Get the home directory of the machine and the current time for tracking
home_dir = os.path.expanduser('~')
current_time = datetime.datetime.now()

# Get the currect system metrics
cpu_percent = psutil.cpu_times_percent(percpu=True)
memory = psutil.virtual_memory()
swap_memory = psutil.swap_memory()
disk_usage = psutil.disk_usage(home_dir)
network_usage = psutil.net_io_counters()
disk_partitions = psutil.disk_partitions()

''' Create functions 
def get_cpu_info():
    # Use psutil to gather CPU information (usage, frequency, etc.)
    # Return a dictionary or object containing relevant data

def get_memory_info():
    # Use psutil to get virtual memory and swap memory details
    # Return a dictionary or object with memory and swap information

def get_disk_info():
    # Use shutil and psutil to get disk partitions and usage data
    # Return a list of dictionaries or objects, each representing a partition

def get_network_info():
    # Use psutil to get network interface information (bytes sent/received, etc.)
    # Return a dictionary or object with network data
'''

# Printing out metrics
print(f'Metrics as of:{current_time}\n')
print(f'CPU Percentage:{cpu_percent}')
print(f'Memory Usage:{memory}')
print(f'Disk Details:{disk_usage}')
print(f'Network Details:{network_usage}')
print(f'Disk Partiions:{disk_partitions}')
print(f'Swap Memory:{swap_memory}')