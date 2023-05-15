import streamlit as st
from google.cloud import firestore


# qui ci stiamo autenticando a Firestore con la chiave json scaricata e inserita nel progetto
db = firestore.Client.from_service_account_json("firestore-key.json")

# qui stiamo mettendo nel codice un riferimento al document presente in firestore, questo riferimento non contiene i dati
# ma è puramente un riferimento ai dati
doc_ref = db.collection("posts").document("Google")

# per accedere ai dati usiamo .get()
doc = doc_ref.get()


# stampiamo a video il contenuto del db
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())


# qui stiamo creando il riferimento ad un nuovo "post" che sarà Apple
doc_ref_apple = db.collection("posts").document("Apple")

doc_ref_apple.set({
    "title": "Apple",
    "url": "www.apple.com"
})

posts_ref = db.collection("posts")

for doc in posts_ref.stream():
    st.write("the id is: ", doc.id)
    st.write("the contents are:", doc.to_dict())