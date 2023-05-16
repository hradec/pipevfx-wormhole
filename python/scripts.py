
import streamlit as st
import os, glob

import redirect as rd
import time

# use the full area of the browser - need to be called before everything else
st. set_page_config(layout="wide")

scripts_folder = os.path.abspath(os.path.dirname(__file__)+'/../')



# left_column, right_column = st.columns([1])
# # You can use a column just like st.sidebar:
# def button():
#     # with st.spinner("please wait"):
#     list = glob.glob(os.environ['HOME']+"/*")
#     os.system("ls -l %s" % os.environ['HOME']+"/*")
#     # os.system("ls -l %s" % os.environ['HOME']+"/*")
#     print(list)
#     # with rd.stdout, rd.stderr(format='markdown', to=st.sidebar):
#     with rd.stdout(max_buffer=1024, to=left_column):
#         for line in list:
#             print(f"> {line}")
#             time.sleep(0.01)
#     # left_column.success("list:\n"+'<BR>'.join(list))
#
# left_column.button('Press me!', on_click=button)

# Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")
#



# Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )
#
# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )
def sidebar_runscript( *args ):
    print(args[0])
    sidebar()

def sidebar():
    with st.sidebar:
        buttons = []
        for each in glob.glob( f"{scripts_folder}/scripts/*" ):
            buttons += [ st.button( os.path.basename(each), on_click=sidebar_runscript, args=[each] ) ]
sidebar()
