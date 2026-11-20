# Research Assistant

A command-line research assistant I built to ask questions about my own course notes and PDFs. It runs a LangChain agent on Gemini that has two tools:

- **search_knowledge_base**: searches the PDFs you've indexed into Pinecone
- **web_search**: searches Google through SerpAPI for anything that isn't in your documents

The agent checks your documents first, uses the web when it needs to, and lists the sources it used at the end of each answer.

## Requirements

- Python 3.13
- [pipenv](https://pipenv.pypa.io/)
- API keys for Gemini, Pinecone and SerpAPI (all three have free tiers)

## Setup

Clone the repo and install the dependencies:

```bash
git clone https://github.com/AbdulazizTajuMohammedyasin/research-assistant.git
cd research-assistant
pipenv install
```

Copy `.env.example` to `.env` and fill in your keys:

```bash
cp .env.example .env
```

In Pinecone, create an index with **dimension 384** and the **cosine** metric. The embeddings come from `sentence-transformers/all-MiniLM-L6-v2`, which runs locally and outputs 384-dimensional vectors. Put the index name in `PINECONE_INDEX_NAME`.

## Indexing your documents

Create a `knowledge_base` folder in the project root and put your PDFs in it. It's in `.gitignore`, so your files won't get committed.

Then run:

```bash
pipenv run python -m app.rag.index_documents
```

This splits the PDFs into chunks of about 1000 characters and uploads them to Pinecone. The first run takes a little longer because it downloads the embedding model.

Running it again uploads every file again, so you'll end up with duplicate chunks. If you add new PDFs, either clear the index first or index only the new files.

## Usage

```bash
pipenv run python -m app.main
```

Ask a question at the `You:` prompt and type `exit` to quit. The conversation history is kept for the session, so you can ask follow-up questions.

## Project structure

```
app/
├── main.py              # CLI chat loop
├── agent/agent.py       # agent setup and system prompt
├── chat/conversation.py # in-memory message history
├── llm/gemini.py        # Gemini model config
├── rag/
│   ├── ingestion.py       # load and chunk PDFs
│   ├── embeddings.py      # HuggingFace embeddings
│   ├── vector_store.py    # Pinecone connection
│   ├── retriever.py       # top-4 similarity search
│   ├── index_documents.py # indexing script
│   └── qa.py              # plain RAG Q&A without the agent
└── tools/
    ├── knowledge_base.py
    └── web_search.py
```

## Notes

- Only PDFs are supported right now.
- The model is set in `app/llm/gemini.py` if you want to switch to a different Gemini model.
