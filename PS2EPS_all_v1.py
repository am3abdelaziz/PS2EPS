import os
import subprocess

# Get the path of the current script
script_path = os.path.dirname(os.path.abspath(__file__))

# Get a list of all .eps files in the same directory as the script
eps_files = [file for file in os.listdir(script_path) if file.endswith(".eps")]

# Iterate through each .eps file
for eps_file in eps_files:
    # Construct the full path to the file
    file_path = os.path.join(script_path, eps_file)

    # Construct the new file name by appending "_processed"
    output_file = eps_file.replace(".eps", "_processed.eps")
    output_path = os.path.join(script_path, output_file)

    # Construct the command to remove excess white space using ps2eps
    command = f'ps2eps "{file_path}" -f "{output_path}"'

    # Execute the command in a shell environment
    subprocess.Popen(command, shell=True)

    print(f"Processed {eps_file} and saved as {output_file}")

print("All .eps files processed.")
