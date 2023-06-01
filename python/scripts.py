
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

def _show_code(script):
    code = ''.join(open(script, 'r').readlines())
    with st.expander("source code"):
        st.code(code, language='bash')

def _run(script):
    st.session_state.kill = False
    with rd.stdout():
        proc = subprocess.Popen( [script], shell=False, bufsize=1, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print("="*200)
        while True:
            status = proc.poll()
            if st.session_state.kill:
                proc.kill()
            if status == None:
                outs = None
                try:
                    outs, errs = proc.communicate(timeout=1)
                except subprocess.TimeoutExpired:
                    #proc.kill()
                    #outs, errs = proc.communicate()
                    pass
                print(st.session_state.kill)
                if outs:
                    for l in outs.splitlines():
                        print( l.decode("utf-8")  )

            elif status == 0:
                # harvest the answers
                print("=" * 200)
                print( "finished susscessfully - return code:", status)
                break
            else:
                print("=" * 200)
                print( "command failed - return code:", status )
                break
            time.sleep(0.01)
            # print("="*200)

def _stop(script):
    st.session_state.kill = True

script = sidebar()

with st.container():
    st.write("## %s" % os.path.basename(script), )

    if os.path.splitext(script.lower())[-1] in ['.py']:
        exec( ''.join(open(script,'r').readlines()) )
    else:
        cols = st.columns([1,10], gap="small")
        scols = cols[0].columns(2, gap="small")
        # show = scols[0].button("SHOW CODE", use_container_width=True, args=[script])
        run = scols[0].button("RUN", use_container_width=True, args=[script], type="primary")
        stop = scols[1].button("STOP", use_container_width=True, on_click=_stop, args=[script])

        #selection = st_btn_select( ("SHOW CODE", "RUN", "STOP"), index=0, nav=False, key='actions' )

        with cols[1]:
            _show_code(script)
        st.divider()


        if run:
            _run(script)
