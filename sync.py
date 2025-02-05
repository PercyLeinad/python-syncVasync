import requests
import time


with open('urls1000.txt','r') as f:
    urls = f.read().split()

def get_response(curr_url,session):
    try:
        res = session.get(curr_url)
        return res.status_code
    except requests.exceptions.RequestException as exp:
        print(exp)

def main():
    with requests.session() as session:
        for url in urls:
            print(f"'status': {get_response(url,session)},url': {url}")

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print('Elapsed {:5f}'.format(stop-start))