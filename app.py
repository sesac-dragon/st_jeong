import streamlit as st
import os

st.title('배포 테스트')
st.write('배포 테스트용 앱입니다.')

api_key = os.environ.get('API_SECRET_KEY')

st.write(f'api key = {api_key}')

if not os.environ.get('DB_HOST'):
    st.write('DB 접속정보가 없습니다.')
else:
    conn = pymysql.connect(host=os.environ.get("DB_HOST"))