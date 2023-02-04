import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("Christopher Thompson")
    content = """
    Hi, I'm Chris. I'm a multi-lingual IT-guy combining a lifelong love of learning with a severe and intractable case of Wanderlust. 
    I have a special interest in cloud technologies and IAAS. I enjoy tinkering with AWS, Azure, Terraform and Python.
    I'm originally from Ireland but moved to Texas recently to enjoy the cowboy lifestyle :)
    """
    st.write(content)


content2 = """
    Below you can find some of the apps I have built in Python. 
    Please feel free to contact me!
    """
st.write(content2)


