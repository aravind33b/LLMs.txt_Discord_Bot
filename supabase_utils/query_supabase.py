from supabase import create_client
import openai
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_PROJECT_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE")
OPENAI_API_KEY = os.getenv("OPEN_AI_API")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
openai.api_key = OPENAI_API_KEY

def embed_text(text: str) -> list:
    """Get OpenAI embedding for a given text."""
    response = openai.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    return response.data[0].embedding

def query_supabase(question: str):
    """Embed question, search Supabase, and return best match."""
    query_embedding = embed_text(question)

    # Perform a pgvector similarity search
    sql = f"""
        SELECT title, url, description, embedding <#> ARRAY{query_embedding} AS distance
        FROM llm_docs
        ORDER BY distance ASC
        LIMIT 1;
    """

    response = supabase.rpc("match_llm_docs", {
        "query_embedding": query_embedding
    }).execute()

    if response.data:
        best_match = response.data[0]
        return {
            "title": best_match["title"],
            "url": best_match["url"],
            "description": best_match["description"]
        }
    else:
        return None

if __name__ == "__main__":
    q = input("Ask a question: ")
    result = query_supabase(q)

    if result:
        print("\n Top Match Found:")
        print(f"Title: {result['title']}")
        print(f"URL:   {result['url']}")
        print(f"Desc:  {result['description']}")
    else:
        print("No match found")

