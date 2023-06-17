from gingerit.gingerit import GingerIt
import streamlit as st
import pandas as pd
import subprocess
import time


def process_text(text):
    parser = GingerIt()
    result_dict = parser.parse(text)

    corrections = result_dict['corrections']
    df_data = []
    for correction in corrections:
        df_data.append({
            'index_num': correction['start'],
            'incorrect_words': correction['text'],
            'correct_words': correction['correct'],
            'definition': correction['definition']
    })
    
    df = pd.DataFrame(df_data).sort_values('index_num')
    return df, result_dict['result']

def all_results():
    st.title('Grammar & Spell Checker in Python')
    text = st.text_area("Enter text:")
    
    if st.button('Correct Sentence'):
        if not text:
            st.write("Please enter text for checking spelling")
        else:
            df, corrected_text = process_text(text)
            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.1)
                my_bar.progress(percent_complete + 1, text=progress_text)
            st.write("Parsing completed successfully")
            st.balloons()
            st.markdown('Corrected Sentence - ' + corrected_text)
            st.button("Corrections")
            st.dataframe(df, use_container_width=True)


if __name__ == '__main__':
    all_results()
    