![cover_image](https://user-images.githubusercontent.com/57211163/124975888-2eaa9680-e04c-11eb-99fb-fbe176b1a1bd.png)
# Xtinguish : Detecting Wildfires using CNNs

**Xtinguish** is an CNN Image Classfication model which helps in detecting and preventing **Wildfires**.

## What it does ?

**Xtinguish** takes an image as a input and detects if there's a possible Fire or Smoke in it. 

Taking advantage of [**`OpenWeatherAPI`**](https://openweathermap.org), **Xtinguish** outputs the **Weather Data** based on your location.

**Xtinguish** also attempts to predict the **Fire Intensity** based on the image.

> **How is Xtinguish, different from other Image Classifiers ?**

At the time of writing, no other Model out there performs all the above mentioned tasks at one spot. 

## How was it built ?

Leveraging on power of **Transfer Learning**, **Xtinguish** adapts the architecture and weights of a pre-built Convultional Neural Network Model, **`EfficientNetB0`** which was initially trained on the infamous **[`ImageNET`](https://www.image-net.org)** dataset.

![cropped-Wildfires-and-Climate-Change-2000x834](https://user-images.githubusercontent.com/57211163/125040260-0efb8880-e0b5-11eb-8b12-b139af1adf1f.png)

Further trained on custom datasets, it classifies a given image into `No Fire`, `Fire`

On being tested on various images and video footages, **Xtinguish** acheived a high accuracy of **`98%`**.

![performance](https://user-images.githubusercontent.com/57211163/125053364-a4514980-e0c2-11eb-832c-8b8bbb0e3ca2.png)

![hhhh](https://user-images.githubusercontent.com/57211163/125050221-6868b500-e0bf-11eb-8169-1abdea1820c1.png)





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
