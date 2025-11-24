# 🏨 Hotel AI Assistant

A **Hotel AI Assistant** built using **Google Gemini API**, **Python**, and **Gradio**, deployed on **Hugging Face Spaces**.  
This AI assistant can help guests with room bookings, pricing, check-in/check-out info, hotel facilities, nearby attractions, and more.

---

## 🌟 Features

- ✅ Room availability information  
- ✅ Room pricing details  
- ✅ Booking and reservation guidance  
- ✅ Check-in and check-out instructions  
- ✅ Hotel facilities (pool, gym, restaurant, spa)  
- ✅ Nearby attractions and travel tips  
- ✅ Cancelation policies  
- ✅ Friendly and professional assistant style  
- ✅ Custom UI with a blue input textbox  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **AI Model:** Google Gemini 2.5 Flash  
- **Libraries:** `google-generativeai`, `gradio`, `python-dotenv`  
- **Deployment:** Hugging Face Spaces  
- **Interface:** Gradio interface shows 

---

## 💡 How It Works

1. **System Prompt:** Defines the assistant's behavior, personality, and rules (e.g., no sensitive data).  
2. **User Query:** Users type a question in the chat interface.  
3. **Gemini API:** The system prompt + user query is sent to the Gemini model for response generation.  
4. **Response Display:** Gradio interface shows the AI's response to the user.  

---

## 🔧 Installation (For Local Testing)

1. Clone the repository:
   ```bash
   git clone https://github.com/D-2020483/AI_Hotel_Agent
   cd hotel-ai-agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

4. Run the app:
   ```bash
   python app.py
   ```

---

## 🚀 Deployment

- The app is deployed on **Hugging Face Spaces**.
- Hugging Face automatically builds and hosts the app.  
- API key is stored securely using **Hugging Face Secrets**.  
- Users can access the AI Assistant online through a web browser.
- [Hugging Face Deployment Link](https://huggingface.co/spaces/Imalsha24/hotel-ai-agent).

---

## 🎨 Customization

- UI colors, input box, and chat styling can be customized via CSS.  
- Additional features like booking database integration, voice input/output, multi-language support can be added.  

---

## 📸 Screenshot

<img width="1898" height="867" alt="Ai" src="https://github.com/user-attachments/assets/ac17423f-538c-4f69-9831-d049968a67bb" />


---

## 📌 Example Questions

- "Do you have deluxe rooms available?"  
- "What is the price for a double room?"  
- "What time is checkout?"  
- "What tourist places can I visit near the hotel?"  

---

## 📄 License

This project is **MIT Licensed** – free to use and modify.


