import os

# Command to open a new terminal and start counting
command = "gnome-terminal -- bash -c 'for i in {1..1000}; do echo $i; sleep 1; done'"

# Execute the command
os.system(command)
