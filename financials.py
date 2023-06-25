def future_value(pv, i, n, m=1):
    """Generates the future value of money

    Args:
        pv (float): The present value of the investment in dollars
        i (float): The current percent interest rate per year
        n (int): The number of years
        m (int): The number of times compounded per year (default 1)
    """
    return pv(1 + (i / m) ** (n * m))