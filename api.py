from keys import API_Key

key = API_Key

import os
import openai
openai.api_key = key
openai.Model.list()

openai.Image.create(
  prompt=input("Qual imagem deseja criar? "),
  n=int(input("Quantas imagens deseja criar? ")),
  size="1024x1024"
)