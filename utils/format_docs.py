import json
import re
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPEN_AI_API'))

def get_embedding(text):
    """Get embedding for a text using OpenAI's API"""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def parse_markdown_line(line):
    # Regular expression to match markdown links and text
    pattern = r'\[(.*?)\]\((.*?)\):(.*)'
    match = re.match(pattern, line.strip())
    
    if match:
        title = match.group(1)
        url = match.group(2)
        description = match.group(3).strip()

        full_text = f"{title}. {description}"
        embedding = get_embedding(full_text)
        
        return {
            "title": title,
            "url": url,
            "description": description,
            "embedding": embedding
        }
    return None

def convert_to_json():
    docs = []
    
    with open('llms.txt', 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('#'):
                line = line.strip().lstrip('- ')
                entry = parse_markdown_line(line)
                if entry:
                    docs.append(entry)
    
    # Write to JSON file
    with open('docs.json', 'w') as json_file:
        json.dump(docs, json_file, indent=2)
    
    print(f"Processed {len(docs)} documents with embeddings")

if __name__ == "__main__":
    convert_to_json()