import streamlit as st
import time



st.title('streamlit 超入門')
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.3)

'Done'





left_colum,right_colum = st.beta_columns(2)
button = left_colum.button('右カラムに文字を表示')
if button:
    right_colum.write('ここは右カラム')
