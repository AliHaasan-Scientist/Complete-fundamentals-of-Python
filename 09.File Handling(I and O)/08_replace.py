words = ["donkey", "basterd"]
with open('09.File Input & Output\censord.txt', 'r') as f:
    content = f.read()

for word in words:
    content = content.replace(word, "cendsord")
    with open('09.File Input & Output\censord.txt', 'w') as f:
        f.write(content)
