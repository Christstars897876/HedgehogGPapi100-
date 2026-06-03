# API REST Flask & Script Client Node.js

Ce dépôt contient une API REST versionnée construite avec Flask (Python) et un script client d'exemple utilisant Axios (Node.js). Le projet est configuré pour être déployé nativement sur **Render** ou sur **Vercel**.

## Déploiement Direct

### Option A : Déploiement sur Render (Persistant)
Le dépôt inclut un fichier `render.yaml`. 
1. Connectez-vous sur votre tableau de bord **Render**.
2. Cliquez sur **New +** puis sélectionnez **Blueprint**.
3. Liez votre dépôt GitHub : Render lira le fichier de configuration et configurera l'API instantanément via `gunicorn`.

### Option B : Déploiement sur Vercel (Serverless)
Le dépôt inclut une directive `vercel.json` mappant Flask sur l'environnement `@vercel/python`.
1. Connectez votre repo sur le dashboard web de **Vercel** ou utilisez la commande globale `vercel`.
*Note : Étant donné que le système de fichiers Serverless de Vercel est éphémère et en lecture seule, la base SQLite locale sera effacée régulièrement. Pour de la vraie production, modifiez `app/database.py` pour pointer vers un service de base de données managé en ligne (ex: Supabase, Neon PostgreSQL).*

## Utilisation Locale

### Lancer l'API Flask (Serveur)
```bash
pip install -r requirements.txt
python run.py

