from playwright.sync_api import sync_playwright

def solve_sudoku(board: list) -> list:
    """
    board: [['1', '', '2', ...], [...], ...]
    """
    with sync_playwright() as p:
        browser_type = p.chromium
        browser = browser_type.launch()
        page = browser.new_page()
        page.goto('https://sudokuspoiler.com/sudoku/sudoku9')

        for i, input in enumerate(page.locator('input').all()):
            if i >= 81:
                break
            # board[x][y] => x = i // 9, y = i % 9
            x = i // 9
            y = i % 9
            input.fill(board[x][y])

        page.locator('#solveButton').click()

        page.wait_for_timeout(500)
        # page.screenshot(path=f'click_solve_wait.png')

        return_list = []
        temp_list = []

        for i in page.locator('input').all():
            temp_list.append(str(i.input_value()))
            if len(temp_list) >= 9:
                return_list.append(temp_list)
                temp_list = []
            if len(return_list) >= 9:
                break

        browser.close()
    return return_list

def board_str_to_board(board_str):
    """
    input: ..8..9.1..7...1..4.
    output: [["", "8", "", "9"], []]
    """
    return_list = []
    temp_list = []
    for i, _ in enumerate(board_str):
        if i + 1 >= len(board_str):
            if board_str[i] == '.':
                temp_list.append("")
                return_list.append(temp_list)
            break
        if board_str[i] != '.':
            continue
        if board_str[i+1] == '.':
            temp_list.append("")
        else:
            temp_list.append(str(board_str[i+1]))

        if len(temp_list) >= 9:
            return_list.append(temp_list)
            temp_list = []

    return return_list

if __name__ == "__main__":
    # print(board_str_to_board('..8..9.1..7...1..4..5..3........3.5..8..3.6.....2...5...4...6...4..6..9...5.3..5..2..6...7...5..1.8......3....5.'))

    print(solve_sudoku(board_str_to_board('..8..9.1..7...1..4..5..3........3.5..8..3.6.....2...5...4...6...4..6..9...5.3..5..2..6...7...5..1.8......3....5.')))