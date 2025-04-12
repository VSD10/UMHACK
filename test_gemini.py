import os
import sys
import time
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("🔄 Testing Gemini API connection...")

# Use the hardcoded API key
api_key = "AIzaSyCDjAEpNxUdaMof0AZFF_Ww8UFPOwYB2Y8"

if not api_key:
    print("⚠️ API key is missing")
    sys.exit(1)

# Configure the Gemini API
try:
    genai.configure(api_key=api_key)
except Exception as config_error:
    print(f"❌ Error configuring Gemini API: {config_error}")
    print("\nPlease check your API key format.")
    sys.exit(1)

# Test the API with a simple prompt
try:
    # Create a model
    model = genai.GenerativeModel('gemini-pro')
    
    print("🔄 Sending test request to Gemini API...")
    
    # Set a timeout for the request
    start_time = time.time()
    max_time = 15  # seconds
    
    # Generate a response with a simple prompt
    response = model.generate_content("Hello! Please respond with a single short sentence.")
    
    elapsed_time = time.time() - start_time
    
    # Print the response
    print(f"✅ Gemini API is working correctly! (Response time: {elapsed_time:.2f}s)")
    print("\nResponse from Gemini:")
    print("-" * 50)
    print(response.text)
    print("-" * 50)
    
    print("\nYou can now run your chatbot application with:")
    print("uvicorn app.main:app --reload")
    
except KeyboardInterrupt:
    print("\n⚠️ Test interrupted by user.")
    print("The API request was cancelled, but this doesn't necessarily mean there's a problem with the API.")
    print("You can still try running your application.")
    sys.exit(0)
    
except Exception as e:
    print(f"❌ Error testing Gemini API: {e}")
    print("\nPossible solutions:")
    print("1. Check your internet connection")
    print("2. Verify the API key is correct")
    print("3. The Gemini API service might be experiencing issues")
    print("\nYou can still try running your application, but the AI responses may fall back to templates.")