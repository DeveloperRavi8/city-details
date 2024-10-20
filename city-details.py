from tkinter import *
import requests
import json

root = Tk()
root.configure(background="green")
root.title("City Details")
root.geometry("500x500")



def city_details():
    capital_name = capital_name_entry.get()
    print("https://restcountries.com/v2/capital/"+ capital_name)
    response = requests.get("https://restcountries.com/v2/capital/"+ capital_name)
    data = json.loads(response.content)
    print(response.content)
    if(response.status_code == 404):
        print("Country not found")
    else:
        country_name = data[0]['name']
        region = data[0]['region']
        lang = data[0]['languages'][0]['name']
        population = data[0]['population']
        area = data[0]['area']

        country_name_label['text'] = "Country : " + country_name
        region_label['text'] = "Region : " + region
        lang_label['text'] = "Language : " + lang
        population_label['text'] = "Population : " + str(population)
        area_label['text'] = "Area : " + str(area)
        

label = Label(root, text="Capital City Name", fg="white", bg="green", font=("Arial", 15, "bold"))
label.pack(pady=10)

capital_name_entry = Entry(root)
capital_name_entry.pack(pady=10)

button = Button(root, text="City Details", command=city_details, relief=FLAT, fg="black", bg="yellow")
button.pack(pady=10)

country_name_label = Label(root, text="Country : ", fg="white", bg="green")
country_name_label.pack(pady=10)

region_label = Label(root, text="Region : ", fg="white", bg="green")
region_label.pack(pady=10)

lang_label = Label(root, text="Language : ", fg="white", bg="green")
lang_label.pack(pady=10)

population_label = Label(root, text="Population : ", fg="white", bg="green")
population_label.pack(pady=10)

area_label = Label(root, text="Area : ", fg="white", bg="green")
area_label.pack(pady=10)

root.mainloop()