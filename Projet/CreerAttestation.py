from PIL import Image , ImageDraw, ImageFont




nom = input("Quel est le nom de l'étudiant ?")
prenom = input("Quel est le prenom de l'étudiant ?")
mail = input("Quel est le mail de l'étudiant ?")



img = Image.open('img/Attestation.png')
fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 100)

imgDraw = ImageDraw.Draw(img)
imgDraw.multiline_text((350,400),"Certificat délivré\n        à\n"+nom+" "+prenom+"", font= fnt, fill=(0,0,0))
img.show()
img.save('img/Certificat'+nom+prenom+'.png')

