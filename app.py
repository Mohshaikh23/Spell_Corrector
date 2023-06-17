from gingerit.gingerit import GingerIt
import streamlit as st
import pandas as pd

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

def main():
    st.title('Grammar & Spell Checker in Python')
    text = st.text_area("Enter text:")
    
    if st.button('Correct Sentence'):
        if not text:
            st.write("Please enter text for checking spelling")
        else:
            df, corrected_text = process_text(text)
            st.markdown('Corrected Sentence - ' + corrected_text)
            st.button("Corrections")
            st.dataframe(df, use_container_width=True)

if __name__ == '__main__':
    main()
