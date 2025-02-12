from settings import settings
import requests
def push_notification(title, message, screen_name, fcm_token):
    fire_base_key = settings['fire_base_key']
    fcm_url = "https://fcm.googleapis.com/fcm/send"

    headers = {
        'Authorization': f'key=' + fire_base_key,
        'Content-Type': 'application/json'
    }

    payload = {
        'to': fcm_token,
        'notification': {
            'title': title,
            'body': message,
            'sound': 'default'
        },
        'data': {
            'screen': screen_name
        },
        'priority': 'high'
    }

    response = requests.post(fcm_url, headers=headers, json=payload)

    if response.status_code == 200:
        return {'success': True, 'response': response.json()}
    else:
        return {'success': False, 'response': response.text}
