import streamlit as st
from google.cloud import firestore

db = firestore.Client.from_service_account_json("firestore-key.json")

doc_ref = db.collection("posts").document("Google")

doc = doc_ref.get()


st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())