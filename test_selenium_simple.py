import time


def test_search_example(selenium):
    """ Найдите какую-нибудь фразу в google и сделайте скриншот страницы. """

    # Откройте страницу поиска google:
    selenium.get('https://google.com')

    time.sleep(5)  # только в демонстрационных целях, не повторяйте это на реальных проектах!

    # Найдите поле для ввода текста поиска:
    search_input = selenium.find_element_by_name('q')


    # Введите текст для поиска:
    search_input.clear()
    search_input.send_keys('first test')

    time.sleep(5)  # только в демонстрационных целях, не повторяйте это на реальных проектах!

    # щелкнуть поиск:
    search_button = selenium.find_element_by_name('btnK')
    search_button.submit()

    time.sleep(10)  # только в демонстрационных целях, не повторяйте это на реальных проектах!

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('result.png')
