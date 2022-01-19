import cv2

imagem1 = cv2.imread('teste/1.png')
imagem2 = cv2.imread('teste/5.png')
imagem3 = cv2.imread('teste/9.png')

classificador1 = cv2.CascadeClassifier(
    'negativas/classificador/cascades/cascade-stage8.xml')
#classificador2 = cv2.CascadeClassifier('cascade_caneca2.xml')
#classificador3 = cv2.CascadeClassifier('cascade_caneca3.xml')

imagemcinza1 = cv2.cvtColor(imagem1, cv2.COLOR_BGR2GRAY)
imagemcinza2 = cv2.cvtColor(imagem2, cv2.COLOR_BGR2GRAY)
imagemcinza3 = cv2.cvtColor(imagem3, cv2.COLOR_BGR2GRAY)

deteccoes1 = classificador1.detectMultiScale(
    imagemcinza1, scaleFactor=1.4, minNeighbors=21)
deteccoes2 = classificador1.detectMultiScale(
    imagemcinza2, scaleFactor=1.4, minNeighbors=21)
deteccoes3 = classificador1.detectMultiScale(
    imagemcinza3, scaleFactor=1.4, minNeighbors=21)

for (x, y, l, a) in deteccoes1:
    cv2.rectangle(imagem1, (x, y), (x + l, y + a), (0, 255, 0), 2)

for (x, y, l, a) in deteccoes2:
    cv2.rectangle(imagem2, (x, y), (x + l, y + a), (0, 255, 0), 2)

for (x, y, l, a) in deteccoes3:
    cv2.rectangle(imagem3, (x, y), (x + l, y + a), (0, 255, 0), 2)

cv2.imshow('Classificador 1', imagem1)
cv2.imshow('Classificador 2', imagem2)
cv2.imshow('Classificador 3', imagem3)


cv2.waitKey(0)
cv2.destroyAllWindows()
