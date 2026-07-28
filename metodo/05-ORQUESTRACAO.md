# Orquestração

Quando um objectivo precisa de vários passos ou vários agentes. O que faz uma orquestração falhar
não é a dificuldade dos passos, é perder se pelo caminho e não notar.

## Dois cadernos

**Caderno de tarefa**, escrito uma vez, só muda se houver replaneamento:

```
O que sei de certeza
O que preciso de descobrir
O que estou a assumir (e pode estar errado)
Plano: passo · agente · entrada mínima · saída esperada · critério de sucesso
```

**Caderno de progresso**, quatro perguntas depois de cada passo:

```
1. O critério de sucesso ficou satisfeito?
2. Estou a andar em círculos?
3. Houve progresso real, ou só actividade?
4. Qual é o passo seguinte, concreto?
```

A separação é o que importa. Sem o caderno de tarefa, o plano dissolve se na conversa. Sem o de
progresso, os passos correm e ninguém verifica.

## Regras de decomposição

- **Um passo é um agente e uma saída verificável.** Se não se verifica, não é um passo.
- **Contexto mínimo a cada agente.** Nunca a conversa toda: entulha, encarece e piora o resultado.
- **Duas falhas no mesmo passo e para de repetir.** Replaneia ou registas o bloqueio e segues para
  os passos independentes. Insistir à terceira é desperdício com aparência de persistência.

## Terminar

Cinco razões, e só cinco:

```
a) todos os passos verificados
b) limite de tentativas atingido depois de replanear
c) orçamento esgotado, e diz onde parou
d) bloqueado à tua espera, com os passos independentes feitos
e) erro irrecuperável, registado
```

Sempre com resumo final até dez linhas, para revires em menos de quinze minutos. Um resumo de
quarenta linhas não é revisto, é arquivado.

## Retomar

Uma orquestração de três ou mais passos vai ser interrompida. Portanto o ponto de controlo em
`## RUNS` não é opcional.

Ao retomar: **verificar o que ficou realmente feito antes de continuar.** Um ponto de controlo é um
sítio onde se gravou, não a verdade sobre o mundo. Se o passo 3 dizia "criado", confirma que existe.
