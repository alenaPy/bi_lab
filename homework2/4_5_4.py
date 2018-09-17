"""BiggerPriceTask."""


def bigger_price(limit, data):
    """Work with data."""
    data = sorted(data, key=lambda row: row['price'], reverse=True)

    return data[:limit]
