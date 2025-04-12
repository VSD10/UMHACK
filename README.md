# Merchant Chatbot

A chatbot application that analyzes data from MongoDB and uses AI to respond to user queries about merchants, menu items, and orders.

## Features

- Natural language processing to understand user intent
- Integration with MongoDB for data retrieval
- AI-powered responses (with fallback to template-based responses)
- Simple web interface for testing

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with the following variables:
   ```
   MONGO_URI=your_mongodb_connection_string
   GEMINI_API_KEY=your_gemini_api_key  # Get from https://makersuite.google.com/app/apikey
   ```
4. Clone with Git LFS:
   
   This repository uses Git Large File Storage (Git LFS) to handle large data files. To properly clone the repository with all data files:
   
   ```
   # Install Git LFS if you haven't already
   # Windows: Download from https://git-lfs.github.com/
   # Mac: brew install git-lfs
   # Linux: apt-get install git-lfs
   
   # Initialize Git LFS
   git lfs install
   
   # Clone the repository (if you haven't already)
   git clone https://github.com/YourUsername/merchant_chatbot.git
   
   # If you've already cloned without Git LFS, pull the LFS files
   git lfs pull
   ```
   
   Note: The large transaction data files are stored using Git LFS to comply with GitHub's file size limits.

5. Run the application:
   ```
   uvicorn app.main:app --reload
   ```
6. Open your browser and navigate to `http://localhost:8000`

## API Endpoints

- `GET /`: Redirects to the chatbot web interface
- `GET /api`: Returns API information
- `POST /api/chat`: Processes a chat request and returns a response
  - Request body: `{"query": "your question here"}`
  - Response: `{"query": "your question", "intent": {"view": 0.5, "menu": 0.5, "checkout": 0.0, "order": 0.0}, "response": "AI-generated response"}`

## Data Structure

The application uses the following MongoDB collections:
- `merchants`: Information about food vendors
- `items`: Menu items with prices and cuisine tags
- `transactions`: Order details and delivery information
- `transaction_items`: Links between orders and items
- `keywords`: Natural language processing keywords for intent detection

## Development

- The main application is defined in `app/main.py`
- API endpoints are in the `app/api` directory
- Services (including the chatbot logic) are in the `app/services` directory
- Database models are in the `app/models` directory
- Database connection is configured in `app/db/mongo.py`
- CSV data loading utilities are in `app/utils/csv_loader.py`

## Customization

- To use a different AI service, modify the `_generate_ai_response` method in `app/services/chatbot_service.py`
- To add more intent categories, update the `_analyze_intent` method and the keyword structure
- To change the response templates, modify the `_generate_template_response` method