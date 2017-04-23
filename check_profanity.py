def read_text():
    quotes = open("/home/aarti/Downloads/MOCK_DATA.csv")
    contents = quotes.read()
    print(contents)
    quotes.close()

read_text()