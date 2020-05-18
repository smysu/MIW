def funkcja(data_text):
    data = {
        "length": len(data_text),
        "letters": [key for key in data_text],
        "big_letters": data_text.upper(),
        "small_letters": data_text.lower()
    }
    return data


a = "kanapka"
print(funkcja(a))
