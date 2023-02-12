
#SOURCE: Andrew @ https://www.tweetspeakpoetry.com/2016/10/17/poetry-prompt-hidden-acrostic/

poem = """Beginning of the day, the sky
Each morning beams it brightest
Always with a hope that there may be
Ulterior to purpose, life to fill
The trees and boughs with birds
Illuminating with their colour
Fen, village, wood and rock
Under that bright sky, each
Leaving their life in land and loch."""

poem_lines = poem.splitlines()

result = ""

for i in range(len(poem_lines)):
    line = poem_lines[i]
    char = line[0]
    result += char
    #print(char)

print(result)




