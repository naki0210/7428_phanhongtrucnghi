import streamlit as st
import random

st.set_page_config(page_title="Tài Xỉu Dễ Thương", page_icon="🎲", layout="centered")

st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #ff69b4;'>🎲 Giả Lập Tài Xỉu Dễ Thương 🎲</h1>
    </div>
""", unsafe_allow_html=True)

if "dice" not in st.session_state:
    st.session_state.dice = [1, 1, 1]
    st.session_state.result = ""

if st.button("🎯 Lắc Xúc Xắc!", use_container_width=True):
    st.session_state.dice = [random.randint(1, 6) for _ in range(3)]
    total = sum(st.session_state.dice)
    st.session_state.result = "Tài" if total >= 11 else "Xỉu"

dice_str = " | ".join(f"🎲 {d}" for d in st.session_state.dice)
st.markdown(f"<div style='font-size: 36px; text-align: center;'>{dice_str}</div>", unsafe_allow_html=True)

if st.session_state.result:
    st.markdown(f"""
        <div style='text-align: center; margin-top: 20px; font-size: 28px; color: #d63384;'>
            👉 Kết quả: <b>{st.session_state.result}</b>
        </div>
    """, unsafe_allow_html=True)
