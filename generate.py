with open("example.xml", "w") as f:
    f.write("<foo>")
    for x in range(800_000):
        f.write(f'<muntagi id="{x}" a="{(x * 331) % 96452}" />')
    f.write("</foo>")
