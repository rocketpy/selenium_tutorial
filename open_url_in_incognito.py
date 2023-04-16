import webbrowser

url = 'www.blablabla.com'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
webbrowser.get(chrome_path).open_new(url)
