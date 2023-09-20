import subprocess

# Define the command to run
command = "ls -l"

# Run the command and capture the output
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check the return code to see if the command succeeded
if result.returncode == 0:
    print("Command output:")
    print(result.stdout)
else:
    print("Command failed with error:")
    print(result.stderr)
