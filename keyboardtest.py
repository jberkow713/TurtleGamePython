# import keyboard  # using module keyboard

# while True:
#     try:
#         if keyboard.is_pressed('x'):
#             break  
# import turtle 
  
  
# sc = turtle.Screen() 
# sc.setup(400, 300) 
# turtle.textinput("title", "promt")
# Len_list = []
# Key_Dict = {0: [-312.0, 312.0], 1: [-156.0, 312.0], 2: [0.0, 312.0], 3: [156.0, 312.0], 4: [312.0, 312.0], 5: [-312.0, 156.0], 6: [-156.0, 156.0], 8: [156.0, 156.0], 9: [312.0, 156.0], 10: [-312.0, 0.0], 11: [-156.0, 0.0], 13: [156.0, 0.0], 14: [312.0, 0.0], 15: [-312.0, -156.0], 17: [0.0, -156.0], 18: [156.0, -156.0], 19: [312.0, -156.0], 20: [-312.0, -312.0], 21: [-156.0, -312.0], 22: [0.0, -312.0], 23: [156.0, -312.0], 24: [312.0, -312.0]}
# for key in Key_Dict.keys():
#     Len_list.append(key)

# print(len(Len_list))
val_list = []
A = {(0, 1, 2, 3, 4): 5, (5, 6, 7, 8, 9): 5, (10, 11, 12, 13, 14): 5, (15, 16, 17, 18, 19): 5, (20, 21, 22, 23, 24): 5, (0, 5, 10, 15, 20): 5, (1, 6, 11, 16, 21): 5, (2, 7, 12, 17, 22): 5, (3, 8, 13, 18, 23): 5, (4, 9, 14, 19, 24): 5, (0, 6, 12, 18, 24): 5, (20, 16, 12, 8, 4): 5}

for x in A.values():
    val_list.append(x)

print(val_list)    