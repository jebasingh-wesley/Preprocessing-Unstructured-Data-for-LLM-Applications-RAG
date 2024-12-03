from langchain.text_splitter import RecursiveCharacterTextSplitter

# Combine content under each title into a single string
combined_text = "\n\n".join([f"{item['title']}\n{item['content']}" for item in structured_data])

# Chunk the text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # Maximum chunk size
    chunk_overlap=200  # Overlap for context preservation
)
chunks = text_splitter.split_text(combined_text)

# Display the chunks
for idx, chunk in enumerate(chunks[:3]):  # Preview first 3 chunks
    print(f"Chunk {idx + 1}:\n{chunk}\n")


