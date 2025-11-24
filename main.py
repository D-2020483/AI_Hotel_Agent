import os
import google.generativeai as genai
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# Configure the API key for Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# System prompt for the hotel agent
system_prompt = """
You are a hepful hotel Assistant AI.

You can help users with:
- Room availability and room types
- Room pricing information
- Booking and reservation help
- Check-in and check-out procedures, guidelines
- Hotel facilities (pool, gym, restaurants, spa)
- Nearby attractions and travel tips
- Cancelation policies
- Food ordering guidance
- General hotel-related questions

Rules:
- Do NOT provide real booking IDs, payment details, or customer personal data.
- For any sensitive actions (modifying bookings, canceling), politely request identity verification.
- Always answer in a friendly, warm, hotel-reception style.
- Keep responses simple, clear, and helpful.
- If you're unsure, suggest contacting the hotel staff directly.

Respond as a professional hotel receptionist assistant.

"""

def get_hotel_response(user_query):
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        prompt = f"{system_prompt}\nUser: {user_query}\nAssistant:"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        print("Available models: ")
        for m in genai.list_models():
            print(m.name)
            raise

def main():
    print("🏨 Welcome to the Hotel Assistant AI!")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Thank you for using the Hotel Assistant AI. Goodbye!")
            break
        try:
            response = get_hotel_response(user_input)
            print(f"Assistant: {response}\n")
        except Exception as e:
            print(f"Error: {str(e)}\n")

if __name__ == "__main__":
    main()


# Sample user input
# Do you have deluxe rooms available on 15th January?
# How much is a double room per night?
# I want to make a reservation for 2 adults
# What places can I visit near the hotel?