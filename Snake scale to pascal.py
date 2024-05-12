test_str=input()
print("Original string: " + test_str)
res = test_str.replace("_", " ").title().replace(" ", "")
print("The String after changing case : " + str(res)) 
