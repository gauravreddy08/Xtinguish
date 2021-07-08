[image](https://user-images.githubusercontent.com/57211163/123479724-facc7b80-d61e-11eb-82d6-5018c7c0c573.png)
# Xtinguish : Preventing Wildfires using CNNs

**Xtinguish** is an CNN Image Classfication model which helps in detecting and preventing **Wildfires**.

## What it does ?

**Xtinguish** takes image as an input and detects if there's a Possible Wildfire with an accuracy of **`95%`**. 

And also leveraging on [**`OpenWeatherAPI`**](https://openweathermap.org), it outputs the **Weather Data** based on your location.

Xtinguish also attempts to predict the **Fire Intensity** in the image.

> **How is Xtinguish, different from other Image Classifiers ?**

At the time of writing, no other Model out there does all the above mentioned tasks at one spot. 

## How was it built ?

**Xtinguish** takes advantage of a pre-built Convultional Neural Network Model, **`EfficientNetB0`**, using **Transfer Learning**.

Further trained on custom datasets, it classifies a given image into `No Fire`, `Fire`






## How can I test it?

Finally after training the model, I have exported it as `.hdf5` files and then integrated it with **Streamlit Web App**. 


### To view the Deployed app, [Click here](https://share.streamlit.io/gauravreddy08/xtinguish/main/app/app.py)

> The app may take a couple of seconds to load for the first time, but it works perfectly fine.

Once an app is loaded, 

1. Upload an image.

2. Once the image is processed, **`Predict`** button appears. Click it.

3. Once you click the **`Predict`** button, the model prediction takes place and the output will be displayed.

4. And voilà, there you go.
----
   

> **Model Used :** **`EfficientNetB0`**
> 
> **Accuracy :** **`95%`**
