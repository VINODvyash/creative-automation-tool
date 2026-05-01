# creative-automation-tool

# Creative Automation Tool

This project is a simple Django-based API that helps generate marketing creatives automatically. Instead of manually designing each image, you can upload a background and a logo, and the system will create multiple creatives by combining them with different panels.

## What this project does

- Takes a background image and logo as input  
- Adds the logo to the image (top-right position)  
- Applies different panels (like dealership banners) at the bottom  
- Generates multiple creative images in one go  
- Provides an option to download all generated images as a ZIP file  

The main idea was to automate repetitive creative design tasks.

## Tech Stack

- Python  
- Django  
- Django REST Framework  
- Pillow (for image processing)  

## API Endpoint

**POST** `/api/generate/`

### Request (form-data)
- `background` → background image file  
- `logo` → logo image file  

### Response
- List of generated image URLs  
- ZIP file link containing all creatives  

## How to run the project

1. Clone the repository  
2. Install dependencies:


PIP install - r requirements.txt
3. Run the server:

python manage.py runserver

4. Use Postman or any API tool to test the endpoint  

## Output

- Generated images are stored in the `media/outputs/` folder  
- A ZIP file is also created for easy download  

## Author

Vinod Vyash
