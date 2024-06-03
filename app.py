import streamlit as st
import pickle
from PIL import Image

def main () :

    st.title("Social Media Usage and Emotional Well-Being !!:performing_arts:")
    image=Image.open("image.png")
    st.image(image,width=700)

    st.caption("Put your details here for your Emotional state :full_moon_with_face:")

    age=st.text_input("Age :innocent:","type here")
    gender=st.radio("Gender :speaking_head_in_silhouette:",["Male","Female","Non-Binary"])

    if gender=="Male" :

        gender2=1

    elif gender=="Female" :

        gender2=0

    else :

        gender2=2

    platform=st.radio("Platform :selfie:",["Instagram","Twitter","Facebook","LinkdIn","Whatsapp","Telegram","Snapchat"])

    if platform=="Instagram" :

        platform2=1
    elif platform=="Twitter" :

        platform2=5
    elif platform == "Facebook":

        platform2 = 0
    elif platform == "LinkdIn":

        platform2 = 2
    elif platform == "Whatsapp":

        platform2 = 6
    elif platform == "Telegram":

        platform2 = 4
    elif platform == "Snapchat":

        platform2 = 3

    usage=st.text_input("Daily Usage in Minutes :1234:","type here")
    posts=st.text_input("Posts Per Day :frame_with_picture:","type here")
    likes=st.text_input("Likes received :heart:","type here")
    comments=st.text_input("Comments received :thought_balloon:","type here")
    messages=st.text_input("Messages sends :email:","type here")

    input=[age,gender2,platform2,usage,posts,likes,comments,messages]

    model=pickle.load(open("emotion detection model","rb"))
    scaler=pickle.load(open("emotion scaler","rb"))
    encoder=pickle.load(open("encoder model","rb"))

    predicts=st.button("Get the Emotional State of Yours!!! :sparkles:")

    st.caption("Your State!!! :first_quarter_moon_with_face:")

    if predicts :

        prediction=model.predict(scaler.transform([input]))

        prediction2=encoder.inverse_transform(prediction)

        st.write(":bookmark: By your details of usage in",platform," :iphone:, I think you are in :grinning:",prediction2)

        if prediction2=="Happiness" :

            happy=Image.open("happiness.jpg")
            st.image(happy,width=560)
            st.caption("Happiness :grin:")

        elif prediction2=="Neutral" :

            happy=Image.open("neutral.webp")
            st.image(happy,width=560)
            st.caption("Neutral :slightly_smiling_face:")

        elif prediction2=="Anxiety" :

            happy=Image.open("anxiety.jpg")
            st.image(happy,width=560)
            st.caption("Anxiety :confounded:")

        elif prediction2=="Sadness" :

            happy=Image.open("sadness.jpg")
            st.image(happy,width=560)
            st.caption("Sadness :disappointed:")

        elif prediction2=="Boredom" :

            happy=Image.open("boredom.png")
            st.image(happy,width=560)
            st.caption("Boredom :unamused:")

        elif prediction2=="Anger" :

            happy=Image.open("anger.webp")
            st.image(happy,width=560)
            st.caption("Anger :rage:")
main()