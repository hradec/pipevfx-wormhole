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
            # line = ' '.join([str(x) for x in row])
            line = "%s  %4s  %-4s  %s" % (row[3], row[1], row[2], row[0] )
            f.write(line + '\n')


# Main Streamlit application
def main():

    # Load the data
    data = read_file('data/grub_boot_defaults')
    df = pd.DataFrame(data, columns=['MAC', 'OS to Boot', 'Menu Timeout', 'Hostname'])

    # Reorder the columns
    df = df[['Hostname', 'OS to Boot', 'Menu Timeout', 'MAC']]

    df['OS to Boot'] = pd.Categorical(df['OS to Boot'].replace({str(v): k for k, v in boot_options.items()}))
    df['Menu Timeout'] = df['Menu Timeout'].astype('int')

    firstScreen = st.empty()
    secondScreen = st.empty()

    with firstScreen.container():

        # Edit the DataFrame with increased height and full width
        df = st.data_editor(df, height=800, use_container_width=True)

        # OK button
        result = st.button('APPLY CHANGES', key='ok_button', use_container_width=True, type="primary")

    if result:
        # "clear screen"
        firstScreen.empty()

        with secondScreen.container():
            st.warning("Please wait wile the server applies the changes. Please avoid booting any machines during this process since the network boot files are being altered and it can cause failed boot!")

        # Ensure that 'Menu Timeout' is integer before writing to the file
        try:
            df['Menu Timeout'] = df['Menu Timeout'].astype('int')
        except ValueError:
            st.error("Please enter valid integer values for the 'Menu Timeout' column.")
            return

        # Write the changes to the file
        data = df.values.tolist()
        write_file('data/grub_boot_defaults', data)

        # Run the shell command
        expander = st.expander("applying changes...", expanded=True)
        # with expander:
        status = _run('data/grub_boot_defaults_apply.sh') #, maxsize=600)

        secondScreen.empty()
        with secondScreen.container():
            if status == 0:
                st.success("The network boot changes have been applied susscessfully!")
                if st.button('DONE', use_container_width=True, type="primary"):
                    st.experimental_rerun()
            else:
                st.error("The network boot changes have failed to apply. \nPlease inform this to your pipeVFX administrator asap as your network boot may be disrupted at this point.")

if __name__ == "__main__":
    main()
