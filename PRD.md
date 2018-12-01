# Product requirements

|         |            |
| ------------- |:-------------:|
| Target release      | 1.0 |
| Epic      |  Pandaman Meme Generator      |
| Document status | Draft      |
| Designer      | Observer-L |
| Developer      | Observer-L      |
| QA | Observer-L      |

## Goals
* Our goal is to create a automatic pandaman generator that allows you to add custom text and image to make your own pandaman memes.
* Sometimes users see a interesting meme and want to be able to make a custom meme.

## Background and strategic fit
We all know meme is usually used in every social platforms. 
However, Most of our users get memes from third party or make memes by some PS APPs, which limit creativity and waste time, so this is something we need to solve.
We will be able to make our own memes through the automatic pandaman generator with creativity!

### Customer research
* ...

## Assumptions
### How can I customize my meme?
* You can use the generator to add text captions to established memes or upload your own images as templates.
* You can move and resize the text boxes by dragging them around.
* You can customize the font color, outline color, and outline width just to the right of where you type your text.
* You can further customize the font and add additional text boxes in the More Options section.
### Why is there an "created by crazy pandaman webapp" watermark on my memes? 
* The watermark helps other people find where the meme was created, so they can make memes too! 
* However, if you'd really like to, you can remove our watermark from all images you create.


## Requirements
|    #     |    Title     |       User story     |      Importance     |      Notes     |
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
| 1      |Fight with memes      | user wanna spoof friends with memes | Must Have |  |
| 1      |Interesting things and people     | things and people make you feel so interesting that want to make memes | Must Have |  |

## User interaction and design
#### Flow Chart
![showcase](showcase/showcase3.png)
The architecture of the application is fairly straightforward.   
...

#### User interaction and design
![showcase](showcase/showcase2.png)

## Questions
|    Question     |       Outcome     |
| ------------- |:-------------:|
| image and text may include potentially sensitive content      |  That's what Baidu's image & text censoring APIs need to figure out   |


## Not doing
* provides both free(watermark) and paid features to users
* supports all web fonts and Windows/Mac fonts including bold and italic, if they are installed on your device. Note that Android and other mobile operating systems may support fewer fonts.
* We’ve successfully built the very first part in a program that could be used as an API to generate memes automatically.
By hooking up our program to something like Flask, we could display a web page allowing for users to upload their own images, and get back fully complete memes.  
