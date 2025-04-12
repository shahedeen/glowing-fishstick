import os
from dotenv import load_dotenv
from supabase import create_client, Client
from datetime import datetime

# Load environment variables from .env
load_dotenv()

# Get Supabase credentials
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

# Debug print (optional)
print("Supabase URL:", supabase_url)
print("Supabase Key:", supabase_key[:5] + "..." if supabase_key else "None")

# Initialize Supabase client
supabase: Client = create_client(supabase_url, supabase_key)

# Function to insert weather data
def insert_weather_data(city, actual_temp, predicted_temp, humidity):
    data = {
        "city": city,
        "actual_temperature": actual_temp,
        "predicted_temperature": predicted_temp,
        "humidity": humidity,
        "timestamp": datetime.utcnow().isoformat()
    }

    try:
        response = supabase.table("weather_data").insert(data).execute()
        if hasattr(response, 'data'):
            print("✅ Data inserted successfully:", response.data)
        else:
            print("⚠️ Insert may have failed. Response:", response)
    except Exception as e:
        print("❌ Error inserting data:", e)

# Example usage
insert_weather_data("London", 15.5, 14.8, 80)










