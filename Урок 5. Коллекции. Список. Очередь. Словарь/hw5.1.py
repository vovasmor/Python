"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
чья прибыль ниже среднего.
"""
import collections


def counter():
    while True:
        monopoly = collections.Counter()
        try:
            number_of_companies = int(input("Введите количество компаний: "))
            for i in range(number_of_companies):
                company_name = input("Введите название компании: ")
                company_profit = 0
                for j in range(4):
                    while True:
                        try:
                            company_profit += int(input(f"Введите прибыль компании за {j+1} квартал:"))/4
                            break
                        except ValueError as er:
                            print("Необходимо ввести число! Повторите попытку.")
                            continue
                monopoly[company_name] = company_profit
            average_profit = int(sum(monopoly.values()) / number_of_companies)
            print(f"Средняя прибыль для всех предприятий: {average_profit}")
            print(
                f"прибыль выше среднего: {', '.join([n for n, p in monopoly.items() if p >= average_profit])}"
            )
            print(
                f"прибыль ниже среднего: {', '.join([n for n, p in monopoly.items() if p < average_profit])}"
            )
        except ValueError as er:
            print("Необходимо ввести число! Повторите попытку.")


# ---------------------------------------------------------------------------------------------
def namedtuple():
    monopoly = collections.namedtuple("company", ["company_name", "profit1", "profit2", "profit3", "profit4"])
    defdict = collections.defaultdict(int)
    try:
        number_of_companies = int(input("Введите количество компаний: "))
        for i in range(number_of_companies):
            while True:
                try:
                    company = monopoly(
                        company_name=input("Введите название компании: "),
                        profit1=int(input("Введите прибыль за 1 квартал: ")),
                        profit2=int(input("Введите прибыль за 2 квартал: ")),
                        profit3=int(input("Введите прибыль за 3 квартал: ")),
                        profit4=int(input("Введите прибыль за 4 квартал: "))
                    )
                    defdict[company.company_name] = int(
                        (company.profit1 + company.profit2 + company.profit3 + company.profit4) / 4
                    )
                    print(defdict[company.company_name])
                    break
                except ValueError as er:
                    print("Необходимо ввести число! Повторите попытку.")
                    continue
        average_profit = int(sum(defdict.values()) / number_of_companies)
        print(f"Средняя прибыль для всех предприятий: {average_profit}")
        print(f"Компании с прибылью выше среднего: {', '.join([n for n, p in defdict.items() if p >= average_profit])}")
        print(f"Компании с прибылью ниже среднего: {', '.join([n for n, p in defdict.items() if p < average_profit])}")
    except ValueError as er:
        print("Необходимо ввести число! Повторите попытку.")


counter()
namedtuple()
