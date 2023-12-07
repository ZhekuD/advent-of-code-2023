from pathlib import Path


FILE = Path(__file__).parent / 'input'
# FILE = Path(__file__).parent / 'input_test'


class LotteryCalculator:
    def __init__(self, file_strings: list[str]):
        self.file_strings = file_strings
        self.result_sum = 0
        self.scratch_card_dict = {}

    def calculate(self) -> int:
        for file_string in self.file_strings:
            file_string = file_string.replace('\n', '')
            card_number, winning_numbers, my_numbers = self._parse_file_string(file_string)
            # calculate the number of winning numbers
            winning_numbers_count = self._count_winnig_numbers(winning_numbers, my_numbers)

            # add 1 to result for the card itself and 1 for each copy of the card
            number_of_copies = 1 + self.scratch_card_dict.get(card_number, 0)
            self.result_sum += number_of_copies
            self.scratch_card_dict.pop(card_number, None)  # and remove the card from the dict

            # if there are no winning numbers, continue to the next card
            if winning_numbers_count == 0:
                continue
            
            # add number of copies for each card that has a higher number than the current card
            for i in range(card_number + 1, card_number + winning_numbers_count + 1):
                if i not in self.scratch_card_dict:
                    self.scratch_card_dict[i] = number_of_copies
                else:
                    self.scratch_card_dict[i] += number_of_copies

        return self.result_sum

    def _parse_file_string(self, file_string: str) -> tuple[int, list[str], list[str]]:
        # string example: Card   1:  4 16 87 61 11 37 43 25 49 17 | 54 36 14 55 83 58 43 15 87 17 97 11 62 75 37  4 49 80 42 61 20 79 25 24 16
        card, numbers = file_string.split(': ')
        card_number = int(card.split(' ')[-1])
        winning_numbers, my_numbers = numbers.split(' | ')
        winning_numbers = winning_numbers.split(' ')
        my_numbers = my_numbers.split(' ')

        # remove empty strings
        winning_numbers = [num for num in winning_numbers if num != '']
        my_numbers = [num for num in my_numbers if num != '']

        return card_number, winning_numbers, my_numbers
    
    def _count_winnig_numbers(self, winning_numbers: list[str], my_numbers: list[str]) -> int:
        # set intersection to find the elements that are in both lists
        return len(set(winning_numbers) & set(my_numbers))


if __name__ == "__main__":
    with FILE.open() as f:
        file_strings = f.readlines()
    calculator = LotteryCalculator(file_strings)
    print(calculator.calculate())
