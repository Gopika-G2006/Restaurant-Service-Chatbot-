import tkinter as tk
app = tk.Tk()
app.title("Restaurant Chatbot")
app.geometry("600x700")
bot_rules ={
    "Hi": "Welcome to our restaurant! How can I assist you today?",
    "Menu": "We serve Fried Chicken,Pizza,Pasta,Shakes,Mojito and desserts.",
    "Timing": "We're open from 9AM to 11 PM, all days of the week.",
    "Home delivery available": "Yes, we deliver through Zomato and Swiggy.",
    "Any discount": "Yes,We have 20 percent discount above 999 orders!",
    "Accepted payment methods": " We accept cash/Gpay/Paytm/COD",
    "Bye": "Thank you for visiting! Have a great day!",
}                               
def send_message():
    user_input = entry.get().strip().capitalize()  
    print(f"User input: '{user_input}'")  
    response = bot_rules.get(user_input.capitalize(), "I'm sorry, I didn't understand that.")
    print(f"Bot response: '{response}'")
    chatbox.insert("end", f"Bot: {response}\n\n")
    entry.delete(0, "end")
    chatbox.yview_moveto(1.0)  
chatbox = tk.Text(app, width=60, height=20, state="disabled", font=("Arial", 12))
chatbox.pack(pady=10, padx=10)
entry_frame = tk.Frame(app)
entry_frame.pack(pady=10)
entry = tk.Entry(entry_frame, width=40, font=("Arial", 12))
entry.pack(side="left", padx=5)
send_button = tk.Button(entry_frame, text="Send", command=send_message)
send_button.pack(side="left")
app.mainloop()import tkinter as tk
app = tk.Tk()
app.title("Restaurant Chatbot")
app.geometry("600x700")
bot_rules ={
    "Hi": "Welcome to our restaurant! How can I assist you today?",
    "Menu": "We serve Fried Chicken,Pizza,Pasta,Shakes,Mojito and desserts.",
    "Timing": "We're open from 9AM to 11 PM, all days of the week.",
    "Home delivery available": "Yes, we deliver through Zomato and Swiggy.",
    "Any discount": "Yes,We have 20 percent discount above 999 orders!",
    "Accepted payment methods": " We accept cash/Gpay/Paytm/COD",
    "Bye": "Thank you for visiting! Have a great day!",
}                               
def send_message():
    user_input = entry.get().strip().capitalize()  
    print(f"User input: '{user_input}'")  
    response = bot_rules.get(user_input.capitalize(), "I'm sorry, I didn't understand that.")
    print(f"Bot response: '{response}'")
    chatbox.insert("end", f"Bot: {response}\n\n")
    entry.delete(0, "end")
    chatbox.yview_moveto(1.0)  
chatbox = tk.Text(app, width=60, height=20, state="disabled", font=("Arial", 12))
chatbox.pack(pady=10, padx=10)
entry_frame = tk.Frame(app)
entry_frame.pack(pady=10)
entry = tk.Entry(entry_frame, width=40, font=("Arial", 12))
entry.pack(side="left", padx=5)
send_button = tk.Button(entry_frame, text="Send", command=send_message)
send_button.pack(side="left")
app.mainloop()
