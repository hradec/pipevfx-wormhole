import streamlit as st
import pandas as pd
import subprocess

# Define boot options
boot_options = {
    "linux": 0,
    "windows": 1,
}

# Function to read the file
def read_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    data = [line.split() for line in lines]
    return data

# Function to write the changes to the file
def write_file(filepath, data):
    with open(filepath, 'w') as f:
        for row in data:
            # Map the second column back to boot options
            row[1] = str(boot_options[row[1]])
            line = ' '.join([ str(x) for x in row ])
            f.write(line + '\n')

# Function to run a shell command and return its output
def run_shell_command(cmd):
    output = ""
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in process.stdout:
        line = line.decode().strip()
        output += line + "\n"
    return output

# Main Streamlit application
def main():

    # Load the data
    data = read_file('grub_boot_defaults')
    df = pd.DataFrame(data, columns=['MAC', 'OS to Boot', 'Menu Timeout', 'Hostname'])
    df['OS to Boot'] = pd.Categorical(df['OS to Boot'].replace({str(v): k for k, v in boot_options.items()}))
    df['Menu Timeout'] = df['Menu Timeout'].astype('int')

    # Edit the DataFrame with increased height and full width
    df = st.experimental_data_editor(df, height=800, use_container_width=True)

    # OK button
    if st.button('OK', key='ok_button', use_container_width=True, type="primary"):
        # Ensure that 'Value_3' is integer before writing to the file
        try:
            df['Menu Timeout'] = df['Menu Timeout'].astype('int')
        except ValueError:
            st.error("Please enter valid integer values for the third column.")
            return

        # Write the changes to the file
        data = df.values.tolist()
        write_file('grub_boot_defaults', data)

        # # Run the shell command
        # shell_cmd_output = run_shell_command('ls -l /')
        #
        # # Display the shell command output
        # st.text_area("Shell Command Output:", value=shell_cmd_output, height=200)
        #
        # st.success("File updated successfully!")
        # st.experimental_rerun()

        _run('scripts/list-root.sh')

if __name__ == "__main__":
    main()
