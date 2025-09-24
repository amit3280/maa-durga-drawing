import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

st.title("🕉️ Maa Durga Drawing (Matplotlib version)")

# Create figure
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-200, 200)
ax.set_ylim(-200, 300)
ax.set_aspect("equal")
ax.axis("off")

# --------------------
# Tika / Bindi
# --------------------
bindi = patches.Circle((0, 220), 40, color="red")
ax.add_patch(bindi)

# --------------------
# Eyes
# --------------------
# Left Eye
left_eye = patches.Circle((-80, 100), 50, color="black")
ax.add_patch(left_eye)
left_pupil = patches.Circle((-60, 120), 15, color="white")
ax.add_patch(left_pupil)

# Right Eye
right_eye = patches.Circle((80, 100), 50, color="black")
ax.add_patch(right_eye)
right_pupil = patches.Circle((60, 120), 15, color="white")
ax.add_patch(right_pupil)

# --------------------
# Eyebrows
# --------------------
left_brow = patches.Arc((-80, 160), 120, 40, angle=0, theta1=200, theta2=340, linewidth=6, color="black")
ax.add_patch(left_brow)
right_brow = patches.Arc((80, 160), 120, 40, angle=0, theta1=200, theta2=340, linewidth=6, color="black")
ax.add_patch(right_brow)

# --------------------
# Nose
# --------------------
nose = patches.Arc((0, 40), 40, 80, angle=0, theta1=200, theta2=340, linewidth=5, color="black")
ax.add_patch(nose)

# --------------------
# Lips
# --------------------
upper_lip = patches.Arc((0, -40), 120, 60, angle=0, theta1=0, theta2=180, linewidth=5, color="red")
ax.add_patch(upper_lip)
lower_lip = patches.Arc((0, -60), 120, 60, angle=0, theta1=180, theta2=360, linewidth=5, color="red")
ax.add_patch(lower_lip)

# --------------------
# Nose Ring
# --------------------
nosering = patches.Arc((40, 20), 150, 150, angle=0, theta1=200, theta2=360, linewidth=8, color="gold")
ax.add_patch(nosering)

# --------------------
# Crown (triangle)
# --------------------
crown = patches.RegularPolygon((0, 280), numVertices=3, radius=100, orientation=0, color="orange")
ax.add_patch(crown)

# Show in Streamlit
st.pyplot(fig)

