import requests, time, datetime

url = "https://api.bytestobits.dev/speedtext2"

text = requests.get(url).json()

time.sleep(1.5)
print(text)

start = datetime.datetime.now()

while True:
    answer = input("\n")
    if answer == text:
        break
    else:
        print("You made a typo! Try again!")

end = datetime.datetime.now()

wpm = round(((len(text))/5)/((end-start).seconds/60))

print(f"Congratulations! You finished the text in {(end-start).seconds} with {wpm} WPM!")

with open(datetime.datetime.now().strftime("speedtype_record_%m_%d_%Y_%H_%M_%S.txt"), "w+") as f:
    f.write(text + f"\n\nFinished in {(end-start).seconds} seconds with {wpm} WPM!")

input("Press any key to exit!")