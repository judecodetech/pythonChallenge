garbage = open("question2.txt").read()

chars_in_garbage = ''.join(g for g in garbage if g.isalnum())

print chars_in_garbage
