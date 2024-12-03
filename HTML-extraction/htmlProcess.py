import os
import json
from unstructured.partition.html import partition_html
from unstructured.partition.pptx import partition_pptx
from unstructured.staging.base import elements_to_json

def process_html(file_path):
    """Process HTML file and extract structured elements."""
    elements = partition_html(filename=file_path)
    return elements

def process_pptx(file_path):
    """Process PPTX file and extract structured elements."""
    elements = partition_pptx(filename=file_path)
    return elements

def save_to_json(elements, output_path):
    """Save extracted elements to JSON format."""
    json_data = elements_to_json(elements)
    with open(output_path, "w", encoding="utf-8") as json_file:
        json_file.write(json_data)
    print(f"Data saved to {output_path}")

def main():
    # File paths
    files = [
        {"path": "example.html", "type": "html"},
        {"path": "example.pptx", "type": "pptx"}
    ]
    
    for file_info in files:
        file_path = file_info["path"]
        file_type = file_info["type"]
        
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
        
        print(f"Processing {file_path} as {file_type.upper()}...")
        
        try:
            if file_type == "html":
                elements = process_html(file_path)
            elif file_type == "pptx":
                elements = process_pptx(file_path)
            else:
                print(f"Unsupported file type: {file_type}")
                continue
            
            # Save the output
            output_path = f"{os.path.splitext(file_path)[0]}_output.json"
            save_to_json(elements, output_path)
        
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    main()
