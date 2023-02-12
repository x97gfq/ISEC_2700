
#SOURCE: Edgar Allan Poe @ https://www.tweetspeakpoetry.com/2016/10/17/poetry-prompt-hidden-acrostic/

poem = """For her this rhyme is penned, whose luminous eyes,
Brightly expressive as the twins of Leda,
Shall find her own sweet name, that nestling lies
Upon the page, enwrapped from every reader.
Search narrowly the lines!- they hold a treasure
Divine- a talisman- an amulet
That must be worn at heart. Search well the measure-
The words- the syllables! Do not forget
The trivialest point, or you may lose your labor
And yet there is in this no Gordian knot
Which one might not undo without a sabre,
If one could merely comprehend the plot.
Enwritten upon the leaf where now are peering
Eyes scintillating soul, there lie perdus
Three eloquent words oft uttered in the hearing
Of poets, by poets- as the name is a poet’s, too,
Its letters, although naturally lying
Like the knight Pinto- Mendez Ferdinando-
Still form a synonym for Truth- Cease trying!
You will not read the riddle, though you do the best you can do."""

poem_lines = poem.splitlines()

result = ""

for i in range(len(poem_lines)):
    line = poem_lines[i].replace(" ", "").replace(",", "").replace("-", "")
    char = line[i]
    result += char
    #print("line", line)
    #print("index", i)
    #print(".... char:", char)

print(result)




