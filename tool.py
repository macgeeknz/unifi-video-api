from unifivideo import Handle
from unifivideo import recordings
import json


def main():
    print("Unifi Video Tool")
    settings = json.load(open('settings.json'))
    handle = Handle(settings['api_key'], settings['server'])

    items = recordings.list(handle, starttime=1457564400000, endtime=1457634748044)
    for item in items:
        print(item)

if __name__ == "__main__":
    main()