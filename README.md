# Yello Discount Checker
Minimal API to check discounts for Yello electricity.

The app exposes the following endpoint:

    /price/<postcode>

The response includes the current discount in % for the given postcode. E.g.

    {"plz": "00000", "discount": 13}
