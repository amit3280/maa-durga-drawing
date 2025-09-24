import turtle
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Maa Durga Drawing", page_icon="🕉️", layout="centered")
st.title("🕉️ Maa Durga Drawing with Python Turtle")

# Hide the main turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
canvas = screen.getcanvas()

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# --- Example: Replace this with your Durga drawing ---
t.color("red")
t.begin_fill()
t.circle(100)
t.end_fill()
# ----------------------------------------------------

# Save as PostScript
canvas.postscript(file="durga.ps")

# Convert to PNG
img = Image.open("durga.ps")
img.save("durga.png")

# Show in Streamlit
st.image("durga.png", caption="Maa Durga (drawn with Python Turtle)", use_column_width=True)

st.success("Drawing rendered successfully ✅")

