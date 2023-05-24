import requests

def get_uri(uri):
    r = requests.get(uri, verify=False)
    print(r.status_code)
    print(r.elapsed)
    print(r.text)
    return r


def main():
    tods = "http://worldtimeapi.org/api/timezone/America/Chicago"
    uri = "https://127.0.0.1:7142/GetWeatherForecast"
    r = get_uri(tods)

if __name__ == "__main__":
    main()