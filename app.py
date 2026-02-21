import streamlit as st
import requests

st.title("🍁 메이플스토리 데이터 센터")

nickname = st.text_input("캐릭터 닉네임을 입력하세요")

if st.button("조회"):
    st.write(f"{nickname} 님의 정보를 찾는 중입니다...")
    # 여기에 나중에 API 기능을 넣을 거예요!
