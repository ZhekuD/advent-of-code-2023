from pathlib import Path


FILE = Path(__file__).parent / 'input'


class LotteryCalculator:
    def __init__(self, file_strings: list[str]):
        self.file_strings = file_strings
        self.result_sum = 0

    def calculate(self) -> int:
        for file_string in self.file_strings:
            file_string = file_string.replace('\n', '')
            card, winning_numbers, my_numbers = self._parse_file_string(file_string)

            winning_numbers_count = self._count_winnig_numbers(winning_numbers, my_numbers)

            if winning_numbers_count > 0:
                self.result_sum += 2 ** (winning_numbers_count - 1)

        return self.result_sum

    def _parse_file_string(self, file_string: str) -> tuple[str, list[str], list[str]]:
        # string example: Card   1:  4 16 87 61 11 37 43 25 49 17 | 54 36 14 55 83 58 43 15 87 17 97 11 62 75 37  4 49 80 42 61 20 79 25 24 16
        card, numbers = file_string.split(': ')
        winning_numbers, my_numbers = numbers.split(' | ')
        winning_numbers = winning_numbers.split(' ')
        my_numbers = my_numbers.split(' ')

        # remove empty strings
        winning_numbers = [num for num in winning_numbers if num != '']
        my_numbers = [num for num in my_numbers if num != '']

        return card, winning_numbers, my_numbers
    
    def _count_winnig_numbers(self, winning_numbers: list[str], my_numbers: list[str]) -> int:
        return len(set(winning_numbers) & set(my_numbers))


if __name__ == "__main__":
    with FILE.open() as f:
        file_strings = f.readlines()
    calculator = LotteryCalculator(file_strings)
    print(calculator.calculate())
