import pywhatkit as pk 
txt = """Text-based coding is the process of writing instructions in a programming language using text characters. This involves using a specific syntax (rules and structure) of the chosen language to communicate with a computer. It's the method used by professional programmers 
and follows a different approach than block-based coding, which relies on visual"""
pk.text_to_handwriting(txt,"demo.png",[0,0,138])
print("finsihed home work")
