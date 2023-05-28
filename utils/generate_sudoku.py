from playwright.sync_api import sync_playwright

def parse_sudoku() -> list:
    """
    Return example: [['', '1', '7', ...], [...]]
    - 9 rows, each row has a list of length 9
    """

    with sync_playwright() as p:
        browser_type = p.chromium
        browser = browser_type.launch()
        page = browser.new_page()
        page.goto('https://soduko-online.com/')
        # page.screenshot(path=f'test.png')

        rows_dict = {}
        for i in range(9):
            rows_dict[i] = []

        for i in range(9):
            box_locator = page.locator(f'.sz{i}')
            number_list = box_locator.locator('div div').all_inner_texts()
            for index, number in enumerate(number_list):
                # fill row: (i // 3) * 3, (i // 3) * 3 + 1, (i // 3) * 3 + 2
                rows_dict[(i // 3) * 3 + index // 3].append(number)

        return_list = []
        for key in rows_dict:
            return_list.append(rows_dict[key])
        browser.close()
        return return_list

if __name__ == '__main__':
    parse_sudoku()