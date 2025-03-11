#Даны линейные функции спроса и предложения Qd=a-bP, Qs=c+dP.
#Ввели фиксированный налог на потребителей в размере t рублей.
#1)Найдите показатели равновесия до и после введения налога.
#2)Найдите изменение объемов продаж и цен, налоговые поступления государства, изменение выигрышей покупателей и продавцов.

import local as lcl

def main():
    """
    Main function.
    :return: None
    """
#Вводим значения коэффицентов
    a = int(input(lcl.maximum_demand))
    b = int(input(lcl.slope_demand))
    c = int(input(lcl.minimum_supply))
    d = int(input(lcl.slope_supply))
    t = int(input(lcl.tax))
#Находим изначально равновесие
    pe_0 = (a - c) / (d + b)
    qe_0 = a - b * pe_0
#Находим цену покупателя и продавца после введения налога
    ps_1 = (c - a + b * t) / (- b - d)
    qs_1 = c + d * ps_1
    pd_1 = ps_1 + t
#Находим изменение объемов продаж и цен
    delta_q = qs_1 - qe_0
    delta_p = ps_1 - pe_0
#Находим налоговые поступления в бюджет государства
    tax_revenue = qs_1 * t
#Находим изменения выигрышей покупателей и продавцов
    delta_cs = (qs_1 + qe_0) / 2 * (pd_1 - pe_0)
    delta_ps = (qs_1 + qe_0) / 2 * (pe_0 - ps_1)

#Выводим найденные значения
    print(f"Изначальный равновесный объем:{qe_0}")
    print(f"Изначальная равновесная цена:{pe_0}")
    print(f"Новый равновесный объем:{qs_1}")
    print(f"Новая цена продавца:{ps_1}")
    print(f"Новая цена покупателя:{pd_1}")
    print(f"Изменение объема продаж:{delta_q}")
    print(f"Изменение цены:{delta_p}")
    print(f"Налоговые поступления:{tax_revenue}")
    print(f'Изменение выигрыша покупателей:{delta_cs}')
    print(f'Изменение выигрыша продавцов:{delta_ps}')


if __name__ == '__main__':
    main()
