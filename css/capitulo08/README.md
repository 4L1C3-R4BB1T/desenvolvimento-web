🔙 [Voltar para o Início](https://github.com/4L1C3-R4BB1T/desenvolvimento-web "Voltar para o Início")

---

> 1. Associe a um documento HTML qualquer o código CSS para que todos os parágrafos tenham fonte de tamanho 18px utilizando as três formas de associação de código CSS a documentos HTML: inline (atributo style), interno (elemento ```<style>```) e externo (arquivo CSS).

- **Inline**

```html
<p style="font-size: 18px;">
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
</p>
```

- **Interno**

```html
<head>
    ...
    <style>
        p {
            font-size: 18px;
        }
    </style>
</head>
```

- **Externo**

```html
<head>
    ...
    <link rel="stylesheet" href="style.css">
</head>
```

```css
/* style.css */
p {
    font-size: 18px;
}
```

---

> 2. Crie um seletor CSS para o elemento HTML ```<h1>``` utilizando o seletor de tipo de elemento.

```css
h1 { ... }
```

---

> 3. Crie um seletor CSS para o elemento HTML com o ```ID titulo``` utilizando o seletor por ID.

```css
#titulo { ... }
```

---

> 4. Crie um seletor CSS para todos os elementos HTML da classe ```destaque``` utilizando o seletor por classe.

```css
.destaque { ... }
```

---

> 5. Crie um seletor CSS para os elementos HTML do tipo ```<p>``` dentro de um elemento da classe ```container``` utilizando o seletor de descendência.

```css
.container p { ... }
```

---

> 6. Crie um seletor CSS para todos os elementos HTML do tipo ```<a>``` da classe ```link``` utilizando o seletor de combinação ```tipo.classe```.

```css
a.link { ... }
```

---

> 7. Crie um seletor CSS para todos os elementos HTML do tipo ```<ul>``` da classe ```lista``` utilizando o seletor de combinação ```tipo.classe```.

```css
ul.lista { ... } 
```

---

> 8. Crie um seletor CSS para todos os elementos HTML do tipo ```<li>``` que estão dentro de um elemento com a classe ```lista``` utilizando o seletor de descendência.

```css
.lista li { ... }
```

---

> 9. Defina uma cor de fundo verde para todos os elementos ```<p>``` do documento.

```css
p {
    background-color: green;
}
```

---

> 10. Defina uma fonte em negrito para o elemento ```<h2>``` com o ```ID titulo```.

```css
#titulo {
    font-weight: bold;
}
```

---

> 11. Defina uma cor de fundo amarela para todos os elementos com a classe ```destaque```.

```css
.destaque {
    background-color: yellow;
}
```

---

> 12. Defina uma margem de 10 pixels para todos os elementos ```<div>``` descendentes de um elemento da classe ```container```. 

```css
.container div {
    margin: 10px;
}
```

---

> 13. Defina uma cor de texto azul para todos os elementos ```<a>``` da classe ```link```.

```css
a.link {
    color: blue;
}
```

---

> 14. Defina uma cor de fundo cinza para todos os elementos ```<ul>``` da classe ```lista```. 

```css
ul.lista {
    background-color: gray;
}
```

---

> 15. Defina um tamanho de fonte de 14 pixels para todos os elementos ```<li>``` que estão dentro de um elemento da classe ```lista```. 

```css
.lista li {
    font-size: 14px;
}
```

---

> 16. Selecione todos os elementos ```<h1>``` e defina um tamanho de fonte de 24 pixels para eles.

```css
h1 {
    font-size: 24px;
}
```

---

> 17. Selecione todos os elementos com a classe ```negrito``` e defina um estilo de fonte em negrito para eles.

```css
.negrito {
    font-weight: bold;
}
```

---

> 18. Selecione todos os elementos ```<p>``` que estão dentro de um elemento com o ```ID conteudo``` e defina uma cor de texto vermelha para eles.

```css
#conteudo p {
    color: red;
}
```

---

> 19. Selecione todos os elementos ```<img>``` que estão dentro de um elemento com a classe ```galeria``` e defina uma largura de 200 pixels para eles.

```css
.galeria img {
    width: 200px;
}
```
