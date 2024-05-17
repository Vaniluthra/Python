'''
Convert a given string with words separated by underscores into CamelCase format, where each word starts with a capital letter and all spaces and underscores are removed.
'''

test_str=input()
print("Original string: " + test_str)
res = test_str.replace("_", " ").title().replace(" ", "")
print("The String after changing case : " + str(res)) 
