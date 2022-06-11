import streamlit as st
from game import create_board, place, random_place, evaluate

# init game in np & tie to st
if "board" not in st.session_state:
    st.session_state.board = create_board()

board = st.session_state.board
def human_game():
    res = -1
    
    while True:
        if evaluate(board) == -1: break
        for player in [1, 2]:
            if evaluate(board) == -1: break
            random_place(board, player)
        
        res = evaluate(board)
        
    return res


# Init game on streamlit
st.set_page_config(layout="centered")
st.header("Tic Tac Toe ❎🅾️")

def refresh():
    for k in st.session_state:
        del st.session_state[k]

replay = st.button("Replay")
if replay:
    refresh()

# state & pos of every specific btn of all 9 btns
for k in range(3):
    for i in range(1, 4):
        btn_checked = f"{i**2-k}_checked"
        # pos in np 2d-array board
        btn_position = (k, i-1)
        btn_pos = f"pos{i**2-k}"
        
        if not btn_checked in st.session_state:
            st.session_state[btn_checked] = '.'
        if not btn_pos in st.session_state:
            st.session_state[btn_pos] = btn_position

if not "turn" in st.session_state:
    st.session_state.turn = 'X'

def play(btn_key):
    """play on specific button using btn_key"""
    position = st.session_state[f"pos{btn_key}"]
    if st.session_state[f"{btn_key}_checked"] == '.':
        if st.session_state.turn == 'X':
            st.session_state[f"{btn_key}_checked"] = 'X'
            place(board, 1, position) # 1 -> X
            st.session_state.turn = 'O'
        elif st.session_state.turn == 'O':
            st.session_state[f"{btn_key}_checked"] = 'O'
            place(board, 2, position) # 2 -> O
            st.session_state.turn = 'X'

        if evaluate(board) == 1:
            st.success("Congrats! X wins!")
            st.balloons()
            refresh()
        elif evaluate(board) == 2:
            st.success("Congrats! O wins!")
            st.balloons()
            refresh()

# Create board and init btns
for k in range(3):
    cols = st.columns(3)
    for i, col in enumerate(cols[0:3], start=1):
        # distinguish every btn during play & session reload
        btn_key = i**2-k  
        col.button(
        st.session_state[f"{btn_key}_checked"], key=btn_key, on_click=play, args=(btn_key,)
        ) 






