def zip_checker(zipcode):
    if len(zipcode) == 5:
        if not zipcode.startswith('00'):
            return zipcode
        else:
            return 'Invalid ZIP Code.'
    elif len(zipcode) == 4:
        if zipcode[0] != '0':
            return '0' + zipcode
        else:
            return 'Invalid ZIP Code.'
    else:
        return 'Invalid ZIP Code.'
    

zip_checker('00280')