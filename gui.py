import tkinter as tk
from tkinter import ttk
from data_collector import get_system_info, get_network_interfaces, get_network_traffic


class NetworkMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Network Monitor")
        self.root.geometry("800x600")

        # Main Frame
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # System Info Section
        self.system_info_label = ttk.Label(self.main_frame, text="System Information", font=("Arial", 14, "bold"))
        self.system_info_label.pack(anchor=tk.W, pady=5)

        self.system_info_text = tk.Text(self.main_frame, height=5, wrap=tk.WORD, state=tk.DISABLED, bg="#f0f0f0")
        self.system_info_text.pack(fill=tk.X, pady=5)

        # Network Interfaces Section
        self.interfaces_label = ttk.Label(self.main_frame, text="Network Interfaces", font=("Arial", 14, "bold"))
        self.interfaces_label.pack(anchor=tk.W, pady=5)

        self.interfaces_tree = ttk.Treeview(self.main_frame, columns=("Name", "IPv4", "Status"), show="headings")
        self.interfaces_tree.heading("Name", text="Name")
        self.interfaces_tree.heading("IPv4", text="IPv4 Address")
        self.interfaces_tree.heading("Status", text="Status")
        self.interfaces_tree.pack(fill=tk.BOTH, expand=True, pady=5)

        # Network Traffic Section
        self.traffic_label = ttk.Label(self.main_frame, text="Network Traffic", font=("Arial", 14, "bold"))
        self.traffic_label.pack(anchor=tk.W, pady=5)

        self.traffic_text = tk.Text(self.main_frame, height=5, wrap=tk.WORD, state=tk.DISABLED, bg="#f0f0f0")
        self.traffic_text.pack(fill=tk.X, pady=5)

        # Start updating the UI
        self.update_ui()

    def update_ui(self):
        # Update System Info
        system_info = get_system_info()
        self.system_info_text.config(state=tk.NORMAL)
        self.system_info_text.delete(1.0, tk.END)
        self.system_info_text.insert(tk.END, system_info)
        self.system_info_text.config(state=tk.DISABLED)

        # Update Network Interfaces
        for item in self.interfaces_tree.get_children():
            self.interfaces_tree.delete(item)
        interfaces = get_network_interfaces()
        for interface in interfaces:
            self.interfaces_tree.insert("", tk.END, values=(interface["name"], interface["ipv4"], interface["status"]))

        # Update Network Traffic
        traffic_info = get_network_traffic()
        self.traffic_text.config(state=tk.NORMAL)
        self.traffic_text.delete(1.0, tk.END)
        self.traffic_text.insert(tk.END, traffic_info)
        self.traffic_text.config(state=tk.DISABLED)

        # Schedule the next update
        self.root.after(2000, self.update_ui)  # Update every 2 seconds


if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkMonitorApp(root)
    root.mainloop()