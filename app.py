# -*- coding: utf-8 -*-
"""

@author: SATHIRA
"""

import streamlit as st
from PIL import Image
    
# app setup 
try:

    from helper_functions import *

    # app design
    #app_meta('📊')
    set_bg_hack('dqw_background.png')

    
    # hide warning for st.pyplot() 
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    # Main panel setup
    display_app_header(main_txt='DatCon Data Converter',
                       sub_txt='Clean and make analyzable your complex text data with DatCon')
    
    st.markdown("""---""")
    
    st.write('Welcome to the DatCon! An app for data processing.')
    
    st.write('Please continue with the instructions below')

    url = 'https://github.com/SathiraKumarasinghe/DatCon_text_app/blob/main/text_data.py'

    st.markdown(f'''
    <a href={url}><button style="background-color:GreenYellow;">Continue</button></a>
    ''',
    unsafe_allow_html=True)
    
    
    #app_section_button('[Continue📚](C:/Users/User/Desktop/CDAP_2022/text_app/text_eda/text_data.py)')
    #st.markdown("""---""")

    intro_text = """
    The DatCon is an Web Application for Data restructuring and preprocessing.
    DatCon helps to increase analytical capabilities of unstructured text Data.
    """
    intro = st.expander("Click here for more info about DatCon App")

    with intro:
        sub_text(intro_text)

    

    

except KeyError:
    st.error("Please select a key value from the dropdown to continue.")
    
except ValueError:
    st.error("Oops, something went wrong. Please check previous steps for inconsistent input.")
    
except TypeError:
    st.error("Oops, something went wrong. Please check previous steps for inconsistent input.")
