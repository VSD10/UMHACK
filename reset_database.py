"""
Reset Database Script

This script clears all collections in the MongoDB database,
allowing you to reload all data on the next application startup.
"""

import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB connection string from environment variables
mongo_uri = os.getenv("MONGO_URI")
if not mongo_uri:
    print("❌ Error: MONGO_URI environment variable not found in .env file")
    exit(1)

async def reset_database():
    print("🔄 Connecting to MongoDB...")
    client = AsyncIOMotorClient(mongo_uri)
    db = client.get_database("merchant_chatbot")
    
    # Get list of collections
    collections = await db.list_collection_names()
    
    if not collections:
        print("ℹ️ Database is already empty.")
        return
    
    print(f"📊 Found {len(collections)} collections: {', '.join(collections)}")
    print("⚠️ WARNING: This will delete all data in these collections!")
    
    # Ask for confirmation
    confirm = input("Are you sure you want to proceed? (yes/no): ")
    if confirm.lower() != "yes":
        print("❌ Operation cancelled.")
        return
    
    # Drop each collection
    for collection in collections:
        print(f"🗑️ Dropping collection: {collection}...")
        await db.drop_collection(collection)
    
    print("✅ All collections have been dropped successfully.")
    print("ℹ️ The next time you start the application, it will reload all data from CSV files.")

if __name__ == "__main__":
    asyncio.run(reset_database())