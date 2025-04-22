from supabase import create_client, Client
import json
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_PROJECT_URL')
SUPABASE_KEY = os.getenv('SUPABASE_SERVICE_ROLE')

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

with open("utils/docs.json", "r") as f:
    docs = json.load(f)

for doc in docs:
    title = doc.get("title", "")
    url = doc.get("url", "")
    description = doc.get("description", "")
    embedding = doc.get("embedding", [])

    if not embedding:
        print(f"Skipping {title} due to missing embedding.")
        continue

    response = supabase.table("llm_docs").insert({
        "title": title,
        "url": url,
        "description": description,
        "embedding": embedding
    }).execute()
