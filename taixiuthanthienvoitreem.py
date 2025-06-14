import streamlit as st
import random
import time

st.set_page_config(page_title="Tài Xỉu Thân Thiện s1tg", page_icon="🎲", layout="centered")

st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #ff69b4;'>🎲 Tài Xỉu Thân Thiện s1tg 🎲</h1>
    </div>
""", unsafe_allow_html=True)

if "dice" not in st.session_state:
    st.session_state.dice = [1, 1, 1]
    st.session_state.result = ""

dice_placeholder = st.empty()
result_placeholder = st.empty()

def shake_dice():
    for _ in range(10):
        fake_dice = [random.randint(1, 6) for _ in range(3)]
        dice_str = " | ".join(f"🎲 {d}" for d in fake_dice)
        dice_placeholder.markdown(f"<div style='font-size: 36px; text-align: center;'>{dice_str}</div>", unsafe_allow_html=True)
        time.sleep(0.1)
    # Kết quả cuối cùng
    st.session_state.dice = [random.randint(1, 6) for _ in range(3)]
    total = sum(st.session_state.dice)
    st.session_state.result = "Tài" if total >= 11 else "Xỉu"

if st.button("🎯 Lắc Xúc Xắc!", use_container_width=True):
    shake_dice()

# Hiển thị xúc xắc cuối cùng
dice_str = " | ".join(f"🎲 {d}" for d in st.session_state.dice)
dice_placeholder.markdown(f"<div style='font-size: 36px; text-align: center;'>{dice_str}</div>", unsafe_allow_html=True)

# Hiển thị kết quả
if st.session_state.result:
    result_placeholder.markdown(f"""
        <div style='text-align: center; margin-top: 20px; font-size: 28px; color: #d63384;'>
            👉 Kết quả: <b>{st.session_state.result}</b>
        </div>
    """, unsafe_allow_html=True)
