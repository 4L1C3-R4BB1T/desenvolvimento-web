🔙 [Voltar para o Início](https://github.com/4L1C3-R4BB1T/desenvolvimento-web "Voltar para o Início")

---

> 1. Crie um seletor CSS que aplique a propriedade ```display``` com valor ```inline``` nos elementos ```<h1>``` para exibi-los na mesma linha.

```css
h1 {
    display: inline;
}
```

---

> 2. Crie um seletor CSS que utilize a propriedade ```display``` com valor ```block``` nos elementos ```<span>``` para exibi-los como blocos independentes.

```css
span {
    display: block;
}
```

---

> 3. Crie um seletor CSS que aplique a propriedade ```display``` com valor ```inline-block``` nos elementos ```<img>``` para permitir ajustes de margem e preenchimento. 

```css
img {
    display: inline-block;
}
```

---

> 4. Crie um seletor CSS que utilize a propriedade ```display``` com valor ```none``` nos elementos com a classe ```"ocultar"``` para remover ```<div>``` da exibição.

```css
div.ocultar {
    display: none;
}
```

---

> 5. Crie um seletor CSS que aplique a propriedade ```visibility``` com valor ```hidden``` nos elementos com a classe ```"invisível"``` para esconder ```<p>```. 

```css
p.invisivel {
    visibility: hidden;
}
```

---

> 6. Crie um seletor CSS que utilize a propriedade ```visibility``` com valor ```visible``` nos elementos com a classe ```visível"``` para garantir a exibição de ```<p>```.

```css
p.visivel {
    visibility: visible;
}
```

---

> 7. Crie um seletor CSS que aplique a propriedade ```opacity``` com valor 0.5 nos elementos ```<img>``` para deixá-los semitransparentes.

```css
img {
    opacity: 0.5;
}
```

---

> 8. Crie um seletor CSS que utilize a propriedade ```opacity``` com valor 1 nos elementos ```<img>``` ao passar o mouse sobre eles para torná-los totalmente opacos.

```css
img:hover {
    opacity: 1;
}
```

---

> 9. Crie um seletor CSS que aplique a propriedade ```display``` com valor ```none``` nos elementos ```<h2>``` com atributo ```data-hide="true"```.

```css
h2[data-hide="true"] {
    display: none;
}
```

---

> 10. Crie um seletor CSS que aplique a propriedade ```visibility``` com valor ```hidden``` nos elementos ```<p>``` com atributo ```data-visibility="false"```.

```css
p[data-visibility="false"] {
    visibility: hidden;
}
```

---

> 11. Crie um seletor CSS que aplique a propriedade ```position``` com valor ```static``` no elemento ```<div>``` para posicioná-lo na ordem normal do fluxo.

```css
div {
    position: static;
}
```

---

> 12. Crie um seletor CSS que utilize a propriedade ```position``` com valor ```relative``` no elemento ```<img>``` para movê-lo em relação à sua posição original.

```css
img {
    position: relative;
}
```

---

> 13. Crie um seletor CSS que aplique a propriedade ```position``` com valor ```absolute``` no elemento ```<p>``` para posicioná-lo em relação ao seu ancestral mais próximo posicionado.

```css
p {
    position: absolute;
}
```

---

> 14. Crie um seletor CSS que utilize a propriedade ```position``` com valor ```fixed``` no elemento ```<nav>``` para fixá-lo na janela do navegador.

```css
nav {
    position: fixed;
}
```

---

> 15. Crie um seletor CSS que aplique a propriedade ```position``` com valor ```sticky``` no elemento ```<header>``` para mantê-lo fixo durante a rolagem.

```css
header {
    position: sticky;
}
```

---

> 16. Crie um seletor CSS que utilize as propriedades ```top``` e ```left``` com valores em pixels para posicionar o elemento ```<div>``` com ```position: relative```. 

```css
div {
    position: relative;
    top: 0;
    left: 10px;
}
```

---

> 17. Crie um seletor CSS que aplique as propriedades ```bottom``` e ```right``` com valores em porcentagem para posicionar o elemento ```<p>``` com ```position: absolute```.

```css
p {
    position: absolute;
    bottom: 5%;
    right: 10%;
}
```

---

> 18. Crie um seletor CSS que utilize a propriedade ```z-index``` para controlar a ordem de empilhamento do elemento ```<img>``` em relação aos elementos adjacentes.

```css
img {
    position: absolute;
    z-index: 3;
}
```

---

> 19. Crie um seletor CSS que aplique a propriedade ```z-index``` com valor maior nos elementos ```<button>``` para mantê-los acima dos outros elementos.

```css
button {
    position: absolute;
    z-index: 99;
}
```

---

> 20. Crie um seletor CSS que utilize a propriedade ```z-index``` com valor negativo no elemento ```<div>``` para posicioná-lo abaixo dos elementos com valor ```z-index``` padrão.

```css
div {
    position: absolute;
    z-index: -1;
}
```

---

> 21. Crie um elemento ```div``` com o conteúdo transbordando verticalmente. Utilize a propriedade ```overflow-y``` para adicionar uma barra de rolagem vertical.

```css
div {
    overflow-y: scroll;
}
```

---

> 22. Explique a diferença entre os valores ```visible```, ```hidden```, ```scroll``` e ```auto``` para a propriedade ```overflow```.

- **visible**: é o valor padrão. Se o conteúdo exceder o tamanho do elemento, ele será exibido normalmente, podendo invadir o espaço de outros elementos adjacentes.

- **hidden**: caso o conteúdo exceda o tamanho do elemento, ele será ocultado e não haverá barras de rolagem.

- **scroll**: significa que, caso o conteúdo exceda o tamanho da div, barras de rolagem serão habilitadas, permitindo que o usuário visualize todo o conteúdo.

- **auto**: semelhante ao scroll, mas as barras de rolagem só serão exibidas se o conteúdo realmente exceder o tamanho do elemento.

---

> 23. Descreva um cenário prático em que seria útil aplicar a propriedade ```float``` com o valor ```left```.

Uma área de exibição de propagandas em um site ou um menu lateral.

---

> 24. Crie uma galeria de imagens utilizando a propriedade ```float``` para organizar as imagens lado a lado, e aplique o valor ```clear``` apropriado para evitar sobreposição com outros elementos da página.

---

> 25. Explique a diferença entre os valores ```left```, ```right```, ```both``` e ```none``` para a propriedade ```clear```, e como eles afetam elementos adjacentes a elementos flutuantes.

- **left**: posiciona os elementos subsequentes à esquerda.

- **right**: posiciona os elementos subsequentes à direita.

- **both**: posiciona os elementos subsequentes somente após todos os elementos flutuantes.

- **none**: posiciona os elementos subsequentes tanto à esquerda quanto direita.

---

> 26. Crie dois elementos ```div``` com largura, altura, margem interna e borda definidos. Aplique a propriedade ```box-sizing``` com o valor ```border-box``` em um deles e ```content-box``` no outro. Descreva a diferença no tamanho total dos elementos.

Quando o valor é content-box, a largura e altura especificadas se aplicam apenas ao conteúdo do elemento, sem incluir bordas, margens internas e externas.

Quando o valor é border-box, a largura e altura especificadas incluem o conteúdo, bordas e margens internas, mas não as margens externas.

---

> 27. Explique como a propriedade ```overflow``` afeta a aparência de um elemento com conteúdo transbordando, e como isso pode ser útil ao criar leiautes responsivos.

A propriedade overflow controla o que acontece quando o conteúdo de um elemento excede seu tamanho especificado, seja em largura ou altura.

Isso pode ser útil quando se precisa criar elementos com alturas e larguras específicas, não importando o tamanho do conteúdo.

---

> 28. Utilize a propriedade ```float``` para criar um leiaute de duas colunas, com uma coluna à esquerda para o menu de navegação e outra à direita para o conteúdo principal.

---

> 29. Crie um exemplo que demonstre o uso de ```overflow-x``` e ```overflow-y``` em conjunto para controlar o transbordo de conteúdo em ambas as direções (horizontal e vertical).

---

> 30. Descreva um cenário em que seria útil usar a propriedade ```box-sizing``` com o valor ```border-box``` para criar um leiaute flexível e adaptável.

Seria útil utilizar box-sizing como border-box no caso em que fosse necessário garantir que os elementos continuassem com a largura e altura definidos, mesmo possuindo a necessidade de se aplicar margens internas e/ou externas.

É especialmente útil quando se está trabalhando com elementos que possuem largura e altura fixas, como imagens e vídeos. 