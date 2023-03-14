import segno

tag_PrusaMk3 = segno.make('https://github.com/FRC-Team8744/Workshop_Docs/blob/main/Prusa_i3_MK3S/Prusa_i3_MK3S.md')
tag_PrusaMk3.save('./RawTags/tag_PrusaMk3.svg', scale=5)
tag_PrusaMk3.save('./RawTags/tag_PrusaMk3.png', scale=5)

with open('./QR_tags.md', 'w') as file:
    file.write('![Prusa_i3](./RawTags/tag_PrusaMk3.png)\n')
    file.write('# 3D Printer Docs\n\n')

# with open('./QR_tags.rst', 'w') as file:
#     file.write('3D Printer Docs\n')
#     file.write('######\n\n')
#     file.write('.. image:: ./RawTags/tag_PrusaMk3.png\n')
#     file.write('  :width: 400\n')
#     file.write('  :alt: Alternative text\n\n')
