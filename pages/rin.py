"""
Rin's Personal Workspace Route (/rin)
"""
import streamlit as st
import streamlit.components.v1 as components

# Set Rin mode
st.query_params["page"] = "rin"
st.session_state["is_rin_mode"] = True

# 1. Try native switch_page to main entrypoint
try:
    st.switch_page("scripts/app.py")
except Exception:
    try:
        st.switch_page("app.py")
    except Exception:
        pass

# 2. JS redirection in parent frame to root with query param
components.html("""
<script>
try {
    if (window.parent && window.parent.location) {
        window.parent.location.href = '/?page=rin';
    } else {
        window.location.href = '/?page=rin';
    }
} catch(e) {
    window.location.href = '/?page=rin';
}
</script>
""", height=0)

st.markdown("""
<div style="font-family: sans-serif; text-align: center; padding: 40px;">
    <h3>⏳ Đang chuyển sang Rin Workspace...</h3>
    <p><a href="/?page=rin" target="_self">Nhấp vào đây nếu không tự động chuyển hướng</a></p>
</div>
""", unsafe_allow_html=True)
