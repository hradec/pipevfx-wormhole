
import os, glob, time, subprocess

import streamlit as st
import streamlit.components.v1 as components
from st_btn_select import st_btn_select
import redirect as rd


scripts_folder = os.path.abspath(os.path.dirname(__file__)+'/../')

# use the full area of the browser - need to be called before everything else
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_title="pipevfx-wormhole")

# Initialize a session state variable that tracks the sidebar state (either 'expanded' or 'collapsed').
if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'expanded'

# Initialize session state
if 'script' not in st.session_state:
    st.session_state.script = None

# Check if URL has parameter
params = st.experimental_get_query_params()
if 'script' in params:
    st.session_state.script = params['script'][0]

def sidebar():
    with st.sidebar:
        buttons = []
        dbuttons = {}
        scripts = glob.glob( f"{scripts_folder}/scripts/*" )
        scripts.sort()
        for each in scripts:
            each = os.path.abspath(each)
            if os.path.isfile(each):
                # buttons += [ st.radio( os.path.basename(each), on_change=sidebar_runscript, args=[each] ) ]
                buttons += [ each ]
                dbuttons[ os.path.basename(each) ] = each

        selected = 0
        if hasattr(st.session_state, 'script') and st.session_state.script:
            keys = list(dbuttons.keys())
            sel = [ x for x in keys if st.session_state.script in x ]
            if sel:
                selected = keys.index( sel[0] )

        script = st.radio(f'select the scritp to run:', options=dbuttons.keys(), index = selected)
        ret = dbuttons[script]
        st.session_state.script = ret
        return ret

def _show_code(script):
    code = ''.join(open(script, 'r').readlines())
    with st.expander("source code"):
        st.code(code, language='bash')

def _run(script, maxsize = None):
    st.session_state.kill = False
    if maxsize:
        st.markdown("""
            <style>
            pre {
                max-height: %dpx;
            }
            </style>
        """ % maxsize, unsafe_allow_html=True)
    with rd.stdout():
        proc = subprocess.Popen( [script], shell=False, bufsize=1, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print("="*200)
        status = 0
        while True:
            status = proc.poll()
            print(status)
            if st.session_state.kill:
                proc.kill()
            if status == None:
                # outs = None
                # try:
                #     outs, errs = proc.communicate(timeout=1)
                # except subprocess.TimeoutExpired:
                #     #proc.kill()
                #     #outs, errs = proc.communicate()
                #     pass
                # # print(st.session_state.kill)
                # print(">",outs)
                # if outs:
                #     for l in outs.splitlines():

                for l in iter(proc.stdout.readline, b''):
                        print( l.decode("utf-8").strip()  )
                        # components.html("""
                        #     <script language="javascript">
                        #     $("span").last()[0].scrollIntoView({ behavior: 'smooth' });
                        #     </script>
                        # """)

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
    return status

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
