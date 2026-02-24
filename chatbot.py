import tkinter as tk
from tkinter import scrolledtext, messagebox
import random
import re

class RuleBasedChatbot:
    def __init__(self):
        # Define chatbot rules with patterns and responses
        self.rules = {
            r'hello|hi|hey': [
                "Hello! How can I help you today?",
                "Hi there! What would you like to talk about?",
                "Hey! I'm here to assist you."
            ],
            r'how are you|how do you do': [
                "I'm doing great, thank you for asking!",
                "I'm functioning perfectly and ready to help!",
                "I'm just a chatbot, but I'm here to assist you!"
            ],
            r'what is your name|who are you': [
                "I'm a rule-based chatbot created to assist you.",
                "I'm your friendly chatbot assistant!",
                "You can call me ChatBot!"
            ],
            r'weather': [
                "I don't have real-time weather data, but I hope it's nice where you are!",
                "Check your local weather app for accurate information.",
                "I'm not connected to the internet, so I can't check the weather for you."
            ],
            r'thank you|thanks': [
                "You're welcome!",
                "Happy to help!",
                "Anytime! Is there anything else I can assist with?"
            ],
            r'bye|goodbye|see you': [
                "Goodbye! Have a great day!",
                "See you later! Take care!",
                "Bye! Come back anytime you need assistance."
            ],
            r'help': [
                "I can help with various topics. Try asking about: "
                "greetings, weather, or just say hello!",
                "I'm here to assist. What would you like to know?",
                "You can ask me general questions or just chat with me!"
            ],
            r'time': [
                "I don't have access to real-time clock, but you can check your device's time.",
                "Time flies when you're chatting with me!"
            ],
            r'joke': [
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "What do you call a computer that sings? A-Dell!",
                "Why did the AI go to therapy? Too many deep learning issues!"
            ],
            r'python': [
                "Python is a versatile programming language great for beginners and experts alike.",
                "Python is known for its simplicity and readability.",
                "I was created using Python and Tkinter!"
            ],
            r'favorite color|colors': [
                "As a chatbot, I don't have personal preferences, but blue is a popular color!",
                "I think all colors are beautiful in their own way!",
                "I'm partial to digital colors like #00FF00 (bright green)!"
            ],
            r'sad|depressed|unhappy': [
                "I'm sorry to hear that. Remember, it's okay to feel down sometimes.",
                "I hope things get better for you. Would you like to talk about it?",
                "Sometimes a chat with a friendly bot can help brighten the day!"
            ],
            r'happy|excited|great': [
                "That's wonderful to hear!",
                "I'm glad you're feeling good!",
                "Positivity is contagious! Thanks for sharing your happiness!"
            ]
        }
        
        # Default responses for unmatched patterns
        self.default_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "That's interesting! Tell me more.",
            "I don't have a specific response for that, but I'm learning!",
            "Could you ask me something else?",
            "I'm still learning and improving. Thanks for your patience!"
        ]
    
    def get_response(self, user_input):
        """Process user input and return appropriate response"""
        user_input = user_input.lower().strip()
        
        # Check against all patterns
        for pattern, responses in self.rules.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
        
        # Return default response if no pattern matches
        return random.choice(self.default_responses)

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rule-Based Chatbot")
        self.root.geometry("500x600")
        self.root.resizable(True, True)
        
        # Initialize chatbot
        self.chatbot = RuleBasedChatbot()
        
        # Create GUI components
        self.create_widgets()
        
    def create_widgets(self):
        """Create and arrange all GUI components"""
        
        # Title label
        title_label = tk.Label(
            self.root, 
            text="🤖 Rule-Based Chatbot", 
            font=("Arial", 16, "bold"),
            bg="#4CAF50",
            fg="white",
            pady=10
        )
        title_label.pack(fill=tk.X)
        
        # Chat display area
        self.chat_display = scrolledtext.ScrolledText(
            self.root, 
            wrap=tk.WORD, 
            font=("Arial", 11),
            bg="#f5f5f5",
            state='disabled'
        )
        self.chat_display.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg="#e0e0e0")
        input_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # User input field
        self.user_input = tk.Entry(
            input_frame, 
            font=("Arial", 12),
            fg="#333",
            bg="white"
        )
        self.user_input.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
        self.user_input.bind('<Return>', self.send_message)
        
        # Send button
        send_button = tk.Button(
            input_frame, 
            text="Send", 
            command=self.send_message,
            font=("Arial", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            padx=15
        )
        send_button.pack(side=tk.RIGHT)
        
        # Clear button
        clear_button = tk.Button(
            self.root, 
            text="Clear Chat", 
            command=self.clear_chat,
            font=("Arial", 10),
            bg="#f44336",
            fg="white",
            activebackground="#da190b",
            padx=10
        )
        clear_button.pack(pady=5)
        
        # Display welcome message
        self.display_message("ChatBot", "Hello! I'm your rule-based chatbot. How can I help you today?")
    
    def send_message(self, event=None):
        """Handle sending user message and getting bot response"""
        user_text = self.user_input.get().strip()
        
        if user_text:
            # Display user message
            self.display_message("You", user_text)
            
            # Get and display bot response
            bot_response = self.chatbot.get_response(user_text)
            self.display_message("ChatBot", bot_response)
            
            # Clear input field
            self.user_input.delete(0, tk.END)
    
    def display_message(self, sender, message):
        """Display a message in the chat area"""
        self.chat_display.config(state='normal')
        
        # Add sender name with formatting
        if sender == "You":
            self.chat_display.insert(tk.END, f"\n{sender}: ", "user")
            self.chat_display.tag_config("user", foreground="blue", font=("Arial", 11, "bold"))
        else:
            self.chat_display.insert(tk.END, f"\n{sender}: ", "bot")
            self.chat_display.tag_config("bot", foreground="green", font=("Arial", 11, "bold"))
        
        # Add message content
        self.chat_display.insert(tk.END, message)
        
        # Scroll to bottom
        self.chat_display.see(tk.END)
        self.chat_display.config(state='disabled')
    
    def clear_chat(self):
        """Clear all chat messages"""
        self.chat_display.config(state='normal')
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state='disabled')
        
        # Display welcome message again
        self.display_message("ChatBot", "Chat cleared! How can I help you today?")

def main():
    """Main function to run the chatbot application"""
    root = tk.Tk()
    
    # Set application icon (optional)
    # root.iconbitmap('chatbot_icon.ico')
    
    # Create and run the chatbot GUI
    app = ChatbotGUI(root)
    
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()