'''
0. To run file type `python tasks.py in_1000000.json`.
   Example structure of `in_xxxxx.py`:
   ```
   [
    {
        "package": "FLEXIBLE",
        "created": "2020-03-10T00:00:00",
        "summary": [
            {
                "period": "2019-12",
                "documents": {
                    "incomes": 63,
                    "expenses": 13
                }
            },
            {
                "period": "2020-02",
                "documents": {
                    "incomes": 45,
                    "expenses": 81
                }
            }
        ]
    },
    {
        "package": "ENTERPRISE",
        "created": "2020-03-19T00:00:00",
        "summary": [
            {
                "period": "2020-01",
                "documents": {
                    "incomes": 15,
                    "expenses": 52
                }
            },
            {
                "period": "2020-02",
                "documents": {
                    "incomes": 76,
                    "expenses": 47
                }
            }
        ]
    }
   ]
   ```
1. Please make below tasks described in docstring of functions in 7 days.
2. Changes out of functions body are not allowed.
3. Additional imports are not allowed.
4. Data could have wholes in periods range ex. 2022-01,2022-03 (missing February),
   then we assume that item has 0 documents in period
5. Send us your solution (only tasks.py) through link in email.
   In annotations write how much time you spent for each function.
6. First we will run automatic tests checking (using: 1 mln and 100 mln items):
   a) proper results and edge cases
   b) CPU usage
   c) memory usage
7. If your solution will NOT pass automatic tests (we allow some errors)
   application will be automatically rejected without additional feedback.
   You can apply again after 30 days.
8. Our develepers will review code (structure, clarity, logic).
'''
import datetime
import collections
import itertools


def pomiar(func):
    def wrapper(*args, **kwargs):
        x = datetime.datetime.now()
        a = func(*args, **kwargs)
        y = datetime.datetime.now()
        y = y - x
        print(f"Wywołanie {func.__name__.upper()} zajęło: {y} ")
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
    cut_created_list = []
    [cut_created_list.append(dic_value['created'][:7]) for dic_value in data_in]

    dict_of_periods = {}
    for term in cut_created_list:
        if term in dict_of_periods:
            dict_of_periods[term] += 1
        else:
            dict_of_periods[term] = 1

    return dict_of_periods


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
    result = {}
    for record in data_in:
        for period_data in record["summary"]:
            if period_data["period"] not in result:
                result[period_data["period"]] = {"incomes": 0, "expenses": 0, "total": 0}
            result[period_data["period"]]["incomes"] += period_data["documents"]["incomes"]
            result[period_data["period"]]["expenses"] += period_data["documents"]["expenses"]

    return {key: {**value, "total": value["incomes"] + value["expenses"]} for key, value in result.items()}


@pomiar
def task_3(data_in):
    '''
        Return average(integer) number of documents per day
        in last three periods
        for package in ['ENTERPRISE', 'FLEXIBLE']
        ex. 64
    '''
    result = {}
    for record in data_in:
        if record['package'] in ['FLEXIBLE', 'ENTERPRISE']:
            for period_data in record["summary"]:
                if period_data["period"] not in result:
                    result[period_data["period"]] = 0
                result[period_data['period']] += period_data['documents']['incomes'] + period_data['documents'][
                    'expenses']
    # no_of_days = len(result)

    return sum(result.values()) // len(result)


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
