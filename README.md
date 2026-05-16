# creative-automation-tool

# Creative Automation Tool

AI-powered creative automation backend built using Django REST Framework.
Django REST Framework-based creative automation system that generates bulk marketing creatives using dynamic image processing, authenticated APIs, and automated media workflows.

# Features
JWT Authentication
Protected REST APIs
Bulk Creative Generation
Image Upload & Processing
ZIP Export System
User-based Creative Dashboard
Multi-user Architecture
Media File Handling
API-based Backend Architecture

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
- JWT Authentication
-  SQLite
-  Postman


# Future Plans:-
React Frontend
Payment Gateway Integration
AI Caption Generation
AI Image Enhancements
Subscription System
Cloud Deployment

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
