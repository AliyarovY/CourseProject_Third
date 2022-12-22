from classes import *
from utils import make_top_10
from v_vars import *
import json


def main():
    try:
        pages = int(input('Pages count = '))
    except:
        pages = 1
    try:
        per_page = int(input('Per page = '))
    except:
        per_page = 10
    file = input('File = ') or 'vacancies'
    text = input('Profession = ') or 'Python'

    for page in range(pages):
        try:
            with open(file, 'w', encoding='utf-8') as f_w:
                hh = HH(page, text, per_page).data
                sj = SJ(page, text, per_page).data
                json.dump(hh, f_w, indent=4, ensure_ascii=False)
                json.dump(sj, f_w, indent=4, ensure_ascii=False)
        except KeyError:
            print('pages ran out')
            break
    print('\n\nThe data was loaded into the file\n')

    is_top = input('to bring out the top 10 vacancies that do not require experience? [y/n] ')
    assert is_top in 'yn', 'Bad try'
    if is_top == 'y':
        for j in make_top_10(text):
            print()
            pprint(j, indent=4)
    else:
        exit()


if __name__ == '__main__':
    main()
