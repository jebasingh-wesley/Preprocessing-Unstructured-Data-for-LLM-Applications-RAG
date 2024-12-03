import json

chunked_data = []
for idx, chunk in enumerate(chunks):
    chunked_data.append({
        "chunk_id": idx + 1,
        "text": chunk,
        "metadata": {
            "source_title": structured_data[idx // 10]["title"] if idx // 10 < len(structured_data) else None
        }
    })

# Display enriched chunks
# for data in chunked_data[:3]:  # Preview first 3 chunks
#     print(data)


# Display enriched chunks as JSON
print(json.dumps(chunked_data[:3], indent=7))  # Pretty print the first 3 chunks as JSON
