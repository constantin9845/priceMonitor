import os
import platform

command = ""

if platform.system() == 'Linux':
    # Command to open a new terminal and start counting
    command = "gnome-terminal -- bash -c 'for i in {1..1000}; do echo $i; sleep 1; clear; done'"
elif platform.system() == 'Windows':
    command = "start cmd /k \"for /L %i in (1,1,1000) do (echo %i & timeout /t & cls 1)\""


# Execute the command
os.system(command)
