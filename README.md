# Uniswap v4 Documentation Bot

A Discord bot that helps users find information about Uniswap v4 by searching through documentation using embeddings and semantic search.

## Features

- `/ask` command to query Uniswap v4 documentation
- Semantic search using OpenAI embeddings
- Vector similarity search using Supabase pgvector
- Rich Discord embeds for formatted responses

## Prerequisites

- Python 3.8+
- Discord Bot Token
- OpenAI API Key
- Supabase Project with pgvector extension

## Setup

1. Clone the repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following variables:
```env
DISCORD_TOKEN="your_discord_bot_token"
OPEN_AI_API="your_openai_api_key"
SUPABASE_PROJECT_URL="your_supabase_project_url"
SUPABASE_SERVICE_ROLE="your_supabase_service_role_key"
```

4. Set up Supabase data (choose one option):

   Option A - Quick Setup:
   - Create a new Supabase project
   - Import `llm_docs_rows.csv` to create a table named `llm_docs`
   
   Option B - Generate Fresh Embeddings:
   - Use `llms.txt` to structure your documentation in the format: `[Title](URL): Description`
   - Generate embeddings and create `docs.json`:
     ```bash
     python utils/format_docs.py
     ```
   - Upload to Supabase:
     ```bash
     python supabase_utils/upload_embeddings.py
     ```

## Usage

1. Start the bot:
```bash
python -m bot.bot
```

2. In Discord, use the `/ask` command followed by your question:
```
/ask How does hook deployment work in Uniswap v4?
```

The bot will respond with the most relevant documentation, including:
- Topic title
- Description
- Link to full documentation

## Project Structure

- `bot/`
  - `bot.py` - Main bot initialization
  - `commands.py` - Discord command definitions
- `supabase_utils/`
  - `query_supabase.py` - Embedding and vector search functions
  - `upload_embeddings.py` - Documentation upload utility
- `utils/`
  - `format_docs.py` - Documentation formatting utilities
