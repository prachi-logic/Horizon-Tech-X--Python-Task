def chatbot():
    print("Welcome to My Chatbox")
    name = input("Enter your name: ")
    print(f"Chatbox: Hello {name}! Welcome.")
    while True:
      user = input("You: ").lower()
      if user == "hello":
        print("Chatbox: Hey! Nice to meet you")

      elif user == "how are you":
        print("Chatbox: I am great")

      elif user == "who made you":
        print("Chatbox: Prachi created me using Python")

      elif user == "favourite colour":
        print("Chatbox: I like yellow colour")

      elif user =="how was your day":  
        print("Chatbox: My day was Amazing")
        
      elif user == "joke":
        print("Chatbox: Why do programmers prefer dark mode? Because light attracts bugs!")
    
      elif user == "add":
       a = int(input("First number: "))
       b = int(input("Second number: "))
       print("Chatbox: Result =", a + b)
       
      elif user == "bye":
       print("Chatbox: Bye! Have a nice day")
       break
    else:
        print("Chatbox: Sorry, I don't understand")
        
chatbot()

       