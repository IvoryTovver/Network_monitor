import tkinter as tk
from tkinter import ttk
from data_collector import get_system_status, get_network_interfaces, get_network_traffic

def refresh_data(system_status_text, network_interfaces_text, network_traffic_text):
    """Fetches and displays data on the GUI."""
    system_status_text.delete(1.0, tk.END)
    network_interfaces_text.delete(1.0, tk.END)
    network_traffic_text.delete(1.0, tk.END)

    # Get data
    system_status = get_system_status()
    interfaces = get_network_interfaces()
    traffic = get_network_traffic()

    # Display system status
    system_status_text.insert(tk.END, "System Status:\n")
    for key, value in system_status.items():
        system_status_text.insert(tk.END, f"{key}: {value}\n")

    # Display network interfaces
    network_interfaces_text.insert(tk.END, "Network Interfaces:\n")
    for interface, details in interfaces.items():
        network_interfaces_text.insert(tk.END, f"{interface}:\n")
        for detail in details:
            network_interfaces_text.insert(tk.END, f"  {detail}\n")

    # Display network traffic
    network_traffic_text.insert(tk.END, "Network Traffic:\n")
    for key, value in traffic.items():
        network_traffic_text.insert(tk.END, f"{key}: {value} MB\n")

def create_gui():
    """Creates and starts the Tkinter GUI."""
    root = tk.Tk()
    root.title("Network Monitoring Tool")
    root.geometry("800x600")

    # Create tabs using a Notebook widget
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True)

    # Create frames for each tab
    system_status_frame = ttk.Frame(notebook)
    network_interfaces_frame = ttk.Frame(notebook)
    network_traffic_frame = ttk.Frame(notebook)

    # Add frames as tabs
    notebook.add(system_status_frame, text="System Status")
    notebook.add(network_interfaces_frame, text="Network Interfaces")
    notebook.add(network_traffic_frame, text="Network Traffic")

    # Create text widgets for each tab to display data
    system_status_text = tk.Text(system_status_frame, wrap=tk.WORD, height=25, width=80)
    network_interfaces_text = tk.Text(network_interfaces_frame, wrap=tk.WORD, height=25, width=80)
    network_traffic_text = tk.Text(network_traffic_frame, wrap=tk.WORD, height=25, width=80)

    # Place text widgets in the frames
    system_status_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    network_interfaces_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    network_traffic_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Add a refresh button at the bottom
    refresh_button = tk.Button(
        root, text="Refresh Data",
        command=lambda: refresh_data(system_status_text, network_interfaces_text, network_traffic_text)
    )
    refresh_button.pack(pady=10)

    # Populate data on startup
    refresh_data(system_status_text, network_interfaces_text, network_traffic_text)

    # Run the Tkinter main loop
    root.mainloop()