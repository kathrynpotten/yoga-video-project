""" Script to extract length of yoga videos from Yoga with Adrience website for "30 days of yoga" playlists """

import requests
import bs4
from pytube import YouTube
import math


with open("./video_lengths.txt", "a", encoding="utf-8") as file:
    # 30 days of yoga
    print("Writing '30 Days of Yoga' ...")
    file.write("\n30 Days of Yoga\n")
    for page in range(1, 31):
        res = requests.get(f"https://yogawithadriene.com/30-days-yoga-day-{page}/")
        soup = bs4.BeautifulSoup(res.text, "lxml")
        video = soup.select(".ct-span.oxy-stock-content-styles p iframe")[0]["src"]
        yt = YouTube(video)
        minutes = math.floor((yt.length) / 60)
        seconds = yt.length - minutes * 60
        print(f"Writing day {page} ...")
        file.write(f"\nDay {page}: {minutes:02d}:{seconds:02d}")

    # camp
    print("Writing 'Yoga Camp' ...")
    file.write("\n\nYoga Camp\n")
    for page in range(1, 31):
        res = requests.get(f"https://yogawithadriene.com/yoga-camp-day-{page}/")
        soup = bs4.BeautifulSoup(res.text, "lxml")
        video = soup.select(".ct-span.oxy-stock-content-styles p iframe")[0]["src"]
        yt = YouTube(video)
        minutes = math.floor((yt.length) / 60)
        seconds = yt.length - minutes * 60
        print(f"Writing day {page} ...")
        file.write(f"\nDay {page}: {minutes:02d}:{seconds:02d}")

    # true
    print("Extracting 'True' titles ...")
    file.write("\n\nTrue\n")
    names = []
    for page in range(1, 7):
        res = requests.get(
            f"https://yogawithadriene.com/free-yoga-videos/true-30-day-yoga-journey/page/{page}/"
        )
        soup = bs4.BeautifulSoup(res.text, "lxml")
        videos = soup.select(".oxy-post-title")
        for video in videos:
            title = video.text.split(" - ")[-1]
            names.append(title.lower().replace(" ", "-"))
    names.reverse()

    print("Writing 'True' ...")
    for page in range(1, 31):
        name = names[page]
        res = requests.get(f"https://yogawithadriene.com/true-day-{page}-{name}/")
        soup = bs4.BeautifulSoup(res.text, "lxml")
        video = soup.select(".wp-block-embed__wrapper iframe")[0]["src"]
        yt = YouTube(video)
        minutes = math.floor((yt.length) / 60)
        seconds = yt.length - minutes * 60
        print(f"Writing day {page} ...")
        file.write(f"\nDay {page}: {minutes:02d}:{seconds:02d}")

    # revolution
    print("Writing 'Revolution' ...")
    file.write("\n\nRevolution\n")

    # page 1 has different HTML
    res = requests.get(f"https://yogawithadriene.com/revolution-day-1/")
    soup = bs4.BeautifulSoup(res.text, "lxml")
    video = soup.select(".ct-span.oxy-stock-content-styles p iframe")[0]["src"]
    yt = YouTube(video)
    minutes = math.floor((yt.length) / 60)
    seconds = yt.length - minutes * 60
    print(f"Writing day {page} ...")
    file.write(f"\nDay {page}: {minutes:02d}:{seconds:02d}")

    for page in range(2, 32):
        res = requests.get(f"https://yogawithadriene.com/revolution-day-{page}/")
        soup = bs4.BeautifulSoup(res.text, "lxml")
        video = soup.select(".wp-block-embed__wrapper iframe")[0]["src"]
        yt = YouTube(video)
        minutes = math.floor((yt.length) / 60)
        seconds = yt.length - minutes * 60
        print(f"Writing day {page} ...")
        file.write(f"\nDay {page}: {minutes:02d}:{seconds:02d}")

    # dedicate
    print("Extracting 'Dedicate' titles ...")
    file.write("\n\nDedicate\n")
    names = []
    for page in range(1, 6):
        res = requests.get(
            f"https://yogawithadriene.com/free-yoga-videos/dedicate-a-30-day-yoga-journey/page/{page}/"
        )
        soup = bs4.BeautifulSoup(res.text, "lxml")
        videos = soup.select(".oxy-post-title")
        for video in videos:
            title = video.text.split(" - ")[-1]
            names.append(title.lower().replace(" ", "-"))
    names.reverse()
    print(names)
    print("Writing 'Dedicate' ...")
    for page in range(1, 31):
        name = names[page - 1]
        res = requests.get(f"https://yogawithadriene.com/dedicate-day-{page}-{name}/")
        soup = bs4.BeautifulSoup(res.text, "lxml")
        video = soup.select(".wp-block-embed__wrapper iframe")[0]["src"]
        yt = YouTube(video)
        minutes = math.floor((yt.length) / 60)
        seconds = yt.length - minutes * 60
        print(f"Writing day {page} ...")
        file.write(f"\nDay {page}: {minutes:02d}:{seconds:02d}")
