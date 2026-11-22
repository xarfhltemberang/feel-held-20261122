import os

TEXT = (
    "You've read a hundred voices tonight, each asking to be chosen. "
    "This one asks nothing. "
    "A kettle has finished, steam thinning in the window light. "
    "Rain taps the glass \u2014 not asking, just keeping time \u2014 "
    "and the quiet settles beside you like a cat finding its place."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
