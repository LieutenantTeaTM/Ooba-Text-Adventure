# Ooba-Text-Adventure
**Quick and simple 100% AI generated text adventure game using Oobabooga WebUI as a backend.**

## Overview & Reasons for Creation

This is just a simple software toy to play around with. It is essentially just an AI chat but with extra prompts to create a fantasy RPG that is entirely free form and on the spot.

**I created this because:**

- I wanted it to work with Oobabooga WebUI
- I wanted the AI to generate the initial story
- I wanted text streaming like ChatGPT

All examples of this I found either made it needlessly complex, or didn't have all of these features. Also there is a lack of Oobabooga apps and api examples.

### **Here is a quick demo:**

![example](https://github.com/LieutenantTeaTM/Ooba-Text-Adventure/assets/112296448/ffac992e-586e-4792-9916-ed19eddde526)

All of this is generated on the spot by the LLM, including the title and story. And it has memory of the entire chat.


## Install & Setup

Installing is fairly straightforward (most likely).

### **Steps:**
  - **Step 1)** Make sure you have Oobabooga setup and running normally, see [Oobabooga's Text Gen WebUI Github](https://github.com/oobabooga/text-generation-webui)
  - **Step 2)** Find a suitable model. I recommend something that has good chat capabilities and also runs efficiently on your hardware. In my example I was running an RTX 3060 Mobile (6GB VRAM) with this model: [llama2-7b-chat-codeCherryPop-qLoRA-GGUF](https://huggingface.co/TheBloke/llama2-7b-chat-codeCherryPop-qLoRA-GGUF)
  - **Step 3)** Clone this repo anywhere on your local disk. `git clone https://github.com/LieutenantTeaTM/Ooba-Text-Adventure.git`
  - **Step 4)** Enable the openai api extension on Ooba after all requirements have been installed (this does not use the actual OpenAI api but instead mimics it). You can                   do this by clicking session in the WebUI and enabling "openai" then clicking **"apply flags/extensions then restart"**.
  - **Step 5)** Inside **game.py** on **line 7** change:
                ```
                key = 'URL HERE'
                ```
                to the url and port Oobabooga gave you. Replace `URL HERE` with that
            
If you're still having issues with the openai api see Oobabooga's official documentation: [Oobabooga OpenAI Api Docs Github](https://github.com/oobabooga/text-generation-webui/tree/main/extensions/openai)

  - **Step 6)** Open your terminal/CMD in the cloned directory. Run The following commands `pip install -r requirements.txt` and `python game.py` NOTE: You only have to                     install the requirements once.
  - Have fun!

## Features & Known Issues

### Features:
- ChatGPT-like text streaming
- Infinite chats (as long as your GPU can take it)
- 100% AI generated including title and main plot
- The LLM has memory of the previous chat messages
- ASCII titles generated for every generated title

### Known Issues:
- The prompts are not foolproof and the AI still gets confused
- The AI often repeats words or phrases
- The AI will sometimes derail/forget the chat
- Titles are sometimes unreadable
- The titles have nothing to do with the actual game or plot
- Only a fantasy theme, which makes it feel repetitive and lacking sometimes
