import streamlit as st
import pandas as pd
import subprocess
from glob import glob
from scripts import _run


# Main Streamlit application
def main():

    # Load the data
    # data = read_file('data/grub_boot_defaults')
    # df = pd.DataFrame(data, columns=['MAC', 'OS to Boot', 'Menu Timeout', 'Hostname'])

    # # Reorder the columns
    # df = df[['Hostname', 'OS to Boot', 'Menu Timeout', 'MAC']]

    # df['OS to Boot'] = pd.Categorical(df['OS to Boot'].replace({str(v): k for k, v in boot_options.items()}))
    # df['Menu Timeout'] = df['Menu Timeout'].astype('int')

    firstScreen = st.empty()
    secondScreen = st.empty()

    filter_logs = glob('data/dropbox-daily-backup/log/*filtered*.log')
    error_logs  = glob('data/dropbox-daily-backup/log/*error*.log')

    def _show_log(log):
        code = ''.join(open(log, 'r').readlines())
        with st.expander("source code"):
            st.code(code, language='bash')

    with firstScreen.container():
        option = st.selectbox('Select the log to display', filter_logs)

    #     cols = st.columns([1,10], gap="small")
    #     scols = cols[0].columns(2, gap="small")
    #     # show = scols[0].button("SHOW CODE", use_container_width=True, args=[script])
    #     run = scols[0].button("Display Log", use_container_width=True, args=[script], type="primary")
    #     # stop = scols[1].button("STOP", use_container_width=True, on_click=_stop, args=[script])

    #     #selection = st_btn_select( ("SHOW CODE", "RUN", "STOP"), index=0, nav=False, key='actions' )

    #     with cols[1]:
    #         _show_code(script)
    #     st.divider()


    #     if run:
    #         _run(script)
    #     # Edit the DataFrame with increased height and full width
    #     # df = st.experimental_data_editor(df, height=800, use_container_width=True)

    #     # OK button
    #     # result = st.button('Display Log', key='ok_button', use_container_width=True, type="primary")
    #     result = st.button('Display Log', key='ok_button', type="primary")

    # if result:
    #     # "clear screen"
    #     firstScreen.empty()

    #     with secondScreen.container():
    #         st.warning("Please wait wile the server applies the changes. Please avoid booting any machines during this process since the network boot files are being altered and it can cause failed boot!")

    #     # Ensure that 'Menu Timeout' is integer before writing to the file
    #     try:
    #         df['Menu Timeout'] = df['Menu Timeout'].astype('int')
    #     except ValueError:
    #         st.error("Please enter valid integer values for the 'Menu Timeout' column.")
    #         return

    #     # Write the changes to the file
    #     data = df.values.tolist()
    #     write_file('data/grub_boot_defaults', data)

    #     # Run the shell command
    #     expander = st.expander("applying changes...", expanded=True)
    #     # with expander:
    #     status = _run('data/grub_boot_defaults_apply.sh') #, maxsize=600)

    #     secondScreen.empty()
    #     with secondScreen.container():
    #         if status == 0:
    #             st.success("The network boot changes have been applied susscessfully!")
    #             if st.button('DONE', use_container_width=True, type="primary"):
    #                 st.experimental_rerun()
    #         else:
    #             st.error("The network boot changes have failed to apply. \nPlease inform this to your pipeVFX administrator asap as your network boot may be disrupted at this point.")

if __name__ == "__main__":
    main()
