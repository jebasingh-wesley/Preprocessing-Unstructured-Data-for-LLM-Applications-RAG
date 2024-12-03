from unstructured.partition.pdf import partition_pdf

# Load the PDF and extract elements
pdf_file = "/content/drive/MyDrive/Rag/Langchain_Project/required_pages.pdf"
elements = partition_pdf(filename=pdf_file)

# Process and structure the data
structured_data = []
current_title = "Untitled Section"  # Default for missing titles

for element in elements:
    # Dynamically identify the type of each element
    if hasattr(element, 'text'):  # Check if the element has text attribute
        if element.__class__.__name__ == "Title":
            # If the element is a Title, assign it to current_title
            current_title = element.text.strip()
        elif element.__class__.__name__ == "Text":
            # If the element is Text, append it to structured_data
            if element.text.strip():  # Skip empty text blocks
                structured_data.append({
                    "title": current_title,
                    "content": element.text.strip()
                })

# Display structured data
if structured_data:
    for item in structured_data[:5]:  # Preview the first 5 items
        print(f"Title: {item['title']}\nContent: {item['content']}\n")
else:
    print("No structured data found!")

