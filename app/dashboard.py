import streamlit as st

st.title("AI-Based Intrusion Detection System (IDS)")

with open('logs/ids_log.txt', 'r') as log_file:
    logs = log_file.readlines()

if logs:
    st.subheader("Intrusion Alerts:")
    for log in logs:
        st.write(log)
else:
    st.write("No intrusions detected.")

