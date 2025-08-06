months_to_numbers = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}
numbers_to_zero_padded = {
    "1": "01",
    "2": "02",
    "3": "03",
    "4": "04",
    "5": "05",
    "6": "06",
    "7": "07",
    "8": "08",
    "9": "09",
    "10": "10",
    "11": "11",
    "12": "12",
    "13": "13",
    "14": "14",
    "15": "15",
    "16": "16",
    "17": "17",
    "18": "18",
    "19": "19",
    "20": "20",
    "21": "21",
    "22": "22",
    "23": "23",
    "24": "24",
    "25": "25",
    "26": "26",
    "27": "27",
    "28": "28",
    "29": "29",
    "30": "30",
    "31": "31"
}



while True:
    user = input("Date: ")
    user = user.split()
    if user[0].title() in months_to_numbers and int(user[1].replace(",", "")) <32 and "," in user[1] :
       user[0] = user[0].title()
       user[1] = user[1].replace(",", "")
       print(f"{user[2]}-{months_to_numbers[user[0]]}-{numbers_to_zero_padded[user[1]]}")
       break
    elif "/" in user[0]:
        user = user[0].split("/")
        if int(user[0]) > 12 or int(user[1])>31:
            continue
        print(f"{user[2]}-{numbers_to_zero_padded[user[0]]}-{numbers_to_zero_padded[user[1]]}")
        break