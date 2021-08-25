import sys
import os
file = open(os.path.join(sys.path[0], "vocabulary.rtf"), 'w')
text = file.write(input())
print(text)
file.close()

file = open(os.path.join(sys.path[0], "vocabulary.rtf"), 'r')
text = file.read
print(text)
file.close