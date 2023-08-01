import requests
import threading
import random
import time

while True:

    colors = ['#FFFFFF', '#E4E4E4', '#888888', '#222222', '#FFA7D1', '#E50000', '#E59500', '#A06A42', '#E5D900', '#94E044', '#02BE01', '#00D3DD', '#0083C7', '#0000EA', '#CF6EE4', '#820080']


    url = 'https://mynewbanner.com/api/place'

    def place(x, y):
        data = {
            'x': x,
            'y': y,
            'hex': random.choice(colors)
        }
        csrf_token = 'Npaxu25N-3GV_JhPGNEFY-B58Q04730cnx4c'
        headers = {
            'X-Csrf-Token': csrf_token,
            'Cookie': 'session=eyJjc3JmU2VjcmV0IjoieWo1VktVSk5ISjI1eXB3aXVGRGR3bkd5IiwicGFzc3BvcnQiOnsidXNlciI6IjY0Yzc5MDA1Y2JlNzQ0ZGIwMTcwNzIzZiJ9fQ==; session.sig=FRq06lQqe_a7LP1VNK6dEkT2WqU',
        }
        while True:
            try:
                response = requests.post(url, data=data, headers=headers)
                break
            except:
                pass

        while True:
            if response.status_code != 200:
                while True:
                    try:
                        response = requests.post(url, data=data, headers=headers)
                        break
                    except:
                        pass
            else:
                break
    max_x = 1441
    max_y = 1441

    current_x = -1
    current_y = 50

    start_x = -1
    start_y = 49







    while current_x * current_y != max_x * max_y:
        if current_x != max_x:
            while True:
                try:
                    threading.Thread(target=place, args=(current_x, current_y)).start()
                    break
                except:
                    pass
            print(f"X:{current_x} Y: {current_y}")
            current_x += 1

        else:
            current_y += 1
            current_x = 0
            try:
                threading.Thread(target=place, args=(current_x, current_y)).start()
                break
            except:
                pass
            print(f"X:{current_x} Y: {current_y}")
        time.sleep(0.1)
    print("map successfully destroyed.")
