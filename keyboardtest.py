# import keyboard  # using module keyboard

# while True:
#     try:
#         if keyboard.is_pressed('x'):
#             break  
# import turtle 
  
  
# sc = turtle.Screen() 
# sc.setup(400, 300) 
# turtle.textinput("title", "promt")
Len_list = []
Key_Dict = {0: [-312.0, 312.0], 1: [-156.0, 312.0], 2: [0.0, 312.0], 3: [156.0, 312.0], 4: [312.0, 312.0], 5: [-312.0, 156.0], 6: [-156.0, 156.0], 8: [156.0, 156.0], 9: [312.0, 156.0], 10: [-312.0, 0.0], 11: [-156.0, 0.0], 13: [156.0, 0.0], 14: [312.0, 0.0], 15: [-312.0, -156.0], 17: [0.0, -156.0], 18: [156.0, -156.0], 19: [312.0, -156.0], 20: [-312.0, -312.0], 21: [-156.0, -312.0], 22: [0.0, -312.0], 23: [156.0, -312.0], 24: [312.0, -312.0]}
for key in Key_Dict.keys():
    Len_list.append(key)

print(len(Len_list))