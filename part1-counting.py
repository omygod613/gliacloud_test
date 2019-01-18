def counting(urls):
    url_dict = dict()
    for url in urls:
        try:
            url_dict[url.split('/')[-1]] += 1
        except:
            url_dict[url.split('/')[-1]] = 1

    url_dict = sorted(url_dict.items(), key=lambda x: x[1], reverse=True)

    urls = ['{} {}'.format(k, v) for k, v in url_dict][:3]
    return '\n'.join(urls)


urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

print(counting(urls))