
with open('shakespeare.txt') as org, open('shakespeare_corrected.txt', 'r') as mod:
    rows = org.readlines()
    mod_rows = mod.read().split()

    corrected_text = []
    idx = 0

    for row in rows:
        row_length = len(row.split())

        if row.strip() == '':
            corrected_text.append('\n')
        else:
            line_words = mod_rows[idx:idx + row_length]
            idx += row_length

            corrected_line = ' '.join(line_words)
            corrected_text.append(corrected_line + '\n')

with open("paragraphed_version.txt", 'w') as prg:
    prg.writelines(corrected_text)
