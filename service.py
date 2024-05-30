import streamlit as st
import pandas as pd
import numpy as np
from main import main

nii_input = st.file_uploader('Выберите файл:', type=['nii'])

def analyze():
    main(nii_input.read())




bt = st.button('Обработать снимок', on_click=analyze)

