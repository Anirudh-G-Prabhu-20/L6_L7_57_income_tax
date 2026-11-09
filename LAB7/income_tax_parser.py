
def clean_pan(pan):
    """
    Removes spaces from a PAN and upper-cases it.
    Returns an empty string for invalid input.
    """
    if not isinstance(pan, str):
        return ""

    return pan.strip().replace(' ', '').upper()


def parse_amount(text):
    """
    Converts an amount such as 'Rs 12,50,000' into an int.
    Returns 0 for invalid input.
    """
    if not isinstance(text, str):
        return 0

    text = text.lower().replace('rs', '').replace(',', '').strip()

    try:
        return int(text)
    except ValueError:
        return 0


def parse_tax_slab(line):
    """
    Parses 'LOW-HIGH:RATE' into a (low, high, rate) tuple.
    Returns (0, 0, 0) for invalid input.
    """
    if not isinstance(line, str):
        return (0, 0, 0)

    try:
        parts = line.split(':')

        if len(parts) != 2:
            return (0, 0, 0)

        limits, rate = parts
        limits = limits.split('-')

        if len(limits) != 2:
            return (0, 0, 0)

        low, high = limits

        return int(low), int(high), int(rate)

    except ValueError:
        return (0, 0, 0)


def main():
    print("==== Running clean_pan ====")
    value = input("Enter a PAN (e.g. abcde 1234f): ")
    print("Cleaned PAN:", clean_pan(value))

    print("\n==== Running parse_amount ====")
    value = input("Enter an amount (e.g. Rs 12,50,000): ")
    print("Amount in rupees:", parse_amount(value))

    print("\n==== Running parse_tax_slab ====")
    value = input("Enter a tax slab as LOW-HIGH:RATE (e.g. 250000-500000:5): ")
    print("Tax slab (low, high, rate):", parse_tax_slab(value))


if __name__ == "__main__":
    main()
