import json
from unstructured.partition.image import partition_image
from unstructured.staging.base import elements_to_json
from PIL import Image

# Step 1: Define the image path
image_path = "example_image.jpg"  # Replace with your image file path

# Step 2: Load and process the image
try:
    # Open the image
    with Image.open(image_path) as img:
        img.show()  # Optionally display the image
    
    # Extract elements from the image using `partition_image`
    elements = partition_image(filename=image_path)
    print(f"Extracted {len(elements)} elements from the image.")
    
    # Step 3: Convert extracted elements to JSON
    json_data = elements_to_json(elements)
    
    # Step 4: Save the JSON data to a file
    output_json_path = "output_data.json"
    with open(output_json_path, "w", encoding="utf-8") as json_file:
        json_file.write(json_data)
    
    print(f"Structured data has been saved to {output_json_path}")

except Exception as e:
    print(f"Error processing the image: {e}")
