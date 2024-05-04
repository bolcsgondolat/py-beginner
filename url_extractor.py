url = "https://exampleURL1.com/r626c36"

def extract_store_url(url):
    
    last_part = url.split('/')[-1]
    # Extract the last seven characters from the last part
    store_id = last_part[-7:]
    return store_id

id = extract_store_url(url)
print(id)