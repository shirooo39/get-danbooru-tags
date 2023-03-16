# Get Danbooru Tags
This is just a simple Python script that I wrote quickly to grab tags from Danbooru of an existing or already uploaded images on the platform by using the ```requests``` module.

## How to use
It's actually quite simple.
BUT as I have not yet added an argument to the script, you will have to edit the script every time you want to use it (it'll be a lot more easier to use once I added argument support, but that's for another day. My use-case for now has been fulfilled).
- Make sure you have Python installed first and the PATH is also added (should work on Python 3.5 to newer, I'm on 3.11 if I recall correctly)
- Download the script
- Edit the script with any text editor you want and replace ```image_id = ''``` with the Image ID from danbooru.  
  Let's say I found this image of my beautiful vtuber waifu from [danbooru.donmai.us/posts/```6135741```?q=hoshimachi_suisei+]  
  What you want from the URL is the highlighted numbers. Copy that and paste it into the ```image_id = ''```
- Open up CMD and just type-in the command below, then you hit ENTER
- ```python danboorutags.py```  
  If you get an error that says ```module requests not found``` or something, chance is you might need to install the ```requests``` module first.  
  Run ```pip install requests``` and then reopen your CMD, then it should work.

You should see this on your CMD. If you don't see anything or an error, then you might be doing it wrong, or just open up an issue to let me know (can't promise I'd be any helpful, but I'll try).
![image](https://user-images.githubusercontent.com/38461122/225559668-b58af4eb-6bec-469d-9b17-e909f9ce1b58.png)

Q: What is that ```prompt``` thing on the bottom?  
A: I wrote this script so I can grab the tags of an uploaded image on danbooru easily and then throw them altogether into a Stable Diffusion prompt (it might not look like a good prompt, but could be useful as a starting point).

Q: Does this work on Linux/Windows?  
A: I wrote this on Windows but should work on Linux too, as there are no OS-specific command in the script other than ```cls``` and ```clear```.
