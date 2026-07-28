# Anatomia de um agente que funciona

Um agente é um documento. O que separa um que funciona de um que não funciona não é inteligência,
é **precisão do pedido**. Oito secções, e as que as pessoas saltam são a 5 e a 7.

```
1. MISSÃO           Uma frase. Se precisas de duas, são dois agentes
2. GATILHOS         As frases exactas com que o chamas
3. MODOS            O que ele faz. Um modo é uma entrada, um processo, uma saída
4. O QUE NUNCA FAZ  A lista de proibições. Vale mais do que a lista de capacidades
5. CRITÉRIO DE      Como se sabe que o resultado está certo, de forma verificável
   SUCESSO          "Uma boa análise" não é critério. "Cada número tem fonte" é
6. FORMATO          A forma exacta do que sai. Sem isto, muda a cada vez
7. TRATAMENTO       O que faz quando falta um dado, uma ferramenta falha, ou o pedido
   DE ERRO          é ambíguo. Sem isto, ele inventa, e inventar é o pior fracasso
8. VERIFICAÇÃO      O passo em que confirma o que fez, antes de dizer que fez
```

## Porque é que a secção 4 é a mais valiosa

Um agente sem proibições faz tudo o que parece útil, e "parece útil" é uma definição elástica.
As proibições são o que o torna previsível, e a previsibilidade é o que te faz confiar nele o
suficiente para o usares sem verificar tudo.

Cada linha da secção 4 nasce de uma vez em que ele fez algo que te incomodou. Começa curta e cresce.

## Três erros que se repetem

**O agente que faz tudo.** "Analisa, escreve, envia e arquiva." Falha num dos quatro e não sabes em
qual. Um passo, um agente, uma saída verificável.

**O critério de sucesso qualitativo.** "Produz uma análise útil." Não é testável, portanto nunca
falha formalmente, portanto nunca melhora.

**O modo que nasceu por simetria.** "Já tem análise semanal, vamos pôr mensal e trimestral." Se não
tens a queixa, não tens o modo. Cada modo custa clareza a todos os outros.

## Teste antes de instalar

Um caso real teu, não inventado. Se o resultado precisa que tu expliques ao agente o que ele
devia ter feito, o master prompt está incompleto, e é lá que se corrige, não na conversa.
