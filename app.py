import streamlit as st
from PIL import Image, ImageDraw, ImageOps

# Set page title and favicon.
st.set_page_config(
    page_title="Jingyi - World Is My Oyster", 
    page_icon="🔭")


image_path = 'assets/profilephoto.jpg'
image = Image.open(image_path)

# Profile picture
# Create a circular mask to apply to the image
mask = Image.new('L', image.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + image.size, fill=255)

# Apply the mask to the image
circular_image = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
circular_image.putalpha(mask)

# Display the circular image in Streamlit
st.image(circular_image, width=200)

# Title and name
st.title("Hello! I am Jingyi 👋")

# Personal Info
col1, space, col2 = st.columns([2, 0.5, 2])

with col1:
    st.header("From:")
    st.write("Xi'an, China🍜")

    st.header("Education:")
    st.write("🎓 Master of Landscape Architecture | Harvard University", "2020-2023")
    st.write("🌿 B.E. in Landscape Architecture | Chongqing University", "2015-2020")

with col2:
    st.header("Birthday:")
    st.write("11/11, 1997 🎂")

    st.header("Interests:")
    st.write("💻 Software Development (post-grad)")
    st.write("🚀 Product Design & Management")

# Hobbies
st.header("Hobbies:")
st.write("🚶 City/Park Walk, 🏊 Swimming, ✈️ Travel !!!, 📸 Photography")
st.write("🍳 Cooking (eating), 🎤 K-pop Girl Groups | Karaoke, 🎬 Movies, 💬 Talk")