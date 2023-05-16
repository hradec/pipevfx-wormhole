
import os, glob, time, subprocess

import streamlit as st
from st_btn_select import st_btn_select
import redirect as rd


scripts_folder = os.path.abspath(os.path.dirname(__file__)+'/../')

# use the full area of the browser - need to be called before everything else
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_title="pipevfx-wormhole")

# Initialize a session state variable that tracks the sidebar state (either 'expanded' or 'collapsed').
if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'expanded'

def sidebar():
    with st.sidebar:
        buttons = []
        dbuttons = {}
        for each in glob.glob( f"{scripts_folder}/scripts/*" ):
            each = os.path.abspath(each)
            if os.path.isfile(each):
                # buttons += [ st.radio( os.path.basename(each), on_change=sidebar_runscript, args=[each] ) ]
                buttons += [ each ]
                dbuttons[ os.path.basename(each) ] = each

        selected = 0
        if hasattr(st.session_state, 'script'):
            if st.session_state.script in dbuttons.keys():
                selected = dbuttons.keys().index( st.session_state.script )

        script = st.radio('select the scritp to run:', options=dbuttons.keys(), index = selected)
        ret = dbuttons[script]
        st.session_state.script = ret
        return ret

script = sidebar()
#cols = st.columns(4,gap="small")
st.write("## %s" % os.path.basename(script), )
selection = ''
selection = st_btn_select( ("SHOW CODE", "RUN", "STOP"), index=0, nav=False )
st.divider()

print(selection)
if selection == "SHOW CODE":
    code = ''.join(open(script, 'r').readlines())
    st.code(code, language='bash')

elif selection == "RUN":
        with rd.stdout():
            proc = subprocess.Popen( [script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("="*200)
            while True:
                status = proc.poll()
                if status == None:
                    try:
                        outs, errs = proc.communicate(timeout=15)
                    except TimeoutExpired:
                        proc.kill()
                        outs, errs = proc.communicate()
                    print(type(outs))
                    for l in outs.splitlines():
                        print( l.decode("utf-8")  )
                    #print( errs )
                elif status == 0:
                    # harvest the answers
                    print("=" * 200)
                    print( "finished susscessfully - return code:", status)
                    break
                else:
                    print("=" * 200)
                    print( "command failed - return code:", status )
                    break
                time.sleep(0.1)
            print("="*200)

elif selection == "STOP":

    pass