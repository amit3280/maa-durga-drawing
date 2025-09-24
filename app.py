# app.py
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.set_page_config(page_title="Maa Durga Drawing")

st.title("🕉️ Maa Durga Drawing (Matplotlib Version)")

# Create figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor("gold")
ax.set_xlim(-200, 200)
ax.set_ylim(-200, 200)
ax.axis("off")

# --------------------
# Tika (Red Circle)
# --------------------
tika = patches.Circle((0, 120), 25, color="red")
ax.add_patch(tika)

# --------------------
# Eyes
# --------------------
# Left eye (outer shape like almond)
left_eye = patches.Ellipse((-70, 40), 100, 50, color="white")
ax.add_patch(left_eye)
ax.add_patch(patches.Ellipse((-70, 40), 40, 40, color="black"))  # pupil
ax.add_patch(patches.Circle((-55, 50), 10, color="white"))       # shine

# Right eye
right_eye = patches.Ellipse((70, 40), 100, 50, color="white")
ax.add_patch(right_eye)
ax.add_patch(patches.Ellipse((70, 40), 40, 40, color="black"))   # pupil
ax.add_patch(patches.Circle((55, 50), 10, color="white"))        # shine

# Eyebrows
ax.plot([-120, -20], [80, 90], color="black", linewidth=8)
ax.plot([20, 120], [90, 80], color="black", linewidth=8)

# --------------------
# Nose (curve)
# --------------------
nose = patches.Arc((0, 0), 40, 60, theta1=200, theta2=340, color="black", linewidth=4)
ax.add_patch(nose)

# --------------------
# Lips
# --------------------
upper_lip = patches.Arc((0, -60), 120, 40, theta1=0, theta2=180, color="red", linewidth=8)
lower_lip = patches.Arc((0, -70), 120, 40, theta1=180, theta2=360, color="red", linewidth=8)
ax.add_patch(upper_lip)
ax.add_patch(lower_lip)

# --------------------
# Nose Ring
# --------------------
nosering = patches.Arc((50, -20), 140, 140, theta1=30, theta2=270, color="yellow", linewidth=6)
ax.add_patch(nosering)

# Show figure in Streamlit
st.pyplot(fig)

