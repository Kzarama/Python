from scrapy.selector import Selector

html_code = open('html.html', 'r').read()
file = open('result.txt', 'w')

xpath_table_uno = '//table[@id="table_uno"]/tbody/tr[2]/th[2]//text()'

titles = Selector(text=html_code).xpath(xpath_table_uno).getall()


def fix_date(date: str):
    new_date = '/'.join(date.replace(',', '').split(' '))
    monts_replace = {'Ene': '01', 'Feb': '02',
                     'Mar': '03', 'Abr': '04', 'May': '05'}
    for initial_month, month in monts_replace.items():
        new_date = new_date.replace(initial_month, month)
    return new_date


file.write(
    'Subject,Start date,Start time,End Date,End Time,All Day Event,Description,Location,Private')

for index, subject in enumerate(titles):
    xpath_table_dos_hour = f'(//table[@id="table_dos"]/tbody)[{index+1}]/tr/th[2]//text()'
    links_selector_hour = Selector(text=html_code).xpath(
        xpath_table_dos_hour).getall()
    links_selector_hour.pop(0)

    xpath_table_dos_date = f'(//table[@id="table_dos"]/tbody)[{index+1}]/tr/th[5]//text()'
    links_selector_date = Selector(text=html_code).xpath(
        xpath_table_dos_date).getall()
    links_selector_date.pop(0)

    xpath_table_dos_url = f'(//table[@id="table_dos"]/tbody)[{index+1}]/tr/th[4]//text()'
    links_selector = Selector(text=html_code).xpath(
        xpath_table_dos_url).getall()
    links_selector.pop(0)

    for index_class in range(0, len(links_selector_date)):
        file.write(subject[14:] + ',' + fix_date(links_selector_date[index_class][:12]) + ',' + links_selector_hour[index_class][:8] + ',' + fix_date(links_selector_date[index_class]
                   [:12]) + ',' + links_selector_hour[index_class][11:] + ',' + 'False' + ',' + links_selector[index_class*2+1][18:] + ',' + links_selector[index_class*2] + ',' + 'True' + '\n')

file.close()
