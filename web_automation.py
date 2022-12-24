import webbrowser as wb

def web_auto():
    # web_path = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
    web_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

    URLS = (
        "https://google.com",
        "https://youtube.com",
        "https://github.com/lexiscode"
    )
    for url in URLS:
        print("Opening " + url)
        wb.get(web_path).open(url)

web_auto()
