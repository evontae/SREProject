# Create a simple Python monitoring script incorporating the psutil module used to get system metrics
# Import psutil and other module, print error message if unable to import
try:
    import psutil, os, datetime # type: ignore
except ImportError as import_error:
    print(f'Error importing module: {import_error}')

#  Create 4 seperate function to retrieve cpu, network, memory & disk metrics. Return a dict for each function and implement error handling to handle access denial and a general exception. We are using a very similar function call for each function 
def get_cpu_info():
    try:
        cpu_count = psutil.cpu_count()
        cpu_percent = psutil.cpu_times_percent(percpu=True)
        cpu_information =  {}
        for range, cpu in enumerate(cpu_percent):
            cpu_information[f'cpu{range+1}'] = cpu._asdict()
            return cpu_information
    except psutil.AccessDenied:
        print("Error: Access denied to CPU information.")
        return {}  # Return empty dictionary
    except Exception as e:  # Catch any unexpected errors
        print(f"Error: Unexpected error occurred - {e}")
    return {}

def get_memory_info():
    try:
        memory = psutil.virtual_memory()
        swap_memory = psutil.swap_memory()
        return {
            "Memory": {
                "total":memory.total,
                "available": memory.available,
                "percent":memory.percent
            },
            "Swap": {
                "total":swap_memory.total,
                "available": swap_memory.available,
                "free":swap_memory.free,
                "percent":swap_memory.percent
            }
            
        }   
    except psutil.AccessDenied:
        print(f"Error: Access denied to memory information.")  # Change xxx to the relevant resource
        return {}  # Or a suitable default value for the function
    except Exception as me:
        print(f"Error: Unexpected error occurred in get_memory_info - {me}") 
        return {}

def get_disk_info():
    try:
        home_dir = os.path.expanduser('~')
        disk_usage = psutil.disk_usage(home_dir)
        disk_partitions = psutil.disk_partitions()
        # Use shutil and psutil to get disk partitions and usage data
        return {
            "Disk Usage" : {
                "total":disk_usage.total,
                "available": disk_usage.available,
                "free":disk_usage.free,
                "percent":disk_usage.percent
            }
        }
    except psutil.AccessDenied:
        print(f"Error: Access denied to disk information.")  # Change xxx to the relevant resource
        return {}  # Or a suitable default value for the function
    except Exception as de:
        print(f"Error: Unexpected error occurred in get_disk_info - {de}") 
        return {}
    
def get_network_info():
    try:
        network_usage = psutil.net_io_counters()
        return {
            "Bytes Sent":network_usage.bytes_sent,
            "Bytes Received":network_usage.bytes_recv,
            "Packets Sent": network_usage.packets_sent,
            "Packets Received": network_usage.packets_recv
        }
    except psutil.AccessDenied:
        print(f"Error: Access denied to network information.")  # Change xxx to the relevant resource
        return {}  # Or a suitable default value for the function
    except Exception as ne:
        print(f"Error: Unexpected error occurred in get_network_info - {ne}") 
        return {}

# Create function to print monitor
# def print_monitor:
    #current_time = datetime.datetime.now()