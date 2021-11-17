import tkinter as tk
import requests
from PIL import Image, ImageTk

# HEIGHT , WIDTH OF THE SCREEN
ht = 690
wt = 1000

screen = tk.Tk()  # main window

tk.Canvas(screen, height=ht, width=wt, bg='darkblue').pack()

# ADDING BACKGROUND IMAGE TO THE SCREEN
path = "./bgr.jpg"
bgr_img = ImageTk.PhotoImage(Image.open(path))

bgr_label = tk.Label(screen, image=bgr_img)
bgr_label.place(relwidth=1, relheight=1)

# FOR SEARCHING DATA
upr_frame = tk.Frame(screen, bg="darkblue", bd=5)
upr_frame.place(relx=0.5, rely=0.1, relwidth=0.85, relheight=0.1, anchor='n')

# GET CITY NAME
input_box = tk.Entry(upr_frame, font=('Cambria', 18))
input_box.place(relwidth=0.75, relheight=1)

sub_button = tk.Button(upr_frame, text="Get Weather", font=('Cambria', 18), bg='orange',
                       command=lambda: get_weather(input_box.get()))
sub_button.place(relx=0.8, relwidth=0.2, relheight=1)

# FOR SHOWING DATA
lwr_frame = tk.Frame(screen, bg='darkblue', bd=5)
lwr_frame.place(relx=0.5, rely=0.3, relwidth=0.85, relheight=0.55, anchor='n')

data = tk.Label(lwr_frame, font=('Cambria', 20), bg='white', anchor='nw', justify='left', bd=5)
data.place(relwidth=1, relheight=1)

# SHOW IMAGE BASED ON CONDITIONS
weather_icon = tk.Canvas(data, bg='white', highlightthickness=0)
weather_icon.place(relx=0.55, rely=0, relwidth=1, relheight=1)


# FUNCTION TO GET DATA FROM OPEN WEATHER MAP API
def get_weather(city):
    weather_api_key = '56aeaa0feb88b770c7fc1d4890edb194'  # OpenWeatherMap api key
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_api_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params)
    weather_data = response.json()
    # print(weather_data)
    try:
        name = weather_data['name']
        desc = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (F): %s' % (name, desc, temp)

    except:
        final_str = ":( Climate info not available"

    data['text'] = final_str
    get_image(desc, temp)


# FUNCTION TO SHOW IMAGE AND TEXT BASED ON DESCRIPTION OF WEATHER DATA
def get_image(desc, temp):
    if temp < 10 or desc in ['snow', 'light snow', 'heavy snow', 'sleet', 'light shower sleet', 'shower snow',
                             'light rain and snow', 'rain and snow', 'light shower snow', 'heavy shower snow']:
        icon = 'frost.jpg'
        data['text'] += '\n\n\nLets make ☃'

    elif desc in ['mist', 'smoke', 'haze', 'fog', 'sand', 'dust', 'volcanic ash', 'squalls', 'tornado']:
        icon = 'fog.png'
        data['text'] += '\n\n\nBetter to be at Home ☁'

    elif desc in ['shower rain', 'rain', 'heavy intensity shower rain', 'freezing rain', 'ragged shower rain',
                  'extreme rain', 'very heavy rain', 'heavy intensity rain', 'light rain', 'drizzle rain', 'drizzle']:
        icon = 'rain.jpg'
        data['text'] += '\n\n\nTime for some tea and sandwich, Its a ☔ Day'

    elif desc in ['broken clouds', 'overcast clouds', 'scattered clouds']:
        icon = 'cloudy.jpg'
        data['text'] += '\n\n\nBring a ☔ just in case '

    elif desc == 'clear sky':
        icon = 'sunny.png'
        data['text'] += '\n\n\nIt\'s  icecream time ☀'

    elif desc == 'few clouds':
        icon = 'sunny_cloudy.png'
        data['text'] += '\n\n\nNice day to go for a walk ☀☁'

    elif desc in ['thunderstorm', 'thunderstorm with light rain', 'thunderstorm with rain',
                  'thunderstorm with heavy rain', 'light thunderstorm', 'heavy thunderstorm', 'ragged thunderstorm',
                  'thunderstorm with light drizzle', 'thunderstorm with drizzle', 'thunderstorm with heavy drizzle']:
        icon = 'thunder.jpg'
        data['text'] += '\n\n\nNot a good day to go outside ☁⚡ϟ ☔'

    else:
        icon = 'landscape.png'

    # RESIZING IMAGE
    size = int(lwr_frame.winfo_height() * 1)
    img = ImageTk.PhotoImage(Image.open('./icons/' + icon).resize((size, size)))

    # DELETING ICON IF ANY FROM THE SCREEN
    weather_icon.delete("all")

    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


# print(tk.font.families())
screen.mainloop()
