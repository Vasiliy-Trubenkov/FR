import requests
import json

def _3():
    jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE1NTczMjQsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IlZhc2lsaXlUcnViZW5rb3YifQ.JhiQto2K7Z5_C11sOthxALN-gIuaZgPivz8wxYuCI7M'
    url = "https://probe.fbrq.cloud/v1/send/2"
    headers = {"accept": "application/json", 'Authorization': jwt, "Content-Type": "application/json"}
    data = {'id': 2, 'phone': 9996664444, 'text': 'just a text'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r

print(_3().json()["message"])


def planir():
    # Планировщик
    import schedule
    import datetime
    from time import sleep
    from threading import Thread
    print(datetime.datetime.now())

    def scheduler():
        schedule.every().day.at('10:07').do(mailing_check)

        while True:
            schedule.run_pending()
            sleep(1)  # Выберите оптимальное значение под свои задачи планировщика

    def CancelJob():
        # возвращаем такой токен, и это задание снимается с выполнения в будущем
        return schedule.CancelJob

    # Создаём и запускаем планировщик в отдельном потоке
    t = Thread(target=scheduler).start()
