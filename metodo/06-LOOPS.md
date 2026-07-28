# Loops

Uma ferramenta funciona no dia em que te lembras dela. Numa semana com quatro reuniões seguidas, não
te lembras. Um loop é o que faz o resultado chegar sem tu pedires.

## A regra que evita a armadilha

**O loop não substitui o agente, entrega o.**

A parte determinística é código: ir buscar dados, verificar, formatar, enviar. O Claude entra só no
passo que exige julgamento. Automatizar o raciocínio todo é caro e frágil. Automatizar a entrega é
barato e robusto.

## Cinco decisões, por esta ordem

```
1. GATILHO       Relógio, evento, ou fim de outro processo?
2. VERIFICAÇÃO   Como é que ele sabe que correu bem, sem ninguém a olhar?
3. SILÊNCIO      O que acontece quando não há nada para dizer?
4. PERSISTÊNCIA  Onde guarda o estado entre execuções?
5. FIM           O que o desliga?
```

**A 2 é a que não se pode saltar.** Um loop que falha em silêncio é pior do que nenhum loop, porque
tu confias nele. Se não sabes responder, não ligues o loop ainda.

**A 3 quase sempre tem a mesma resposta certa: não envia nada.** Um alerta que chega todos os dias
deixa de ser lido à segunda semana, e a partir daí o loop está a produzir a ilusão de vigilância.

**A 5 é a que ninguém escreve.** Um loop sem condição de fim é um loop que alguém vai desligar à
bruta dentro de três meses, provavelmente no pior dia possível.

## Os três padrões

| Padrão | Gatilho | Usa quando |
|---|---|---|
| **Agendado** | Relógio | "Todas as segundas às 8h", antes de uma reunião fixa |
| **Por evento** | Algo aconteceu | "Quando entrar uma reunião nova" |
| **Encadeado** | Outro loop acabou | "Correu o semanal, faz o resumo" |

O agendado é o mais fácil e é onde começar. O por evento é o mais útil e exige que exista um sinal
fiável. O encadeado é onde as coisas se tornam difíceis de depurar, porque a falha aparece longe da
causa.

## Antes de ligar

```
□ O agente que ele entrega já passou SPAR? (senão, industrializas um erro)
□ Corri o loop à mão pelo menos três vezes, e o resultado estava certo nas três?
□ Sei onde ver se ele correu?
□ Ele avisa quando falha, ou falha em silêncio?
□ Se enviar para fora, tem aprovação? Ver 04-AUTONOMIA-E-RARV.md
```

A skill `/loop-engineering` desenha isto em detalhe. O Modo 6 do Cérebro usa a.
