def funkcja(text, letter):
    if letter in text:
        text = text.replace(letter, "")
    return text


a = "Stwórz funkcję, która przyjmie jako parametry text oraz letter, " \
    "a następnie zwróci wynik usunięcia wszystkich wystąpień wartości w " \
    "letter z tekstu text "
print(funkcja(a, "a"))
