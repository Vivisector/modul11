import requests

response = requests.get('https://httpbin.org/get')
print('вывод некоторого запроса в виде неформатированного текста')
print(response.text)
print(f'{'-'*20}\nвывод некоторого запроса в виде словаря (ключ-значение)')
print(response.json())
print()
print(f'{'-'*20}\nвывод статуса запроса (успешно-неуспешно)')
print(response.status_code)
print(f'{'-'*20}\nвывод web-адреса запроса')
print(response.url)
print(f'\netc...')