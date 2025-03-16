import pandas as pd
import streamlit as st
import random

def clear_all():
	st.session_state["P1"]=False
	st.session_state["P2"]=False
	st.session_state.index1 = list(range(0, len(players)))
	st.session_state.index2 = list(range(0, len(players)))
	return
	
st.title(":rainbow[** Game - Random Picker **]")	

try:
	file = st.sidebar.file_uploader("**Upload an Excel file - ID/Name must be in first column**")
	df = pd.read_excel(file)
	players = list(df.iloc[:,0])

	if "index1" not in st.session_state:
		st.session_state.index1 = list(range(0, len(players)))

	if "index2" not in st.session_state:
		st.session_state.index2 = list(range(0, len(players)))

	st.markdown("### Select the Random Players")

	p1 = st.checkbox("Player 1", ["Player 1"], key="P1")
	p2 = st.checkbox("Player 2", ["Player 2"], key="P2")

	col = st.columns(2)

	try:
		with col[0]:
			if st.button("Submit", type = "primary"):

				if p1:
					random.shuffle(st.session_state.index1)
					st.text(f"Player 1: {players[st.session_state.index1.pop()]}")
	
				if p2:
					random.shuffle(st.session_state.index2)
					st.text(f"Player 2: {players[st.session_state.index2.pop()]}")
	except:
		st.write("List complete..click on **Restart** button to start over")

	with col[1]:
		st.button("Restart", on_click = clear_all, type = "primary")
except:
	pass