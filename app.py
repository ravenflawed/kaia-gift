
import streamlit as st

# --- CONFIGURATION ---
VALID_USERNAME = "maphe"
VALID_PASSWORD = "06282025"
FLOWER_EMOJI = "🌷🌸💐"
GIFT_EMOJI = "🎁"
MESSAGE = """
Congratulations on your graduation, Princess Luna.
You’ve grown so much, and I’m incredibly proud of you. You’re officially a big girl now—ready to earn your own money, explore new experiences, and continue discovering who you are.

You’re entering a new era of your life—and I hope I get to walk beside you through all of it.
Whether you’re growing, hurting, healing, or glowing, I want to be here. Behind you. Supporting you. (And maybe... you know... behind you in other ways too 😏—just kidding. Kind of.)

I genuinely want to help you grow, and I hope you’ll help me grow too.
Let’s spend this next chapter together—becoming the best versions of ourselves, not just side-by-side, but intertwined.

There will be sad days, but we’ll talk through them.
There will be fun days, and we’ll make the most of them together.

If you ever grow more—promise not to leave me behind.
And when I do, I won’t leave you behind either.

I don’t believe in “growing apart.” I believe in growing individually and together.
So let’s try to do that. Every day. Just us.

And before I end this, I just want to say it out loud—I really, really like you, Sayang.
It’s been proven time and time again, hasn’t it?

You’re the light in my darkest days.
You make me feel alive.
And you liked me as I am—when I didn’t expect anyone to.

I don’t want to waste time chasing anyone else.
I’ve found you. And to me, that’s more than enough.

It’s already been a month like you said—and I think that’s more than enough time for me to know this feeling is real.

You, baby girl, are someone I genuinely want. 💗

So…
"""

ROMANTIC_QUESTION = "💍 Do you want to take this relationship to the next level? If you're not ready, I can wait too... 💗 You are worth the wait."

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

        st.image(
    "https://upload.wikimedia.org/wikipedia/commons/3/36/20231124_Anton_Lee_%28Riize%29.jpg",
    caption="With love Rabin💖",
    use_container_width=True
)
