

def extra_cost(carbon_amount):
    """
    Returns carbon offset price given carbon emitted ($0.01 per kg)
    Parameters
    ----------
    carbon_amount: float
        carbon emitted, in kg

    Returns
    -------
    extra_cost: float
        carbon offset price
    """
    rate = 0.01 #$ per kg
    extra_cost = carbon_amount*rate
    return round(extra_cost, 2)

