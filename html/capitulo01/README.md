🔙 [Voltar para o Início](https://github.com/4L1C3-R4BB1T/desenvolvimento-web "Voltar para o Início")

---

> 1. Quais são os 3 tipos de códigos básicos de uma página de hipertexto? Explique para que serve cada um dos tipos.
 
- **HTML:** sigla para HyperText Markup Language. É uma linguagem de marcação, sendo responsável por definir quais elementos serão exibidos em uma determinada página.

- **CSS:** sigla para Cascading Style Sheets. É uma linguagem de folhas de estilo, sendo responsável por definir como os elementos de conteúdo serão mostrados.

- **JavaScript:** é uma linguagem de programação. Ele é o responsável por tornar a página dinâmica e interativa.

---

> 2. Quantos arquivos CSS e Javascript podem estar vinculados a uma mesma página de hipertexto? Justifique sua resposta.

Uma página HTML pode estar associada a vários arquivos CSS e Javascript. Separar os códigos em arquivos diferentes pode ajudar a melhorar a organização do código-fonte de um site como um todo. 

---

> 3. É possível diferentes páginas de hipertexto terem vínculo com os mesmos arquivos Javascript e CSS? Justifique sua resposta.

Arquivos CSS e JavaScript podem estar vinculados a diferentes páginas, pois elas podem ter funcionalidades comportamentais em
comum.

---

> 4. Descreva a diferença entre uma página de hipertexto estática e uma dinâmica, pontuando as vantagens e desvantagens de cada um dos dois tipos.

- **Estática:** é quando as páginas de um site são totalmente compostas por arquivos prontos. Uma página estática tem a característica de não demandar atualizações com muita frequência. 

- **Dinâmica:** é quando as páginas (ao menos algumas delas) são geradas por uma aplicação web. Os arquivos podem ser modificados por alguém, mas depois da modificação eles continuam estáticos no servidor.

---

> 5. Qual é o caminho percorrido por uma requisição HTTP a uma página de hipertexto estática?

- O usuário informa uma URL na barra de endereços do navegador.
- O navegador consulta um servidor DNS e obtém o endereço IP do domínio digitado.
- Uma requisição HTTP é feita ao servidor web correspondente ao IP.
- O servidor responde com os arquivos necessários para a renderização da página.

---

> 6. Qual é o caminho percorrido por uma requisição HTTP a uma página de hipertexto dinâmica?

- O usuário informa uma URL na barra de endereços do navegador.
- O navegador consulta um servidor DNS e obtém o endereço IP do domínio digitado.
- Uma requisição HTTP é feita ao servidor web correspondente ao IP.
- O servidor responde com os dados necessários para a renderização da página, como dados armazenados em um banco de dados por exemplo.
- O servidor responde com os arquivos necessários para a renderização da página.

---

> 7. Quais as vantagens da atualização parcial de conteúdo em segundo plano em uma página de hipertexto usando Javascript? 

Ao se atualizar um conteúdo parcialmente, permitimos a modeficação de partes da página sem a necessidade de requisitar toda a página novamente. Recarregar toda a página novamente é algo computacionalmente custoso, e milhares de usuários fazendo isso ao mesmo tempo sobrecarregaria o servidor.
