🔙 [Voltar para o Início](https://github.com/4L1C3-R4BB1T/desenvolvimento-web "Voltar para o Início")

---

> 1. Utilize o pseudoseletor ```::before``` para adicionar um asterisco (*) antes dos títulos de nível 1.

```css
h1::before {
    content: "* ";
}
```

---

> 2. Aplique o pseudoseletor ```::after``` para adicionar uma linha horizontal após todos os parágrafos.

```css
p::after {
    content: "";
    display: block;
    border-bottom: solid 1px black;
    margin-top: 1em;
}
```

---

> 3. Utilize o pseudoseletor ```::first-letter``` para aumentar a fonte da primeira letra dos parágrafos.

```css
p::first-letter {
    font-size: 2em;
}
```

---

> 4. Aplique o pseudoseletor ```::first-line``` para alterar a cor da primeira linha de todos os parágrafos.

```css
p::first-line {
    color: yellow;
}
```

---

> 5. Use o pseudoseletor ```::marker``` para alterar a cor dos marcadores dos itens de lista para verde.

```css
li::marker {
    color: green;
}
```

---

> 6. Crie um seletor CSS que utilize o pseudoseletor ```[value="10"]``` para aplicar uma cor de fundo aos elementos ```input``` com o valor 10.

```css
input[value="10"] {
    background-color: red;
}
```

---

> 7. Utilize o pseudoseletor ```:first-of-type``` para alterar a cor do texto do primeiro elemento de título ```h2``` em uma página.

```css
h2:first-of-type {
    color: blue;
}
```

---

> 8. Aplique o pseudoseletor ```:last-of-type``` para adicionar uma margem inferior no último elemento de parágrafo de uma página.

```css
p:last-of-type {
    margin-bottom: 10px;
}
```

---

> 9. Utilize o pseudoseletor ```:nth-of-type(3)``` para aplicar um estilo de fonte em negrito no terceiro item de uma lista não ordenada.

```css
ul li:nth-of-type(3) {
    font-weight: bold;
}
```

---

> 10. Aplique o pseudoseletor ```:nth-child(even)``` para alterar a cor de fundo dos itens de lista em posições pares.

```css
li:nth-child(even) {
    background-color: red;
}
```

---

> 11. Utilize o pseudoseletor ```:disabled``` para alterar a cor de fundo dos campos de formulário desabilitados.

```css
input:disabled {
    background-color: lightgray;
}
```

---

> 12. Aplique o pseudoseletor ```:enabled``` para adicionar uma borda aos campos de formulário habilitados.

```css
input:enabled {
    border: solid 1px blue;
}
```

---

> 13. Utilize o pseudoseletor ```:checked``` para alterar a cor dos campos do tipo ```checkbox``` selecionados.

```css
input[type="checkbox"]:checked {
    background-color: green;
}
```

---

> 14. Aplique o pseudoseletor ```:required``` para adicionar uma borda vermelha aos campos de formulário obrigatórios.

```css
input:required {
    border: 1px solid red;
}
```

---

> 15. Utilize o pseudoseletor ```:valid``` para aplicar uma borda verde nos campos de formulário com entrada válida.

```css
input:valid {
    border: 1px solid green;
}
```

---

> 16. Aplique o pseudoseletor ```:invalid``` para adicionar uma borda vermelha nos campos de formulário com entrada inválida.

```css
input:invalid {
    border: 1px solid red;
}
```

---

> 17. Utilize o pseudoseletor ```input[type="email"]``` para alterar a cor do texto dos campos de e-mail.

```css
input[type="email"] {
    color: yellow;
}
```

---

> 18. Aplique o pseudoseletor ```input[type="password"]``` para adicionar uma margem inferior nos campos de senha.

```css
input[type="password"] {
    margin-bottom: 10px;
}
```

---

> 19. Utilize o pseudoseletor ```:focus``` para aplicar uma borda azul aos campos de formulário quando estiverem em foco.

```css
input:focus {
    border: 1px solid blue;
}
```

---

> 20. Aplique o pseudoseletor ```input[type="submit"]``` para alterar a cor de fundo do botão de envio ao passar o mouse.

```css
input[type="submit"]:hover {
    background-color: purple;
}
```
