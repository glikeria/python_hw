#I just needed to add something! Vivat modification!!!
print "**********"
print "this is test task for Git"
symbols = {}
string = 'Additional Resource Links Visit https://www.python.org/downloads/ to download the latest version of Python 2.x See Introduction to Python for information on how to introduce and use Python in your curriculum See the Python Basics Quick Reference for an overview of the basic features of Python Administrative Details Contact info For more info about Exploring Computational Thinking (ECT), visit the ECT website (g.co/exploringCT) Credits Developed by the Exploring Computational Thinking team at Google and reviewed by K-12 educators from around the world. Last updated on 01/15/2015 Copyright info Except as otherwise noted, the content of this document is licensed under the Creative Commons Attribution 4.0 International License, and code samples are licensed under the Apache 2.0 License.'
for symbol in string.lower():
    symbols[symbol] = symbols.get(symbol, 0) + 1

    # if symbol in symbols:
    #     symbols[symbol] = symbols[symbol] + 1
    # else:
    #     symbols[symbol] = 0 + 1

# def func(key):
#     return symbols[key]

for key in sorted(symbols, reverse=False, key=symbols.get):
    #if key in "abcdefgjhklmnoqrstuvwxyz":
    #if ord(key) in range(ord("a"), ord("z")+1):#"abcdefgjhklmnoqrstuvwxyz":
    if 'a' < key < 'z':
        print "%s -> %s" % (key, symbols[key])
