import segno

tag_PrusaMk3 = segno.make('URL to Prusa docs')
tag_PrusaMk3.save('./RawTags/tag_PrusaMk3.svg', scale=10)
tag_PrusaMk3.save('./RawTags/tag_PrusaMk3.png', scale=10)

with open('./QR_tags.md', 'w') as file:
    file.write('![Prusa_i3](./RawTags/tag_PrusaMk3.png)\n')
    file.write('# 3D Printer Docs\n\n')

