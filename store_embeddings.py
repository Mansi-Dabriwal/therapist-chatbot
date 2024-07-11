import pinecone

# Initialize Pinecone
pinecone.init(api_key='#enter-your-key')
index = pinecone.Index("therapy-conversations")

# Store embeddings in Pinecone
for i, row in df_conversations.iterrows():
    index.upsert([(f'conversation_{i}', row['embedding'])])

# Save IDs and texts for later use
id_text_map = {f'conversation_{i}': row['conversation'] for i, row in df_conversations.iterrows()}
