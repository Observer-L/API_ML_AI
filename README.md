# Meme generator in Python with Face Detection
![showcase](showcase/showcase1.png)

## what is Carzy Pandaman
Pandaman is one of the most popular memes in China.  
...  
[click here for PRD](https://github.com/Observer-L/API_ML_AI/blob/master/PRD.md)

## what you can do
you can use any static image with face and text as input, the APP will automatically generate a crazy pandaman meme for you!

## The Tools of Face Detection and APIs
I use Dlib’s get_frontal_face_detector, along with the 68 point shape prediction model.
and use BaiduAI's censor APIs for user's input(both image and text)

## Architecture of Automatic Meme Generator
![showcase](showcase/showcase3.png)
The architecture of the application is fairly straightforward.   
...

## Where To Go From Here
We’ve successfully built the very first part in a program that could be used as an API to generate memes automatically.  
By hooking up our program to something like Flask, we could display a web page allowing for users to upload their own images, and get back fully complete memes.  
With something like youtube-dl, we could have users paste in YouTube url videos to automatically generate memes.  
In case you missed it, the code is available at Github.
