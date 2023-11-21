""" Script to extract length of yoga sequences from video descriptions on Yoga with Adriene website for "30 days of yoga" playlists """

import requests
import bs4
import re


with open("./sequence_lengths.txt", "a", encoding="utf-8") as file:
    # 30 days of yoga
    file.write("\n30 Days of Yoga\n")
    for page in range(1, 31):
        res = requests.get(f"https://yogawithadriene.com/30-days-yoga-day-{page}/")
        soup = bs4.BeautifulSoup(res.text, "lxml")
        items = soup.select(".ct-span.oxy-stock-content-styles p")
        for item in items:
            pattern = r"\d\d\smin(|ute)"
            match = re.search(pattern, str(item))
            if match != None:
                file.write(f"\nDay {page}: {match.group()}")

    # revolution
    file.write("\n\nRevolution\n")
    for page in range(1, 31):
        res = requests.get(f"https://yogawithadriene.com/revolution-day-{page}/")
        soup = bs4.BeautifulSoup(res.text, "lxml")
        items = soup.select(".ct-span.oxy-stock-content-styles p")
        for item in items:
            pattern = r"\d\d\smin(|ute)"
            match = re.search(pattern, str(item))
            if match != None:
                file.write(f"\nDay {page}: {match.group()}")

    # camp
    file.write("\n\nYoga Camp\n")
    for page in range(1, 31):
        res = requests.get(f"https://yogawithadriene.com/yoga-camp-day-{page}/")
        soup = bs4.BeautifulSoup(res.text, "lxml")
        items = soup.select(".ct-span.oxy-stock-content-styles p")
        for item in items:
            pattern = r"\d\d\smin(|ute)"
            match = re.search(pattern, str(item))
            if match != None:
                file.write(f"\nDay {page}: {match.group()}")
