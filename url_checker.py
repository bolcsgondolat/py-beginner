def url_checker(url):
    # Extract store_id from the URL
    store_id = url.split('/')[-1]
    url = url.split('://')[0]
    
    if not url.startswith('https') or len(store_id) !=7:
        if not url.startswith('https'):
            print('{} is an invalid protocol.' .format(url))
        else:
            print('{} is an invalid store ID.' .format(store_id))
    else:
        print(store_id)

# Example usage:
url_checker('ftps://exampleURL1.com/r626c36')