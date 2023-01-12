#!/usr/bin/python3
# Dependencies
# - exiftool
# - imagemagick
import os

MONTHNAMES = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

YEAR = 2022


def main():
    for monthindex, monthname in enumerate(MONTHNAMES):
        make_marker_image(monthname, monthindex + 1, YEAR, f"{monthname}{YEAR}.jpg")


def make_marker_image(monthname: str, monthindex: int, year: int, filename: str):
    os.system(
        f"""convert -size 640x480 xc:darkgrey \
            -font Helvetica -pointsize 96 \
            -gravity Center \
            -draw "text 0,-64 {monthname}" -channel RGB -fill black \
            -draw "text 0,+64 '{year}'" -channel RGB -fill black \
            {filename}"""
    )
    os.system(
        f"""exiftool "-EXIF:DateTimeOriginal={year}{monthindex:02d}01_000000" -overwrite_original {filename}"""
    )


if __name__ == "__main__":
    main()
