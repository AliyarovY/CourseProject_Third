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
    file = 'vacancies'
    text = input('Profession = ') or 'Python'

    # cache work
    begin = 0
    with open('cache_record') as cache_r:
        v_count = pages * per_page
        ch = json.load(cache_r)
        if text in ch:
            begin = v_count // per_page - ch[text] // per_page
            if begin < 0:
                begin = pages
            ch[text] = v_count
        else:
            ch[text] = v_count
    with open('cache_record', 'w') as cache_w:
        json.dump(ch, cache_w, indent=4)


    for page in range(begin, pages):
        try:
            with open(file, 'r', encoding='utf-8') as f_r:
                nn = json.load(f_r)
            with open(file, 'w', encoding='utf-8') as f_w:
                hh = HH(page, text, per_page).data
                sj = SJ(page, text, per_page).data
                res_dmp = sj + hh + nn
                json.dump(res_dmp, f_w, indent=4, ensure_ascii=False)
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
