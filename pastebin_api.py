'''
Library for interacting with the PasteBin API
https://pastebin.com/doc_api
'''
import requests

PASTEBIN_API_POST_URL = 'https://pastebin.com/doc_api '
API_DEV_KEY = 'K-OqOvRLRxaO3tPj7vlyQSozF9y-AMNs'

def post_new_paste(title, body_text, expiration='N', listed=True):
    
    params = {
        'api_dev_key': API_DEV_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 0 if listed else 1
    }
    
    
    print("Sending request to pastebin_api")
    response = requests.post(PASTEBIN_API_POST_URL, data=params)
    
    
    if response.status_code == 200 and response.text.startswith('https://'):
        print("Paste created successfully!")
        return response.text
    else:
        print("Failed to paste. Response status code:", response.status_code)
        print("Response text:", response.text)
        return None
    
    
    """Posts a new paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False) 
    
    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """    
    if __name__ == "__main__":
    
     paste_url = post_new_paste("Test Paste", "This is a test paste.", "10M", True)
    if paste_url:
        print("Paste URL:", paste_url)
    else:
        print("Failed")