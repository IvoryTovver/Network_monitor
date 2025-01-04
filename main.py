import psutil
import time
import socket  # Import socket for AF_INET and AF_INET6 constants

def get_system_status():
    """Collects and returns basic system status information."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    system_status = {
        "CPU Usage (%)": cpu_usage,
        "Memory Usage (%)": memory_info.percent,
        "Disk Usage (%)": disk_usage.percent
    }
    return system_status

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
    traffic_data = {
        "Bytes Sent (MB)": round(net_io.bytes_sent / (1024 ** 2), 2),
        "Bytes Received (MB)": round(net_io.bytes_recv / (1024 ** 2), 2)
    }
    return traffic_data

if __name__ == "__main__":
    while True:
        # System status
        system_status = get_system_status()
        print("\nSystem Status:")
        for key, value in system_status.items():
            print(f"{key}: {value}")

        # Network interfaces
        interfaces = get_network_interfaces()
        print("\nNetwork Interfaces:")
        for interface, details in interfaces.items():
            print(f"{interface}:")
            for detail in details:
                print(f"  {detail}")

        # Network traffic
        traffic = get_network_traffic()
        print("\nNetwork Traffic:")
        for key, value in traffic.items():
            print(f"{key}: {value} MB")

        # Sleep for 5 seconds before the next update
        time.sleep(5)