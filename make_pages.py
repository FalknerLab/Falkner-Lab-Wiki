import re


page_file = 'wiki_pages.txt'

with open(page_file) as f:
    lines = f.readlines()
    cur_cat = ''
    md_file_content = ''
    toc_num = 0
    last_level = 0
    for l in lines:
        re_match = re.search(r'\S', l)
        if re_match:
            txt = ''.join(l.split('.')[1:])[1:-1]
            level = re_match.start()
            if last_level == 3 and level == 3 or last_level == 3 and level == 0 or last_level == 6 and level == 3:
                with open(md_title, "w", encoding="utf-8") as md_file:
                    md_file.write(md_file_content)
                md_file_content = ''
            match level:
                case 0:
                    cur_cat = txt
                case 3:
                    md_file_content = f'---\ntitle: {txt}\ncategory: {cur_cat}\n---\n'
                    md_title = f'_docs/{'-'.join(txt.split('/'))}.md'
                case 6:
                    md_file_content += f'* [{txt}](#{'-'.join(txt.lower().split(' '))})\n'
            last_level = level