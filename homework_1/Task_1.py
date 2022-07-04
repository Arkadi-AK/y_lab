def domain_name(url: str):
    """Outputs the domain name from the url:"""
    dom = url.split('//')[-1].split("www.")
    if len(dom) > 1:
        domain = dom[-1].split(".")[0]
    else:
        domain = dom[-1].split(".")[0]
    return domain


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name("www.zombie-bites.com") == "zombie-bites"
assert domain_name("https://www.cnet.com") == "cnet"
assert domain_name('google.com') == "google"
