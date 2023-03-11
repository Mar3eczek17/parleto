import datetime
import collections
import itertools

def pomiar(func):
    def wrapper(*args, **kwargs):
        x = datetime.datetime.now()
        a= func(*args, **kwargs)
        y = datetime.datetime.now()
        y=y-x
        print(f"Wywołanie zajęło: {y} ")
        return a
    return wrapper


@pomiar
def task_1(data_in):
    '''
        Return number of items per created[year-month].
        ex. {
            '2020-04': 29,
            '2020-05': 24
        }
    '''
    return {
            '2020-04': 29,
            '2020-05': 24
        }

@pomiar
def task_2(data_in):
    '''
        Return number of documents per period (incomes, expenses, total).
        ex. {
            '2020-04': {
                'incomes': 2480,
                'expenses': 2695,
                'total': 5175
            },
            '2020-05': {
                'incomes': 2673,
                'expenses': 2280,
                'total': 4953
            }
        }
    '''
    return  {
            '2020-04': {
                'incomes': 2480,
                'expenses': 2695,
                'total': 5175
            },
            '2020-05': {
                'incomes': 2673,
                'expenses': 2280,
                'total': 4953
            }
    }

@pomiar
def task_3(data_in):
    '''
        Return average(integer) number of documents per day
        in last three periods
        for package in ['ENTERPRISE', 'FLEXIBLE']
        ex. 64
    '''
    r=0
    for i in data_in:
        try:
            x=i.get("package")
            if x=='FLEXIBLE' or 'ENTERPRISE':
                r+=1
        except:
            continue
    return r


if __name__ == '__main__':
    import json
    import sys
    try:
        with open(sys.argv[1]) as fp:
            data_in = json.load(fp)
    except IndexError:
        print(f'''USAGE:
    {sys.executable} {sys.argv[0]} <filename>

Example:
    {sys.executable} {sys.argv[0]} in_1000000.json
''')
    else:
        for func in [task_1, task_2, task_3]:
            print(f'\n>>> {func.__name__.upper()}')
            print(json.dumps(func(data_in), ensure_ascii=False, indent=2))