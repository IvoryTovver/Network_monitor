import psutil
import socket

def get_system_status():
    """Collects and returns basic system status information."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    return {
        "CPU Usage (%)": cpu_usage,
        "Memory Usage (%)": memory_info.percent,
        "Disk Usage (%)": disk_usage.percent
    }

def get_network_interfaces():
    """Returns a list of available network interfaces and their details."""
    interfaces = psutil.net_if_addrs()
    interface_details = {}
    for interface, addresses in interfaces.items():
        details = []
        for addr in addresses:
            if addr.family == socket.AF_LINK:  # MAC address
                details.append(f"MAC Address: {addr.address}")
            elif addr.family == socket.AF_INET:  # IPv4 address
                details.append(f"IPv4 Address: {addr.address}")
            elif addr.family == socket.AF_INET6:  # IPv6 address
                details.append(f"IPv6 Address: {addr.address}")
        interface_details[interface] = details
    return interface_details

def get_network_traffic():
    """Returns the total bytes sent and received by all network interfaces."""
    net_io = psutil.net_io_counters()
    return {
        "Bytes Sent (MB)": round(net_io.bytes_sent / (1024 ** 2), 2),
        "Bytes Received (MB)": round(net_io.bytes_recv / (1024 ** 2), 2)
    }