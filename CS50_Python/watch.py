import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = (
        r"^<iframe (width=\"[0-9]+\" )?"
        r"(height=\"[0-9]+\" )?"
        r"src=\"(https|http)://(www.)?youtube.com/embed/(\w+)\""
        r"( title=\"YouTube video player\" frameborder=\"[0-9]+\""
        r" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\""
        r" allowfullscreen)?></iframe>$"
    )
    #if HTML := re.search(r"^<iframe (width=\"[0-9]+\" )?(height=\"[0-9]+\" )?src=\"(https|http)://(www.)?youtube.com/embed/(\w+)\"( title=\"YouTube video player\" frameborder=\"[0-9]+\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen)?></iframe>$", s):
    if HTML := re.search(pattern, s):
        return f"https://youtu.be/{HTML.group(5)}"


if __name__ == "__main__":
    main()
