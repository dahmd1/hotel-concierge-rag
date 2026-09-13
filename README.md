# 🏨 hotel-concierge-rag

> ⚠️ Projet en cours de construction — ce README décrit l'état d'avancement actuel, pas le produit final.

Assistant conversationnel IA basé sur le RAG (Retrieval-Augmented Generation) pour répondre aux questions des clients d'un hôtel de Dubaï (DoubleTree by Hilton Dubai Al Jadaf) à partir de sa documentation officielle — sans jamais inventer d'informations non présentes dans les documents source.

Projet inspiré du notebook pédagogique "Projet 04" de Machine Learnia (https://github.com/MachineLearnia/Cahier-Vacances-2026), poussé vers des pratiques plus proches de la production :
- un modèle de génération plus robuste (Mistral en local, plutôt qu'un petit modèle de 0,5B de paramètres)
- une vraie étape de chunking (découpage avec chevauchement, via `langchain-text-splitters`)
- une couche d'évaluation quantitative (recall@k et autres métriques de retrieval/génération) (TO DO)
- une interface de chat Streamlit avec mémoire conversationnelle (TO DO)

## Stack technique

| Composant | Choix |
|---|---|
| Extraction PDF | `pypdf` |
| Chunking | `langchain-text-splitters` (RecursiveCharacterTextSplitter) |
| Embeddings | `sentence-transformers` (multilingue) — *à venir* |
| Base vectorielle | Chroma — *à venir* |
| Génération | Mistral (Hugging Face `transformers`, local) — *à venir* |
| Interface | Streamlit — *à venir* |
| Gestion de projet | `uv` |

## État d'avancement

- [x] **Ingestion** (`src/hotel_concierge_rag/ingest.py`) — extraction du texte des 11 pages du PDF hôtel via `pypdf`, avec un diagnostic de qualité par page (nombre de mots extraits) pour détecter les pages où l'information serait piégée dans une image plutôt que dans du texte réel.
- [x] **Chunking** (`src/hotel_concierge_rag/chunking.py`) — découpage du texte de chaque page en chunks de 500 caractères avec 100 caractères de chevauchement, via `RecursiveCharacterTextSplitter`. Découpage effectué page par page (pas sur le document entier concaténé), pour garder une métadonnée `page_number` fiable sur chaque chunk. 29 chunks obtenus à partir des 11 pages.
- [ ] Filtrage des chunks non-informatifs (pages de titre/couverture, texte décoratif)
- [ ] Embeddings + base vectorielle Chroma
- [ ] Génération avec Mistral en local
- [ ] Pipeline RAG complet (recherche + prompt + génération, avec citation des sources)
- [ ] Jeu de questions d'évaluation + métriques (recall@k, précision, fidélité de génération)
- [ ] Interface de chat Streamlit avec mémoire conversationnelle

## Limites connues (documentées, pas des bugs)

- **Extraction PDF imparfaite sur les pages à mise en page complexe** : sur certaines pages (colonnes, icônes, encadrés), `pypdf` ne restitue pas toujours l'ordre de lecture logique du contenu — des blocs d'information sans rapport peuvent se retrouver concaténés (ex : infos wifi et horaires de check-in/out sur la même page). Un mode d'extraction alternatif (`extraction_mode="layout"`) a été testé mais introduit trop de bruit (espaces/lignes vides) pour être retenu en l'état. Ce choix est assumé : le projet vise avant tout la maîtrise du pipeline RAG bout en bout, pas un parseur PDF parfait.


