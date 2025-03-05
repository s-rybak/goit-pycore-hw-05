import re


# Function that extracts all numbers from the text and returns them as a generator
# The numbers in the text are assumed to be separated by spaces on both sides
def generator_numbers(str):
    regex = re.compile(r'\s[\d\.]+\s')
    # Iterate through all matches found in the text
    for match in re.finditer(regex, str):
        yield float(match.group().strip())

# Function that calculates the sum of all numbers in the text
# Takes text string and generator function as arguments
def sum_profit(str, func):
    return sum(func(str))


# Usage example
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

print(list(generator_numbers(text)))
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")