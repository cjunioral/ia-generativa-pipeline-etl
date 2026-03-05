import requests


url = 'https://dummyjson.com/products'
limit = 20


def extract_products(url, limit):
    params = {'limit': limit}
    response = requests.get(url, params= params, timeout= 10)
    
    if response.status_code == 200:
        print('API acessada com sucesso!')
        
        data = response.json()
        
        return data['products']
    
    else:
        print(f'Ocorreu um erro. Status: {response.status_code}')
    

def main():
    
    data = extract_products(url, limit)

    if data is None:
        print('Falha na extração.')
        return
    
    print(f'Extração feita: {len(data)} produtos')
    
    if len(data) > 0:
        print('Exemplo:', data[0]['title'])
    
  
    
if __name__ == '__main__':
    main()