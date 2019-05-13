from moneybird import MoneyBird, TokenAuthentication
import logging

logger = logging.getLogger('moneybird')
moneybird = MoneyBird(TokenAuthentication('fc249145ec8fd04e167e3e2c80ad04123e883267219925ac5847abb6a027d03d'))
moneybird.get('administrations')

administrations = moneybird.get('administrations')

for administration in administrations:
    id = administration['id']
    contacts = moneybird.get('contacts', administration_id=id)


    # Print invoices per contact
    for contact in contacts:
        print(contact['company_name'])

        for invoice in moneybird.get('sales_invoices?filter=contact_id:%s' % contact['id'], administration_id=id):
            print('  ', invoice['invoice_id'])



contacts = moneybird.get('contacts', administration_id=id)
print(contacts)