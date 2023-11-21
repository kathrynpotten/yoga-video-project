""" Function to extract length of yoga videos from Yoga with Adrience website for any given "30 days of yoga" playlist """


import requests
import bs4
from pytube import YouTube
import math


def extract_video_lengths_30_days(title, selection, days, file, title_extract=False):
    print(f"Writing '{title}' ...")
    file.write(f"\n{title}\n")

    if title_extract:
        print(f"Extracting '{title}' titles ...")
        names = []
        for page in range(1, 7):
            res = requests.get(
                f"https://yogawithadriene.com/free-yoga-videos/{title.lower().replace(' ','-')}-30-day-yoga-journey/page/{page}/"
            )
            soup = bs4.BeautifulSoup(res.text, "lxml")
            videos = soup.select(".oxy-post-title")
            for video in videos:
                video_title = video.text.split(" - ")[-1]
                names.append(video_title.lower().replace(" ", "-"))
        names.reverse()

        for page in range(1, days + 1):
            name = names[page]
            res = requests.get(
                f"https://yogawithadriene.com/{title.lower().replace(' ','-')}-day-{page}-{name}/"
            )
            soup = bs4.BeautifulSoup(res.text, "lxml")
            video = soup.select(selection)[0]["src"]
            yt = YouTube(video)
            minutes = math.floor((yt.length) / 60)
            seconds = yt.length - minutes * 60
            print(f"Writing day {page} ...")
            file.write(f"\nDay {page}: {minutes:02d}:{seconds:02d}")

    else:
        for page in range(1, days + 1):
            res = requests.get(
                f"https://yogawithadriene.com/{title.lower().replace(' ','-')}-day-{page}/"
            )
            soup = bs4.BeautifulSoup(res.text, "lxml")
            video = soup.select(selection)[0]["src"]
            yt = YouTube(video)
            minutes = math.floor((yt.length) / 60)
            seconds = yt.length - minutes * 60
            print(f"Writing day {page} ...")
            file.write(f"\nDay {page}: {minutes:02d}:{seconds:02d}")


if __name__ == "__main__":
    with open("./video_lengths_test.txt", "a", encoding="utf-8") as file:
        extract_video_lengths_30_days(
            "True", ".wp-block-embed__wrapper iframe", 30, file, True
        )
