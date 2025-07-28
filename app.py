
import streamlit as st

# --- CONFIGURATION ---
VALID_USERNAME = "maphe"
VALID_PASSWORD = "06282025"
FLOWER_EMOJI = "🌷🌸💐"
GIFT_EMOJI = "🎁"
MESSAGE = """
Congratulations on your graduation, Princess Luna 🌙!

You are now finally a big girl. You will earn lots of money, experience different things, and learn more about yourself.

Don’t worry— as long as I can, I will be with you every step of the way. Behind you, supporting you (and maybe jokingly, fucking you 😏—just kidding—kind of). I mean it when I say I hope I can help you grow... and vice versa, you help me too.

We’ll spend another era with you being the best version of yourself.

Don’t worry about sad times — we’ll talk through them.
Don’t worry about the fun times — we’ll make them together.

When you grow more, promise not to leave me out.
And when I do, I won’t leave you out either.

I don’t like the words ‘growing apart.’ Let’s grow individually and together.

I hope we’ll make it through this year and the next — congrats again, Sayang! 🎓💕

---

And I’d like to add that I like you, sayang. It’s been proven time and time again — I really like you just as you are.

You’re the light in my darkest days.
You make me feel alive.
And you like me... as *I* am, too.

— From Rabin 💌
"""

ROMANTIC_QUESTION = "💍 Do you want to take this relationship to the next level? If you're not ready, I can wait too... 💗"

st.set_page_config(page_title="Princess Luna's Graduation Gift 🎓", page_icon=GIFT_EMOJI, layout="centered")

# --- SESSION STATE ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "gift_opened" not in st.session_state:
    st.session_state.gift_opened = False

# --- LOGIN FUNCTION ---
def attempt_login(user, pw):
    if user == VALID_USERNAME and pw == VALID_PASSWORD:
        st.session_state.logged_in = True
    else:
        st.error("🚫 Invalid username or password. Hint: The date of the day we met.")

# --- GIFT OPEN FUNCTION ---
def open_gift():
    st.session_state.gift_opened = True

# --- UI ---
if not st.session_state.logged_in:
    st.title("🔐 Login to Open Your Gift")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        attempt_login(username, password)

else:
    st.title("🎁 Your Surprise Gift")
    st.markdown("Click the box below to open it!")

    if not st.session_state.gift_opened:
        st.button(GIFT_EMOJI + " Tap to Open", on_click=open_gift)
    else:
        st.balloons()
        st.markdown(f"## {FLOWER_EMOJI}")
        st.success(MESSAGE)
        st.markdown(f"### {ROMANTIC_QUESTION}")

        st.image("https://i.imgur.com/lyLUUkk.jpg", caption="Anton from RIIZE 💖", use_container_width=True)
