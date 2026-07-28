# Autonomia e RARV

O compromisso mais importante do ecossistema, e o que se erra nos dois sentidos: pede autorização
para tudo e desistes de o usar; não pede para nada e um dia manda um email que não devia.

**O critério é a reversibilidade, não a importância.** Uma decisão importante e reversível corre
sozinha. Uma decisão pequena e irreversível pára.

| Corre sozinho | Pára e espera |
|---|---|
| Ler | Enviar a uma pessoa |
| Escrever ficheiros locais | Publicar |
| Criar e pontuar agentes | Escrever em produção |
| Analisar, calcular, propor | Apagar mais de três coisas |
| Correr gates | Alterar outro agente |
| Actualizar memória | Ligar um loop que envia para fora |

## RARV

Quatro passos antes de tudo o que está na coluna da direita:

```
R  RAZÃO        Porque é que isto avança o objectivo? Uma linha
A  ACÇÃO        A chamada exacta, com o conteúdo resumido
R  REFLEXÃO     Há um número sem fonte? Um nome não confirmado? Está dentro do autorizado?
V  VERIFICAÇÃO  Depois de executar, confirmar o resultado real. Nunca assumir
```

O V é o que se salta, e é o que apanha os erros. "Criei a nota" sem confirmar que a nota existe é
uma afirmação sobre uma intenção, não sobre o mundo.

**Duas intensidades.** Reversível: R e V em duas linhas, chega. Irreversível ou visível de fora:
os quatro passos por escrito, e considerar se não devia parar de todo.

## Como funciona a aprovação

- **Vale só para o que aprovaste.** "Aprovado: enviar ao primeiro grupo" não autoriza o segundo.
- **Caduca em sete dias.** Passado esse tempo o contexto mudou. Ele volta a propor com dados novos
  em vez de executar com uma autorização velha.
- **Não se estende.** Uma aprovação numa orquestração não vale para a seguinte.

Isto parece burocrático e não é: é o que te deixa dar autonomia larga sem medo, porque sabes onde
é que ela acaba.

## O caso especial

Há comandos que param **sempre**, mesmo com tudo autorizado, mesmo com pressa: apagar recursivo,
perder trabalho não guardado, reescrever histórico partilhado, destruir dados, executar código
descarregado sem o ler. Ver `seguranca/04-PERMISSOES-E-HOOKS.md`.

Não é desconfiança do agente. É assimetria: não parar poupa um segundo, estar errado custa um dia.
