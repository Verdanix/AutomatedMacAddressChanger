import subprocess

components = subprocess.run('cat /sys/class/net/wlo1/address', shell=True, check=True, capture_output=True).stdout.decode('utf-8').strip().split(":")
print("Mac address:", ':'.join(components))
print("Hex code:", "".join(components))
print()

# Convert the last component to an integer, add one, then convert back to hexadecimal
new_last_component = hex(int(components[-1], 16) + 1)[2:].upper()
# Reconstruct the MAC address with the updated last component
mac = ":".join([components[0]] + [new_last_component] + components[1:-1])
print("New mac address:", mac)
print("Hex code:", "".join(mac.split(":")))

subprocess.run('sudo ip link set dev wlo1 down', shell=True, check=True)
subprocess.run('sudo ip link set dev wlo1 address ' + mac, shell=True, check=True)
subprocess.run('sudo ip link set dev wlo1 up', shell=True, check=True)
