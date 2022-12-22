from pprint import pprint

import requests
from v_vars import api_key


def min_ind(ls, key=lambda x: x) -> int:
    if not ls:
        raise NotImplemented
    res = 0
    for i in range(1, len(ls)):
        if key(ls[i]) < key(ls[res]):
            res = i
    return res


def hh_mney(obj: dict) -> int:
    try:
        frst = obj['money']['from'] or 0
    except:
        frst = 0
    try:
        scnd = obj['money']['to'] or 0
    except:
        scnd = 0
    return frst, scnd


def correct_top_10(obj, top: list[dict], key=lambda x: x) -> list[dict]:
    if len(top) < 10:
        top.append(obj)
        return sorted(top, key=key, reverse=True)
    elif len(top) > 10:
        top.append(obj)
        return sorted(top, key=key, reverse=True)[:11]
    mn = min_ind(top, key=key)
    if key(top[mn]) < key(obj):
        del top[mn]
        top.append(obj)
    return sorted(top, key=key, reverse=True)


def make_top_10(name='Python'):
    link = 'https://api.hh.ru/vacancies'
    params = {
        'text': f'NAME:{name}',
        'area': 113,
        'page': 0,
        'per_page': 10,
        'experience': 'noExperience',
        'order_by': 'salary_desc'
    }
    req = requests.get(link, params).json()
    result = []
    for k in req['items']:
        now = {}
        now['name'] = k['name']
        now['url'] = k['alternate_url']
        now['money'] = k['salary']
        now['description'] = k['snippet']['requirement']
        result.append(now)
    return result

