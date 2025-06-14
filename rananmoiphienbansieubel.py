import streamlit as st
import random
import time

st.set_page_config(page_title="Rắn Ăn Mồi Chấm Tròn", layout="centered")

# Game Config
GRID_SIZE = 20
CELL_SIZE = 25
INIT_LENGTH = 3

# Init session state
if "snake" not in st.session_state:
    st.session_state.snake = [(5, 5 - i) for i in range(INIT_LENGTH)]
    st.session_state.direction = (0, 1)  # (row, col)
    st.session_state.food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
    st.session_state.score = 0
    st.session_state.game_over = False

def move_snake():
    if st.session_state.game_over:
        return

    head = st.session_state.snake[0]
    dx, dy = st.session_state.direction
    new_head = ((head[0] + dx) % GRID_SIZE, (head[1] + dy) % GRID_SIZE)

    if new_head in st.session_state.snake:
        st.session_state.game_over = True
        return

    st.session_state.snake.insert(0, new_head)

    if new_head == st.session_state.food:
        st.session_state.score += 1
        while True:
            new_food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
            if new_food not in st.session_state.snake:
                break
        st.session_state.food = new_food
    else:
        st.session_state.snake.pop()


def draw_board():
    board = ""
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i, j) == st.session_state.food:
                board += f"<span style='color: red;'>●</span>"
            elif (i, j) in st.session_state.snake:
                board += f"<span style='color: green;'>●</span>"
            else:
                board += "<span style='color: lightgray;'>.</span>"
        board += "<br>"
    st.markdown(f"<div style='font-size: 16px; font-family: monospace;'>{board}</div>", unsafe_allow_html=True)


st.title("🟢 Game Rắn Ăn Chấm Tròn")
st.caption("Di chuyển bằng nút bấm. Chấm xanh là rắn, đỏ là mồi 🟥")
st.write(f"**Điểm số:** {st.session_state.score}")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️"):
        st.session_state.direction = (0, -1)
with col2:
    if st.button("⬆️"):
        st.session_state.direction = (-1, 0)
    if st.button("⬇️"):
        st.session_state.direction = (1, 0)
with col3:
    if st.button("➡️"):
        st.session_state.direction = (0, 1)

move_snake()
draw_board()

if st.session_state.game_over:
    st.error("💀 Trò chơi kết thúc! Rắn tự cắn chính mình!")
    if st.button("Chơi lại"):
        for key in ["snake", "direction", "food", "score", "game_over"]:
            st.session_state.pop(key, None)
        st.experimental_rerun()
else:
    time.sleep(0.1)
    st.experimental_rerun()
