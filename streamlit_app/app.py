import streamlit as st
import numpy as np
import pickle

# Charger le modèle et le scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.set_page_config(page_title="Segmentation des Clients", page_icon="💎", layout="centered")

st.title("🛍️ Segmentation des Clients - KMeans")
st.markdown("Saisissez vos informations pour connaître votre profil client et votre cluster.")

# ---- Entrées utilisateur ----
gender = st.selectbox("Genre", ["Male", "Female"])
age = st.slider("Âge", 18, 70, 30)
income = st.slider("Revenu Annuel (k$)", 10, 150, 60)
spending_score = st.slider("Score de Dépense (1-100)", 1, 100, 50)

# Encodage du genre
gender_encoded = 1 if gender == "Female" else 0

# Préparation des données
X = np.array([[age, income, spending_score]])

# Normalisation
X_scaled = scaler.transform(X)

# Prédiction du cluster
cluster = model.predict(X_scaled)[0]

# ---- Descriptions des clusters ----
cluster_info = {
    0: "🟠 **Cluster 0 - Least Valuable** : faible revenu, faible score de dépense, âge moyen.",
    1: "🟡 **Cluster 1 - Targets** : revenu élevé, score de dépense faible, âge moyen.",
    2: "🟢 **Cluster 2 - Valuable** : revenu et dépenses modérés, clients jeunes.",
    3: "🔵 **Cluster 3 - Less Valuable** : revenu et dépenses modérés, âge élevé.",
    4: "🟣 **Cluster 4 - Most Valuable** : revenu et score de dépense élevés, jeunes clients.",
    5: "🔴 **Cluster 5 - Very Valuable** : score de dépense élevé mais faible revenu, jeunes clients."
}

# ---- Résultat ----
st.subheader("🎯 Résultat de la prédiction")
st.markdown(cluster_info.get(cluster, f"Cluster {cluster} (non défini)"))

st.write(f"*(Cluster numérique : {cluster})*")

# ---- Option d'explication ----
with st.expander("ℹ️ À propos de l'application"):
    st.write("""
    Cette application de **segmentation client** utilise un modèle **K-Means** 
    entraîné sur les données du *Mall Customer Segmentation Dataset*.
    
    Elle prédit à quel groupe (cluster) appartient un nouveau client 
    selon son **âge**, **revenu annuel**, **score de dépense** et **genre**.
    """)

st.caption("Développé avec ❤️ et Streamlit")
