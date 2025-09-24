# app.py
import turtle
import streamlit as st
import io
from PIL import Image

st.title("Maa Durga Drawing with Python 🕉️")

# Set up turtle screen
screen = turtle.Screen()
canvas = screen.getcanvas()

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# Example small drawing
t.color("red")
t.begin_fill()
t.circle(50)
t.end_fill()

# Save turtle canvas as postscript
canvas.postscript(file="durga.ps")

# Convert to PNG for Streamlit
img = Image.open("durga.ps")
img.save("durga.png")

st.image("durga.png", caption="Maa Durga")

