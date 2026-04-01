import streamlit as st
import pandas as pd

# ── BLOC 1 : CONFIGURATION ───────────────────────────────────────────────────
st.set_page_config(page_title="Le Tribunal du Restaurant", page_icon="🏛️", layout="wide")
st.title("🏛️ Le Tribunal du Restaurant")
st.caption("La justice algorithmique pour régler vos comptes entre amis.")

# Liste étendue à 20 accusés (10 originaux + 10 nouveaux)
accusés = [
    'Qubit 🦊', 'Volt ⚡', 'Personne Salade 🥗', 'Négateur de Jus 🧃',
    'Oublieur de Portefeuille 🪙', 'Commandeur de Homard 🦞', 'Voleur de Frites 🍟',
    'Buveur de Vin 🍷', 'Double Dessert 🍰', 'Disparaisseur aux Toilettes 🚽',
    'Picoreur de Pain 🥖', 'Critique Gastronomique 🧐', 'Partageur de Plat 🤝',
    'Addict au Ketchup 🍅', 'Grand Soiffard 🍺', 'Calculeur de Centimes 🧮',
    'Allergique Imaginaire 🤧', 'Photographe de Plats 📸', 'Presse-Citron 🍋', 'Roi du Pourboire 💸'
]

# Initialisation du session state
if 'reçu' not in st.session_state:
    # Quelques données par défaut pour illustrer
    st.session_state.reçu = pd.DataFrame([
        {'article': 'Pizza Margherita 🍕',   'prix': 14.50, 'accusé': 'Qubit 🦊'},
        {'article': 'Salade Variée 🥗',      'prix': 12.00, 'accusé': 'Personne Salade 🥗'},
        {'article': 'Jus Premium 🧃',        'prix': 18.00, 'accusé': 'Négateur de Jus 🧃'},
        {'article': 'Homard Grillé 🦞',      'prix': 45.00, 'accusé': 'Commandeur de Homard 🦞'},
        {'article': 'Entrecôte 🥩',          'prix': 28.00, 'accusé': 'Critique Gastronomique 🧐'},
        {'article': 'Burger Géant 🍔',       'prix': 22.00, 'accusé': 'Grand Soiffard 🍺'},
    ])

# ── BLOC 2 : TABLE DES PREUVES INTERACTIVES ──────────────────────────────────
st.subheader("🗂️ Le Registre des Preuves")

df = st.data_editor(
    st.session_state.reçu,
    column_config={
        'article': st.column_config.TextColumn("Article Commandé"),
        'prix': st.column_config.NumberColumn(
            "Prix (DH)",
            format="%.2f DH",
            min_value=0
        ),
        'accusé': st.column_config.SelectboxColumn(
            "Coupable",
            options=accusés,
            required=True
        ),
    },
    num_rows="dynamic",
    use_container_width=True
)

# Sauvegarde immédiate
st.session_state.reçu = df

# ── RÉGLAGES FINAUX ──────────────────────────────────────────────────────────
col_a, col_b = st.columns([2, 1])
with col_a:
    taux_service = st.slider("🧾 Frais de service (%)", 0, 20, 10) / 100

# ── BLOCS 3 & 4 : LE VERDICT ────────────────────────────────────────────────
if st.button("⚡ RENDRE LE VERDICT", type="primary", use_container_width=True):
    if df.empty or df['prix'].sum() == 0:
        st.warning("⚠️ Le dossier est vide ! Ajoutez des articles et des prix.")
    else:
        st.divider()
        st.header("⚖️ Sentence du Tribunal")

        # Calcul des totaux par personne
        totaux = df.groupby('accusé')['prix'].sum().to_dict()
        
        # Gestion du cas spécial "Oublieur de Portefeuille"
        oublieur = 'Oublieur de Portefeuille 🪙'
        dette_oublieur = totaux.get(oublieur, 0)
        
        # Affichage en grille (4 colonnes pour 20 personnes)
        n_cols = 4
        rows = [accusés[i:i + n_cols] for i in range(0, len(accusés), n_cols)]
        
        for row in rows:
            cols = st.columns(n_cols)
            for idx, personne in enumerate(row):
                doit_initial = totaux.get(personne, 0)
                
                with cols[idx]:
                    if personne == oublieur and doit_initial > 0:
                        st.metric(label=personne, value="0.00 DH")
                        st.error("💸 Insolvable !")
                    else:
                        # Calcul final avec service
                        total_perso = doit_initial * (1 + taux_service)
                        
                        # Bonus : Si quelqu'un d'autre doit payer pour l'oublieur
                        if doit_initial > 0 and dette_oublieur > 0:
                            subvention = (dette_oublieur / (len(accusés) - 1)) * (1 + taux_service)
                            total_perso += subvention
                        
                        st.metric(label=personne, value=f"{total_perso:.2f} DH")

        # Résumé financier
        total_ht = df['prix'].sum()
        total_ttc = total_ht * (1 + taux_service)
        
        st.success(f"💰 **Total Général à payer : {total_ttc:.2f} DH** (Service inclus)")

        # ── EXPORTATION ──────────────────────────────────────────────────────
        lignes_txt = [f"{p}: {totaux.get(p, 0) * (1 + taux_service):.2f} DH" for p in accusés if totaux.get(p, 0) > 0]
        texte_export = "--- TRAITÉ DE PAIX DU TRIBUNAL ---\n\n" + "\n".join(lignes_txt)
        
        st.download_button(
            label="📥 Télécharger le Traité de Paix",
            data=texte_export,
            file_name="verdict_restaurant.txt",
            mime="text/plain"
        )