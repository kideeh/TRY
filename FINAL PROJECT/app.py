# app.py
import streamlit as st
import time
import random
from difflib import get_close_matches
from database import (
    init_db,
    create_user,
    verify_user_code_in_db,
    set_verified,
    verify_login,
    get_user_by_email,
    update_free_uses,
    grant_subscription,
    add_history,
    get_history_for_user,
    mark_user_verified,
)
from herbs_data import HERBS_DATA

# -------------------------
# Config & Theme
# -------------------------
st.set_page_config(page_title="AI for Traditional Healing", page_icon="🌿", layout="centered")

st.markdown(
    """
    <style>
    body { background-color: #f3fff5; }
    .stApp { color: #0b2f1b; }
    .stButton>button {
        color: white;
        background: linear-gradient(180deg,#2e8b57,#276a48);
        border-radius: 8px;
        padding: .6rem 1rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        background: linear-gradient(180deg,#3ba469,#2b7d54);
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>select {
        background: #ffffff !important;
        color: #111111 !important;
        border: 1px solid #2e8b57 !important;
        border-radius: 6px !important;
        padding: .5rem !important;
    }
    .css-1d391kg { background-color: #f6fff6 !important; }
    h1,h2,h3 { color: #0b6623; font-weight:700; }
    .card { background: #fff; border-radius: 10px; padding: 1rem; box-shadow: 0 1px 6px rgba(0,0,0,0.05); margin-bottom: 0.9rem; border: 1px solid #dff3e6; }
    .subscription { background-color: #ffffff !important; color: #0b2f1b !important; padding: 1rem; border-radius: 10px; border: 1px solid #cfead6; }
    .hero { padding: 1rem; border-radius:12px; background: linear-gradient(180deg,#ffffff,#f1fff4); border:1px solid #dff3e6; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Initialize DB
# -------------------------
DB_PATH = "users.db"
init_db(DB_PATH)

# -------------------------
# Session defaults
# -------------------------
DEFAULTS = {
    "page": "🏠 Home",
    "logged_in": False,
    "email": None,
    "free_uses": 0,
    "pending_user": None,
    "next_action": None,
}
for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

def navigate_to(page):
    st.session_state.page = page
    try:
        st.rerun()
    except Exception:
        pass

# -------------------------
# Sidebar
# -------------------------
menu = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🔐 Register/Login", "💳 Subscription", "🌿 AI Tool"],
    index=["🏠 Home", "🔐 Register/Login", "💳 Subscription", "🌿 AI Tool"].index(st.session_state.page),
)
st.session_state.page = menu

# -------------------------
# HOME (rich)
# -------------------------
if st.session_state.page == "🏠 Home":
    st.markdown("<div class='hero'>", unsafe_allow_html=True)
    st.title("🌿 AI for Traditional Healing")
    st.markdown("### Intelligent guidance, rooted in local herbal knowledge")
    st.write(
        "Welcome! This app helps you translate symptoms (English or Kiswahili) into suggested local herbal remedies, "
        "simple healing actions, and safety guidance. It is informational only — not a replacement for medical care."
    )
    st.markdown("---")
    st.subheader("Why this matters")
    st.write(
        "- Preserve traditional knowledge while adding an easy-to-use interface.\n"
        "- Designed for accessibility and quick community usage.\n"
        "- Simple verification & free trial to let users test the tool."
    )
    st.markdown("---")
    st.subheader("How to use (quick)")
    st.write(
        "1. Register — create an account (name, email, password).  \n"
        "2. Verify — a 4-digit code will appear on-screen; enter it to activate your trial.  \n"
        "3. Try — you get **2 free checks**; the AI suggests herbs + safety tips.  \n"
        "4. Subscribe — unlock unlimited access (demo payments not included)."
    )
    c1, c2 = st.columns([2,1])
    with c2:
        if st.button("🚀 Start — Register"):
            st.session_state.next_action = "Register"
            navigate_to("🔐 Register/Login")
    st.caption("© 2025 AI for Traditional Healing — Built with care in Kenya 🇰🇪")
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# REGISTER / VERIFY / LOGIN
# -------------------------
elif st.session_state.page == "🔐 Register/Login":
    st.header("Register / Verify / Login")

    options = ["Register", "Verify Account", "Login"]

    # Determine default index for selectbox
    default_index = 0
    next_action = st.session_state.get("next_action")
    if next_action in options:
        default_index = options.index(next_action)

    # Always define 'action'
    action = next_action if next_action else st.selectbox("Action", options, index=default_index)

    # Clear next_action if it was used
    if next_action:
        st.session_state.pop("next_action")

    # ---------- REGISTER ----------
    if action == "Register":
        st.subheader("Create an account")
        st.markdown("Placeholders inside the inputs show expected values.")
        name = st.text_input("Full name", key="reg_name", placeholder="e.g. Asha Mohamed")
        email = st.text_input("Email address", key="reg_email", placeholder="you@example.com")
        password = st.text_input("Password", type="password", key="reg_password", placeholder="Choose a secure password")

        if st.button("Register"):
            if not (name and email and password):
                st.warning("Please complete all fields.")
            else:
                email_l = email.strip().lower()
                ok, msg = create_user(DB_PATH, name.strip(), email_l, password)
                if not ok:
                    st.error(msg)
                else:
                    code = str(random.randint(1000, 9999))
                    verify_user_code_in_db(DB_PATH, email_l, code)
                    st.session_state.pending_user = {"name": name.strip(), "email": email_l, "code": code}
                    st.balloons()
                    st.success(f"Account created for {name.strip()} — verification code: **{code}** (demo).")
                    st.info("Enter this 4-digit code in the next step to activate your 2 free checks.")
                    st.session_state.next_action = "Verify Account"
                    time.sleep(0.9)
                    st.rerun()

    # -------------------------
    # VERIFY ACCOUNT
    # -------------------------
    elif action == "Verify Account":
        st.subheader("Verify Your Account")

        pending = st.session_state.get("pending_user")
        if not pending:
            st.warning("You need to register first before verification.")
            if st.button("Go to Register"):
                st.session_state["next_action"] = "Register"
                st.rerun()
        else:
            st.write(f"Verifying account for **{pending['email']}**")
            code_input = st.text_input("Enter 4-digit code shown on screen", key="verify_code")

            if st.button("Verify"):
                correct_code = pending["code"]
                if code_input.strip() == correct_code:
                    mark_user_verified(pending["email"])
                    st.session_state.verified = True
                    st.session_state.free_uses = 2
                    st.success("✅ Account verified! You now have 2 free uses.")
                    st.session_state["next_action"] = "Login"
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ Invalid code. Please try again.")

    # ---------- LOGIN ----------
    elif action == "Login":
        st.subheader("Login")
        st.markdown("Use your registered email and password.")

        email_in = st.text_input("Email", key="login_email", placeholder="you@example.com")
        pw_in = st.text_input("Password", type="password", key="login_pw", placeholder="Your password")

        if st.button("Login"):
            if not (email_in and pw_in):
                st.warning("Enter both email and password.")
            else:
                login_ok = verify_login(DB_PATH, email_in.strip().lower(), pw_in)
                if not login_ok:
                    st.error("Invalid email or password.")
                else:
                    user = get_user_by_email(DB_PATH, email_in.strip().lower())
                    if not user:
                        st.error("Account not found. Please register.")
                    elif not user.get("verified"):
                        st.warning("Account not yet verified. Please verify before logging in.")
                        st.session_state.next_action = "Verify Account"
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.session_state.logged_in = True
                        st.session_state.email = user.get("email")
                        if user.get("subscribed"):
                            st.session_state.free_uses = 999
                        else:
                            st.session_state.free_uses = user.get("free_uses", 2)
                        st.success("✅ Login successful — redirecting to AI Tool")
                        time.sleep(0.6)
                        navigate_to("🌿 AI Tool")

# -------------------------
# SUBSCRIPTION (demo)
# -------------------------
elif st.session_state.page == "💳 Subscription":
    st.header("Subscription (Demo)")
    st.write("After using your free checks, subscribe to continue. (No real payments in this demo.)")
    st.markdown("<div class='subscription'>", unsafe_allow_html=True)
    plans = {"Daily": "$1", "Weekly": "$5", "Monthly": "$15", "Yearly": "$50"}
    for name, price in plans.items():
        st.markdown(f"**{name} — {price}**")
        if st.button(f"Subscribe — {name}", key=f"sub_{name}"):
            if not st.session_state.logged_in:
                st.warning("Please login first to subscribe.")
            else:
                grant_subscription(DB_PATH, st.session_state.email)
                st.session_state.free_uses = 999
                st.success(f"Subscribed to {name} (demo). Unlimited access unlocked.")
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# AI TOOL
# -------------------------
elif st.session_state.page == "🌿 AI Tool":
    st.header("AI Symptom Checker 🌿")
    if not st.session_state.logged_in:
        st.warning("Please login to use the AI tool.")
        if st.button("Go to Login"):
            navigate_to("🔐 Register/Login")
    else:
        st.write(f"Logged in as: **{st.session_state.email}**")
        st.write(f"Free uses remaining: **{st.session_state.free_uses}**")
        language = st.selectbox("Language / Lugha", ["English", "Kiswahili"], index=0)
        symptoms = st.text_area("Describe your symptoms (English or Kiswahili):", placeholder="e.g. fever and headache, or 'homa na maumivu ya kichwa'")

        col1, col2 = st.columns([2,1])
        with col1:
            if st.button("Analyze Symptoms"):
                if not symptoms or not symptoms.strip():
                    st.warning("Please enter some symptoms.")
                elif st.session_state.free_uses <= 0:
                    st.warning("No free checks left. Please subscribe.")
                    if st.button("Go to Subscription"):
                        navigate_to("💳 Subscription")
                else:
                    st.session_state.free_uses -= 1
                    if st.session_state.email:
                        update_free_uses(DB_PATH, st.session_state.email, st.session_state.free_uses)

                    user_text = symptoms.lower().strip()
                    tokens = [t.strip() for t in user_text.replace(',', ' ').split() if t.strip()]

                    best_match = None
                    best_score = 0.0
                    best_matches_detail = {}

                    for disease, info in HERBS_DATA.items():
                        score = 0.0
                        matched_keywords = []
                        for kw in info["keywords"]:
                            kw_l = kw.lower()
                            if kw_l in user_text:
                                score += 2.0
                                matched_keywords.append((kw, "exact"))
                            else:
                                close = get_close_matches(kw_l, [user_text], n=1, cutoff=0.6)
                                if close:
                                    score += 1.2
                                    matched_keywords.append((kw, "fuzzy"))
                                else:
                                    for tok in tokens:
                                        if tok and (tok in kw_l or kw_l in tok):
                                            score += 0.6
                                            matched_keywords.append((kw, f"partial:{tok}"))
                                            break
                        norm = max(1, len(info["keywords"]))
                        final_score = score / norm
                        if final_score > best_score:
                            best_score = final_score
                            best_match = disease
                            best_matches_detail = {"matched": matched_keywords, "score": final_score}

                    if best_match and best_score >= 0.35:
                        data = HERBS_DATA[best_match]
                        st.success(f"🌿 Possible condition: **{best_match}** — confidence {best_score:.2f}")
                        st.markdown("**Matched evidence:**")
                        if best_matches_detail["matched"]:
                            for m_kw, m_type in best_matches_detail["matched"]:
                                st.write(f"- {m_kw} ({m_type})")
                        herbs = data["herbs"].get(language, data["herbs"]["English"])
                        st.subheader("Recommended Herbs")
                        st.write(", ".join(herbs))
                        st.subheader("Healing Actions")
                        for act in data["actions"]:
                            st.write(f"- {act}")
                        st.info(f"⚕️ Safety: {data['safety']}")
                        add_history(DB_PATH, st.session_state.email, best_match, best_matches_detail, herbs, language, int(time.time()))
                    else:
                        st.error("Could not identify a clear condition. Try clearer symptoms or different keywords.")

        with col2:
            st.subheader("Recent searches")
            history = get_history_for_user(DB_PATH, st.session_state.email, limit=8)
            if not history:
                st.write("No recent searches yet.")
            else:
                for h in history:
                    ts = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(h['timestamp']))
                    st.markdown(f"**{h['predicted']}** — {h['language']} — {ts}")
                    m = h.get('details', {})
                    if m.get('matched'):
                        mm = ", ".join([f"{k}({t})" for k,t in m.get('matched')])
                        st.write(f"Evidence: {mm}")
