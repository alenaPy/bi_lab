"""Price."""


def main():
    """Main."""
    instr = open('input.txt', 'r').read()
    [dollar, cent, count] = get_nums(instr)
    print(calculate_price(dollar, cent, count))


def get_nums(instr):
    """Get numbers from string."""
    return [int(s) for s in instr.split() if s.isdigit()]


def calculate_price(dollar, cent, count):
    """Price calculation."""
    return 'Total cost: {0} dollars {1} ' \
           'cents.'.format((dollar * 100 + cent) * count // 100,
                           (dollar * 100 + cent) * count % 100)


main()
