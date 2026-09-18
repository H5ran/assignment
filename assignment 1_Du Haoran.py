#Name: [Du Haoran]
#Assignnemnt One
#ddl is 22/9/2026 23:59pm


import turtle

def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")
    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        print("Result:", num1 / num2)
    else:
        print("Invalid operation")

def QABot():
    print("Question Answering Bot")
    question = input("Ask me something: ")
    if question == "hello":
        print("Bot: Hello! Nice to meet you.")
    elif question == "python":
        print("Bot: Python is a language.")
    elif question == "jetson":
        print("Bot: Jetson Nano is an AI computer.")
    elif question == "ai":
        print("Bot: AI means Artificial Intelligence.")
    elif question == "name":
        print("Bot: My name is Python Bot.")
    else:
        print("Bot: Sorry, I don't understand.")

def turtledrawing():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    screen = turtle.Screen()
    screen.bgcolor("black")
    colors = ["red", "orange", "yellow", "green", 
              "cyan", "blue", "purple", "magenta"]
    size = 300          
    angle = 0           
    step = 0            
    
    while size > 5:     
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)   
        t.pendown()
        t.color(colors[step % len(colors)])
        t.width(2)

        for _ in range(4):
            t.forward(size)
            t.right(90)
        
        size -= 2        
        angle += 5      
        step += 1
    
    turtle.done()

def main():
    while True:
        print("choose function")
        print("1.calculator")
        print("2.QA Bot")
        print("3.turtle drawing")
        print("4.exit")

        choice = input()

        if choice == "1":
            calculator()
        elif choice == "2":
            QABot()
        elif choice == "3":
            turtledrawing()
        elif choice == "4":
            break
        else:
            print("invalid input, try again")

if __name__ == "__main__":
    main()