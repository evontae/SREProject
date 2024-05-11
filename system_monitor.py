# Create a simple Python monitoring script incorporating the psutil module used to get system metrics
# Import psutil and other module, print error message if unable to import
try:
    import psutil, shutil, datetime, json # type: ignore
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

def print_json(system_info) -> str:
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


