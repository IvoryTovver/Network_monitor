import psutil
import socket


def get_system_info():
    """Returns system information as a formatted string."""
    cpu_percent = psutil.cpu_percent(interval=None)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    return (
        f"CPU Usage: {cpu_percent}%\n"
        f"Memory Usage: {memory.percent}% ({memory.used / (1024**3):.2f} GB / {memory.total / (1024**3):.2f} GB)\n"
        f"Disk Usage: {disk.percent}% ({disk.used / (1024**3):.2f} GB / {disk.total / (1024**3):.2f} GB)"
    )


def get_network_interfaces():
    """Returns a list of network interfaces and their details."""
    interfaces = []
    stats = psutil.net_if_stats()
    addrs = psutil.net_if_addrs()

    for iface_name, iface_addrs in addrs.items():
        ipv4 = next((addr.address for addr in iface_addrs if addr.family == socket.AF_INET), "N/A")
        status = "Up" if stats.get(iface_name, {}).isup else "Down"
        interfaces.append({"name": iface_name, "ipv4": ipv4, "status": status})

    return interfaces


def get_network_traffic():
    """Returns network traffic statistics."""
    net_io = psutil.net_io_counters()
    return (
        f"Bytes Sent: {net_io.bytes_sent / (1024**2):.2f} MB\n"
        f"Bytes Received: {net_io.bytes_recv / (1024**2):.2f} MB"
    )