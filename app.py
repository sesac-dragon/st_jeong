import streamlit as st

@st.cache_data
def load_data():
    return

load_data()

st.title('my first app')
st.write('hello')
st.write('안녕')

with st.sidebar:
    st.title('메뉴')

col = st.columns(3)
with col[0]:
    st.metric('주가', '3.77', 0.2)
with col[1]:
    st.metric('거래량', '5.4m', -0.7)

with col[2]:
    st.metric('abc', 'def', 123)

with st.expander('상세정보'):
    st.table([
        'a', 'b', 'c'
    ])

v = st.button('클릭')
print(v)

if v:
    st.write('버튼 클릭됨.')

st.slider('볼륨')

name = st.text_input('이름')
st.write(name)