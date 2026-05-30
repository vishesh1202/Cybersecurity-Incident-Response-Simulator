import streamlit as st

st.set_page_config(
    page_title="Cybersecurity Incident Response Simulator",
    layout="wide"
)

st.title("🛡️ Cybersecurity Incident Response Simulator")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Incidents Detected", 8)

with col2:
    st.metric("Average Response Time", "12 mins")

with col3:
    st.metric("Playbooks Executed", 8)

st.divider()

st.subheader("Active Threats")

st.table([
    {"Threat":"Ransomware","Severity":"Critical"},
    {"Threat":"Phishing","Severity":"High"},
    {"Threat":"Brute Force","Severity":"Medium"}
])

st.divider()

st.subheader("MITRE ATT&CK Mapping")

st.code("""
T1566 - Phishing
T1110 - Brute Force
T1021 - Lateral Movement
T1486 - Ransomware
""")