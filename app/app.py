import streamlit as st
import tensorflow as tf
import tempfile

import requests
from weather import get_weather, get_time
from intensity import get_pixel_count, find_intensity

def predicting(image, model):
    image = load_and_prep(image)
    image = tf.cast(tf.expand_dims(image, axis=0), tf.int16)
    preds = model.predict(image)
    pred_class = class_names[tf.round(int(preds[0]))]
    return pred_class

def load_and_prep(image, shape=224, scale=False):
    image = tf.image.decode_image(image, channels=3)
    image = tf.image.resize(image, size=([shape, shape]))
    if scale:
        image = image / 255.
    return image


def weather_bar():
    loc, weather, temp, hum, wind_dir, wind_speed = get_weather(OP_API_KEY)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Temperature", f"{temp} K")
    col2.metric("Humidity", f"{hum} %")
    col3.metric("Wind Direction", f"{wind_dir}°")
    col4.metric("Wind Speed", f"{wind_speed} m/s")

class_names = ['Fire', 'No Fire']
st.set_page_config(page_title="Xtinguish")
OP_API_KEY = st.secrets("KEY")

st.title("Xtinguish")
st.write("**Xtinguish** is an CNN Image Classfication model which helps in detecting and preventing Wildfires.")
st.write("""
1. Detects if there's a possible Fire or Smoke in it. 
2. Taking advantage of [**`OpenWeatherAPI`**](https://openweathermap.org), 
it outputs the **Weather Data** based on your location.
3. **Xtinguish** also attempts to predict the **Fire Intensity** based on the image.
        """)
st.write("> To know more about this app, visit [**GitHub Repo**](https://github.com/gauravreddy08/Xtinguish)")

model = tf.keras.models.load_model("./models/baseline_model.hdf5")

file = st.file_uploader(label="Upload an Image.",
                        type=['jpg', 'jpeg', 'png'])

if not file:
    st.warning("Please upload the file.")
    st.stop()
else:
    image = file.read()
    st.image(image, use_column_width=True)
    pred_button = st.button("Predict")

if pred_button:
    pred = predicting(image, model)
    st.success(f"**Prediction :** {pred}")
    weather_bar()
    if pred=="Fire":
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(image)
        count = get_pixel_count(tfile.name)
        time = get_time(OP_API_KEY)
        i = find_intensity(count, time)
        st.success(f"""
                **Time :** {time}

                **Fire Intensity :** {i}
                            """)
