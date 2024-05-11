# Create a simple Python monitoring script incorporating the psutil module used to get system metrics
# Import psutil and other module, print error message if unable to import
try:
    import psutil, shutil, datetime, json # type: ignore
    import pyinputplus as pyip # type: ignore
except ImportError as import_error:
    print(f'Error importing module: {import_error}')
    
def get_cpu_info():
    """
    This function gets information on the CPU, such as cores and usage.
    
    Error handling: access denial and general exceptions
    
    Arguments: None
    
    Returns: Dictionary with cpu information.
    
    Return Type: Dict
    """
    try:
        cpu_count = psutil.cpu_count()
        cpu_percent = psutil.cpu_times_percent(percpu=True)
        cpu_information =  {}
        for cpu_index, cpu in enumerate(cpu_percent):
            cpu_information[f'cpu{cpu_index+1}'] = cpu._asdict()
        return cpu_information
    except psutil.AccessDenied:
        print("Error: Access denied to CPU information.")
        return {}  
    except Exception as error:  
        print(f"Error: Unexpected error occurred - {error}")
        return {}

def get_memory_info():
    """
    This function gets information on memory, such as swap memory and the virtual usage.

    Error handling: access denial and general exceptions
    
    Arguments: None

    Returns: Dictionary with memory information.
    
    Return Type: Dict
    """
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
        print(f"Error: Access denied to memory information.")  
        return {}  
    except Exception as error:
        print(f"Error: Unexpected error occurred in get_memory_info - {error}") 
        return {}

def get_disk_info():
    """
    This function gets information on the disks, such as each partition and their usage.
    
    Error handling: access denial and general exceptions
    
    Arguments: None

    Returns: Dictionary with disk type and usage information.
    
    Return Type: Dict
    """
    try:
        disk_partitions = psutil.disk_partitions()
        disk_info ={}
        for partition in disk_partitions:
            usage = shutil.disk_usage(partition.mountpoint)
            # Create a dictionary for this partition (use mountpoint as key)
            disk_info[partition.mountpoint] = {
                "device": partition.device,
                "fstype": partition.fstype,
                "opts": partition.opts,  # Include options if needed
                "total": usage.total,
                "used": usage.used,
                "free": usage.free,
                "percent": usage.percent
            }
            
        return disk_info  # Return the main dictionary
    except psutil.AccessDenied:
        print(f"Error: Access denied to disk information.")  # Change xxx to the relevant resource
        return {}  
    except Exception as error:
        print(f"Error: Unexpected error occurred in get_disk_info - {error}") 
        return {}
    
def get_network_info():
    """
    This function gets information on network metrics, the bytes and packets.
    
    Error handling: access denial and general exceptions
    
    Arguments: None

    Returns: Dictionary with network information on data sent and received.
    
    Return Type: Dict
    """
    try:
        network_usage = psutil.net_io_counters()
        return {
            "Bytes Sent":network_usage.bytes_sent,
            "Bytes Received":network_usage.bytes_recv,
            "Packets Sent": network_usage.packets_sent,
            "Packets Received": network_usage.packets_recv
        }
    except psutil.AccessDenied:
        print(f"Error: Access denied to network information.")  
        return {}  
    except Exception as error:
        print(f"Error: Unexpected error occurred in get_network_info - {error}") 
        return {}

def print_json(system_info: dict) -> str:
    """
    This function prints sytem information in JSON format by calling all four functions.
        
    Arguments: system_info (dict): A dictionary containing system information.

    Returns: str: The JSON string representation of the system information.
    """
    try:
        json_string = json.dumps(system_info, indent=4)
        print(json_string)
        return json_string
    except Exception as error:
        print(f"Error: An unexpected error occurred while printing JSON: {error}")
        return None
def print_table(system_info):
    """Prints system information in a tabular format."""

def print_monitor(as_table=False):
    """
    Retrieves and prints the system information.

    Args:
        as_table (bool, optional): If True, prints the output as a table. Defaults to False (JSON).
    """
    current_time = datetime.datetime.now()
    
    system_info = {
        "timestamp" : current_time.isoformat(),
        "cpu" : get_cpu_info(),
        "memory": get_memory_info(),
        "disk": get_disk_info(),
        "network":get_network_info()
    }
    if as_table:
        pass
    else:
        result = print_json(system_info)
        if result is None:
            print('Error: Unable to generate JSON output.')

from tabulate import tabulate # type: ignore

# ... (your other functions)

def print_table(system_info):
    """
    Prints system information in a tabular format.

    Args:system_info (dict): A dictionary containing system information 
    with keys 'cpu', 'memory', 'swap', 'disk', and 'network'. Each key 
    holds another dictionary with the respective metric data.

    Raises: Exception: If an unexpected error occurs during table formatting or printing.
    """
    try:
        current_time = datetime.datetime.now()
        print(f"\nSystem Monitor - {current_time}")
        # --- CPU Information Table ---
        cpu_headers = ["CPU", "User (%)", "System (%)", "Idle (%)"]
        cpu_table_data = []
        for cpu, info in system_info['cpu'].items():
            cpu_table_data.append([cpu, info['user'], info['system'], info['idle']])
        print("\nCPU Information:")
        print(tabulate(cpu_table_data, headers=cpu_headers))

        # --- Memory Information Table ---
        memory_headers = ["Metric", "Value (MB)"]
        memory_table_data = [
            ["Total", system_info['memory']['total'] / 1024 / 1024],
            ["Available", system_info['memory']['available'] / 1024 / 1024],
            ["Used", (system_info['memory']['total'] - system_info['memory']['available']) / 1024 / 1024],
            ["Percent", system_info['memory']['percent']]
        ]
        print("\nMemory Information:")
        print(tabulate(memory_table_data, headers=memory_headers))

        # --- Swap Memory Information Table ---
        swap_headers = ["Metric", "Value (MB)"]
        swap_table_data = [
            ["Total", system_info['swap']['total'] / 1024 / 1024],
            ["Used", system_info['swap']['used'] / 1024 / 1024],
            ["Free", system_info['swap']['free'] / 1024 / 1024],
            ["Percent", system_info['swap']['percent']]
        ]
        print("\nSwap Information:")
        print(tabulate(swap_table_data, headers=swap_headers))

        # --- Disk Information Table ---
        disk_headers = ["Mount Point", "Filesystem", "Size (GB)", "Used (GB)", "Free (GB)", "Percent (%)"]
        disk_table_data = []
        for mountpoint, info in system_info["disk"].items():
            disk_table_data.append([mountpoint, info["fstype"], 
                                info["total"] / 1024 / 1024 / 1024,
                                info["used"] / 1024 / 1024 / 1024,
                                info["free"] / 1024 / 1024 / 1024,
                                info["percent"]])
        print("\nDisk Information:")
        print(tabulate(disk_table_data, headers=disk_headers))

        # --- Network Information Table ---
        network_headers = ["Metric", "Value"]
        network_table_data = [[k, v] for k, v in system_info['network'].items()]
        print("\nNetwork Information:")
        print(tabulate(network_table_data, headers=network_headers))
    except Exception as error:
        print(f"Error: An unexpected error occurred while printing the table: {error}")