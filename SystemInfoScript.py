import platform, socket

print("\n")
print(">|<"*10, "System Information", ">|<"*10)
uname = platform.uname()
print(f"Operating System: {uname.system} {uname.release}")
print(f"Version: {uname.version}\n")

print(f"Node Name: {uname.node}")
print("IP Address: " +socket.gethostbyname(socket.gethostname()))
print("")

print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

print("\n\n")
