# Erros

A forma como um agente falha importa mais do que a frequência com que falha. Uma falha declarada
custa cinco minutos. Uma falha silenciosa, ou inventada, custa a confiança em tudo o resto.

## O protocolo

```
1. Falha uma ferramenta          uma tentativa imediata
2. Persiste                      caminho alternativo, e registar qual
                                 "⚠️ ALTERNATIVA: [o que falhou] para [o que usei]"
3. Falhou tudo                   registar nos PENDENTES com o erro exacto, e dizer
4. Falta um dado                 dizer qual falta. Nunca preencher
```

## As três formas de falhar mal

**Silenciar.** O passo falhou, o agente seguiu, e o relatório final diz que está tudo bem. É a pior,
porque tu agiste sobre uma conclusão que não tem base.

**Inventar.** A ferramenta não devolveu o número, e o agente produziu um número plausível. Muitas
vezes nem é deliberado: o modelo completa o padrão. É por isso que o V do RARV existe.

**Assumir sucesso.** "Criei o registo." Criou? A chamada devolveu confirmação? Sem verificar, isto é
uma afirmação sobre uma intenção, não sobre o mundo.

## O que registar

```
[data] O que tentei | o que falhou | o erro exacto | o que fiz em alternativa | o que falta
```

O erro exacto, não a paráfrase. "Não conseguiu ligar" não se depura. A mensagem de erro literal
resolve o problema em dois minutos daqui a três semanas.

## Falta de dados

O caso mais frequente e o mais mal tratado. Quando falta o dado, a resposta certa é dizer que falta.

Uma análise genérica sobre dados que não existem **parece trabalho e não é**: tem a forma de uma
análise, a extensão de uma análise, e nenhum conteúdo. E é pior do que não responder, porque
consome a tua atenção antes de tu descobrires que está vazia.

## Depois de um erro real

Vai ao master prompt, não à conversa. A correcção que fica na conversa morre com ela, e o mesmo erro
volta na sexta. A dimensão 6 do SPAR desce, o master prompt ganha uma linha na secção de erros, e a
pontuação sobe outra vez quando o caso que falhava passar.
