"""
check_data function takes two parameters - path to a file and a list of functions (validators).
You should:
- read data from file data.txt
- validate each line according to rules. Each rule is a function, that performs some specific check
- write a report to txt file and return absolute path to that file. For each line you should report 
it if it doesn't conform with at least one rule, plus add a reason - the name of a validator that
doesn't pass (if there are more than one failed rules, get the name of the first one that fails)

Valid line should have 5 elements in this order:
email, amount, currency, account, date

You should also implement at least two rules:
- validate_line should check if a line has 5 elements
- validate_date should check if a date is valid. In our case valid date will be anything that follows
the pattern DDDD-DD-DD (four digits - two digits - two digits). Date always exists in a line, even 
if this line is corrupted in some other way.
Feel free to add more rules!

For example, input lines:
foo@example.com 729.83 EUR accountName 2021-01:0
bar@example.com 729.83 accountName 2021-01-02
baz@example.com 729.83 USD accountName 2021-01-02

check_data(filepath, [validate_date, validate_line])

output lines:
foo@example.com 729.83 EUR accountName 2021-01:0 validate_date
bar@example.com 729.83 accountName 2021-01-02 validate_line
"""
import datetime
from typing import Callable, Iterable


def validate_line(line: str) -> bool:
    return len(line.split(" ")) == 5


def validate_date(date: str) -> bool:
    date_parts = date.split("-")
    return all(item.isnumeric() for item in date_parts) and \
           len(date_parts[0]) == 4 and len(date_parts[1]) == 2 and len(date_parts[2]) == 2
#    try:
#        datetime.datetime.strptime(date, '%Y-%m-%d')
#        return True
#    except ValueError:
#        return False

def check_data(filepath: str, validators: Iterable[Callable]) -> str:
    filelines = get_file_lines(filepath)
    with open("result.txt", "wt", encoding="utf-8") as resultfile:
        for line in filelines:
            validations = []
            for validator in validators:
                if validator.__name__ == "validate_line":
                    validations.append((validator.__name__, validator(line)))
                elif validator.__name__ == "validate_date":
                    content = line.split(" ")
                    validations.append((validator.__name__, validator(content[len(content) - 1])))
            first_issue = next((x for x in validations if x[1] is False), None)
            if first_issue is not None:
                resultfile.write(f"{line} {first_issue[0]}\n")
                resultfile.flush()
        return resultfile.name
    
def get_file_lines(filepath: str) -> Iterable[str]:
    with open(filepath, "r") as file:
        lines = [i.strip() for i in file.readlines()]
        return lines
