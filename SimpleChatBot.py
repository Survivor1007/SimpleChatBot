import tkinter as tk
from tkinter import scrolledtext

class SimpleChatbot:
      """
      A simple chatbot with a GUI using tkinter andd OOP principles.
      """
      def __init__(self,master):

            self.master = master
            master.title("Simple OOP chatbot")
            master.geometry("400x500")

            self.response = {
                  ("hello", "hi", "greetings"): "Hello there! How can I help you today?",
            ("how are you", "how's it going"): "I'm a computer program, so I'm always doing great! Thanks for asking.",
            ("your name", "what is your name"): "You can call me Bot. What's your name?",
            ("bye", "goodbye", "see you"): "Goodbye! Have a great day.",
            ("help",): "I can answer basic questions. Try asking me about my name or how I am.",
            ("favorite color", "colour"): "I don't have a favorite color, but I do like the color of binary code!",
            ("weather",): "I don't have access to real-time weather data, sorry!",
            }

            self.chat_box = scrolledtext.ScrolledText(master, state = tk.DISABLED, wrap = tk.WORD, bg= "#f0f0f0")
            self.chat_box.pack(padx = 10, pady = 10 , fill = tk.BOTH, expand = True)

            self.input_frame = tk.Frame(master)
            self.input_frame.pack(padx= 10, pady = (0, 10), fill = tk.X)

            self.entry = tk.Entry(self.input_frame, bd= 2)
            self.entry.pack(side = tk.LEFT, fill = tk.X, expand = True, padx = ( 0, 5))

            self.button = tk.Button(self.input_frame, text = "SEND", command=self.send_message)
            self.button.pack(side = tk.RIGHT)

            #Bind the Enter key with the send message function
            master.bind('<Return>', self.send_message)

      def get_bot_response(self,user_input):
            user_input_lower = user_input.lower()

            for keywords, response in self.response.items():
                  if any(keyword in user_input_lower for keyword in keywords):
                        return response
            return "ERROR...I couldn't understand you .Can you be more specific ?"
      
      def send_message(self, event = None):
            user_input  = self.entry.get()
            if user_input.strip() == "":
                  return 

            self.chat_box.config(state = tk.NORMAL)
            self.chat_box.insert(tk.END, "You:" + user_input +"\n")
            self.chat_box.config(state = tk.DISABLED)
            self.entry.delete(0, tk.END)

            bot_response = self.get_bot_response(user_input)
            self.chat_box.config(state = tk.NORMAL)
            self.chat_box.insert(tk.END, "Bot:" + bot_response +"\n")
            self.chat_box.config(state = tk.DISABLED)
            self.chat_box.yview(tk.END)




if __name__ == "__main__":
      root = tk.Tk();
      my_chatbot = SimpleChatbot(root)
      root.mainloop()