import requests
import data
import configuration

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body);

print(response.status_code)
print(response.json())

def post_new_client_kit(kit_body, auth_token):
    headers = data.headers_for_kit_creation
    headers['Autorization'] = auth_token
    print(headers)

    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=kit_body,
                         headers=headers)
