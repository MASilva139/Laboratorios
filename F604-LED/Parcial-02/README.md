# PARCIAL 02
## Instrucciones:
Para el presente ejercicio de complejos hay que añadir las siguientes funciones:
* Potencia de complejos
```math
Z=(Z_1)^{Z_2}\hspace{10pt};\hspace{30pt} Z_1,Z_2\in \mathbb{C}
```
* Logaritmo natural de complejos
```math
Z=\ln\left(Z_1\right)\hspace{10pt};\hspace{30pt} Z_1\in \mathbb{C}
```
* Seno de complejos
```math
Z=\sin\left(Z_1\right)\hspace{10pt};\hspace{30pt} Z_1\in \mathbb{C}
```
* Coseno de complejos
```math
Z=\cos\left(Z_1\right)\hspace{10pt};\hspace{30pt} Z_1\in \mathbb{C}
```
Debe entregarse en un archivo comprimido (.zip o .tar.gz) con los códigos del archivo de headers (.h), la implementación de las funciones (.c) y un archivo donde se pongan a prueba las funciones implementadas (.c).

* Fecha de entrega: 8/Noviembre - 23:59:00

## Resolución
* Potencia de complejos: Sean los complejos $`Z_1=a+b\cdot i`$, $`Z_2=x+y\cdot i`$; entonces,
```math
Z = Z_1^{Z_2}
\longrightarrow
Z=(a+b\cdot i)^{(x+y\cdot i)}
\longrightarrow
Z = \left(\left| Z_1 \right|e^{i\theta}\right)^{(x+y\cdot i)}
\longrightarrow
Z = \left| Z_1 \right|^{(x+y\cdot i)}e^{i\theta(x+y\cdot i)}
```
a partir de ello
```math
Z = \left| Z_1 \right|^{x}e^{-y\hspace{1pt}\theta}e^{i\left(x\hspace{1pt}\theta+y\cdot\ln\left[Z_1\right]\right)}
```
* Logaritmo de complejos: Sea el complejo $`Z=x+y\cdot i`$; entonces,
```math
Z = \ln\left[\hspace{1pt}x+y\cdot i\hspace{1pt}\right]
\longrightarrow
Z = \ln\left[\hspace{1pt}\left| Z \right|\hspace{1pt}\right] + i\cdot\theta
```
* Seno de complejos: Sea el complejo $`Z=x+y\cdot i`$; entonces,
```math
Z = \sin\left[\hspace{1pt}x+y\cdot i\hspace{1pt}\right]
\longrightarrow
Z = \sin\left[x\right]\cos\left[y\cdot i\right] + \sin\left[y\cdot i\right]\cos\left[x\right]
```
por definición se sabe que $`\sin\left[y\cdot i\right]=i\sinh\left[y\right]`$ y $`\cos\left[y\cdot i\right]=\cos\left[y\right]`$. Por lo tanto,
```math
Z = \sin\left[x\right]\cosh\left[y\right] + i\cdot\sinh\left[y\right]\cos\left[x\right]
```
* Coseno de complejos: Sea el complejo $`Z=x+y\cdot i`$; entonces,
```math
Z = \cos\left[\hspace{1pt}x+y\cdot i\hspace{1pt}\right]
\longrightarrow
Z = \cos\left[x\right]\cos\left[y\cdot i\right] - \sin\left[y\cdot i\right]\sin\left[x\right]
```
por definición se sabe que $`\sin\left[y\cdot i\right]=i\sinh\left[y\right]`$ y $`\cos\left[y\cdot i\right]=\cos\left[y\right]`$. Por lo tanto,
```math
Z = \cos\left[x\right]\cosh\left[y\right] - i\cdot\sinh\left[y\right]\sin\left[x\right]
```