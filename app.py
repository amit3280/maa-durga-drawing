import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# -----------------------------
# Draw Maa Durga Face (simple version)
# -----------------------------
def draw_durga():
    fig, ax = plt.subplots(figsize=(6, 8))
    ax.set_xlim(-200, 200)
    ax.set_ylim(-200, 250)
    ax.set_aspect('equal')
    ax.axis("off")

    # Background
    ax.set_facecolor("gold")

    # Tika (red circle)
    tika = plt.Circle((0, 180), 40, color="red")
    ax.add_patch(tika)

    # Eyes
    right_eye = plt.Circle((70, 80), 40, color="black")
    left_eye = plt.Circle((-70, 80), 40, color="black")
    ax.add_patch(right_eye)
    ax.add_patch(left_eye)

    # Eye whites
    re_white = plt.Circle((85, 90), 12, color="white")
    le_white = plt.Circle((-85, 90), 12, color="white")
    ax.add_patch(re_white)
    ax.add_patch(le_white)

    # Nose
    nose = patches.Arc((0, 30), 40, 60, angle=0, theta1=200, theta2=340, color="black", lw=3)
    ax.add_patch(nose)

    # Lips (red oval)
    lips = plt.Circle((0, -40), 50, color="red")
    ax.add_patch(lips)

    # Nose ring
    nosering = patches.Arc((40, 20), 100, 100, angle=0, theta1=120, theta2=300, color="yellow", lw=5)
    ax.add_patch(nosering)

    return fig

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🕉️ Maa Durga Drawing (Matplotlib version)")

fig = draw_durga()
st.pyplot(fig)

