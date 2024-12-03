from unstructured.partition.pdf import partition_pdf
import nltk
nltk.download('all')

pdf_file = "/content/drive/MyDrive/Rag/Langchain_Project/required_pages.pdf"

# Sample usage
elements = partition_pdf(filename=pdf_file)

# for element in elements[:10]:  # Preview first 10 elements
#     print(f"Element Type: {type(element).__name__}")
#     if hasattr(element, "text"):  # Check if the element has a text attribute
#         print(f"Content: {element.text}")
#     else:
#         print("Content: Not a text element")
