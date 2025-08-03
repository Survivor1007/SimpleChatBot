# SimpleChatBot

# Simple Python Chatbot with GUI

A beginner-friendly chatbot with a graphical user interface (GUI) built using Python and the Tkinter library. This project is a great starting point for anyone looking to understand core programming concepts like Object-Oriented Programming (OOP), GUI development, and basic event handling.

The chatbot's "brain" is a simple dictionary of keywords and responses. It serves as a solid foundation for more complex conversational agents.

## Key Features

* **Graphical User Interface:** The chatbot interacts with the user through a clean and simple window.
* **Object-Oriented Design:** The entire application is encapsulated within a single `SimpleChatbot` class, demonstrating good programming practices for organization and reusability.
* **Keyword-Based Responses:** The bot provides pre-defined responses based on keywords it detects in the user's input.
* **Event Handling:** The application responds to user actions, such as clicking the "Send" button or pressing the `Enter` key.
* **Conversation History:** A scrollable text box keeps a record of the entire conversation.

## Technologies Used

* **Python 3.x:** The core programming language.
* **Tkinter:** Python's built-in standard GUI library.

## How to Run

### Prerequisites

You need to have Python 3.x installed on your system. Tkinter is included with a standard Python installation, so no further dependencies are required.



A window titled "Simple OOP Chatbot" will appear, and you can begin your conversation with the bot!

## Code Snippet

The core logic of the chatbot is handled by the `get_bot_response` method, which iterates through a dictionary to find a matching response.

```python
def get_bot_response(self, user_input):
    user_input_lower = user_input.lower()
    
    for keywords, response in self.response.items():
        if any(keyword in user_input_lower for keyword in keywords):
            return response
    
    return "Sorry, I didn't understand that. Can you please be more specific?"