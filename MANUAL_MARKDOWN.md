# Manual de Markdown

> Um guia prático com exemplos de **todos os principais estilos** do Markdown.
> Use este arquivo como referência rápida. Cada seção mostra o resultado e,
> em blocos de código, como escrevê-lo.

---

## Índice

1. [Títulos](#títulos)
2. [Ênfase de texto](#ênfase-de-texto)
3. [Listas](#listas)
4. [Links e imagens](#links-e-imagens)
5. [Citações](#citações)
6. [Código](#código)
7. [Tabelas](#tabelas)
8. [Linhas horizontais](#linhas-horizontais)
9. [Listas de tarefas](#listas-de-tarefas)
10. [Notas de rodapé](#notas-de-rodapé)
11. [Recursos extras](#recursos-extras)

---

## Títulos

Use `#` para criar títulos. Quanto mais `#`, menor o título.

```markdown
# Título nível 1
## Título nível 2
### Título nível 3
#### Título nível 4
##### Título nível 5
###### Título nível 6
```

# Título nível 1
## Título nível 2
### Título nível 3
#### Título nível 4
##### Título nível 5
###### Título nível 6

---

## Ênfase de texto

```markdown
*itálico* ou _itálico_
**negrito** ou __negrito__
***negrito e itálico***
~~riscado~~
`código inline`
```

- *itálico* ou _itálico_
- **negrito** ou __negrito__
- ***negrito e itálico***
- ~~riscado~~
- `código inline`

---

## Listas

### Lista não ordenada

```markdown
- Item A
- Item B
  - Subitem B.1
  - Subitem B.2
- Item C
```

- Item A
- Item B
  - Subitem B.1
  - Subitem B.2
- Item C

### Lista ordenada

```markdown
1. Primeiro
2. Segundo
   1. Segundo.um
   2. Segundo.dois
3. Terceiro
```

1. Primeiro
2. Segundo
   1. Segundo.um
   2. Segundo.dois
3. Terceiro

---

## Links e imagens

```markdown
[Texto do link](https://exemplo.com)
[Link com título](https://exemplo.com "Passe o mouse aqui")
<https://link-automatico.com>

![Texto alternativo da imagem](https://via.placeholder.com/150)
```

[Texto do link](https://exemplo.com) ·
[Link com título](https://exemplo.com "Passe o mouse aqui") ·
<https://link-automatico.com>

---

## Citações

```markdown
> Isto é uma citação.
>
> > Citações podem ser aninhadas.
>
> — Autor da frase
```

> Isto é uma citação.
>
> > Citações podem ser aninhadas.
>
> — Autor da frase

---

## Código

### Código em linha

Use crases simples: `` `meuCodigo()` ``.

### Bloco de código com destaque de sintaxe

````markdown
```python
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Mundo"))
```
````

```python
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Mundo"))
```

```javascript
const soma = (a, b) => a + b;
console.log(soma(2, 3)); // 5
```

---

## Tabelas

```markdown
| Recurso     | Suportado | Observação              |
|:------------|:---------:|------------------------:|
| Títulos     |     ✅    | Seis níveis             |
| Tabelas     |     ✅    | Alinhamento configurável|
| Vídeo       |     ❌    | Não nativo              |
```

| Recurso     | Suportado | Observação               |
|:------------|:---------:|-------------------------:|
| Títulos     |     ✅    | Seis níveis              |
| Tabelas     |     ✅    | Alinhamento configurável |
| Vídeo       |     ❌    | Não nativo               |

> Dica: `:` na linha separadora controla o alinhamento (esquerda, centro, direita).

---

## Linhas horizontais

```markdown
---
***
___
```

Todas produzem uma linha como esta:

---

## Listas de tarefas

```markdown
- [x] Tarefa concluída
- [ ] Tarefa pendente
- [ ] Outra tarefa
```

- [x] Tarefa concluída
- [ ] Tarefa pendente
- [ ] Outra tarefa

---

## Notas de rodapé

```markdown
Aqui há uma afirmação com nota de rodapé.[^1]

[^1]: Esta é a explicação da nota de rodapé.
```

Aqui há uma afirmação com nota de rodapé.[^1]

[^1]: Esta é a explicação da nota de rodapé.

---

## Recursos extras

### Detalhes recolhíveis (HTML embutido)

```markdown
<details>
<summary>Clique para expandir</summary>

Conteúdo escondido que aparece ao clicar.

</details>
```

<details>
<summary>Clique para expandir</summary>

Conteúdo escondido que aparece ao clicar.

</details>

### Emojis

Muitos renderizadores aceitam `:emoji:` — por exemplo `:rocket:` 🚀, `:tada:` 🎉.

### Quebra de linha forçada

Termine a linha com dois espaços  
para forçar uma quebra sem novo parágrafo.

### Escapando caracteres

Use a barra invertida `\` para mostrar símbolos literais:

```markdown
\*isto não fica em itálico\*
```

\*isto não fica em itálico\*

---

> **Fim do manual.** Bons textos! ✍️
