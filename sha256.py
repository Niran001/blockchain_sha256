import streamlit as st
import hashlib

def hash_cal(input_string):
    # Create the Hash object to the data
    sha256_hash = hashlib.sha256()

    # I need to update the Hash with the data

    sha256_hash.update(input_string.encode())

    # Get the hexa value
    hash_data = sha256_hash.hexdigest()

    st.write("SHA256 - Hash Value : ", hash_data)

#display to the front end Web GUI


st.title("SHA 256")

st.text("Convert My String data to HASH code !!")
text = st.text_area(" ")
st.button("Convert",on_click=hash_cal(text))

st.balloons()


print("My Hashlib code successful")