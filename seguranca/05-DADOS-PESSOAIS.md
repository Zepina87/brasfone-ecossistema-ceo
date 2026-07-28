# Dados pessoais

Nome, email, telefone, morada, cargo numa empresa identificada, tudo o que permite chegar a uma
pessoa concreta. Em Portugal e na União Europeia isto é matéria de RGPD, e a responsabilidade é de
quem trata os dados, não da ferramenta que os processou.

Para quem dirige uma empresa, a parte que interessa é simples: **a multa e o dano de reputação são
teus**, e não do agente que fez o trabalho.

---

## As quatro regras que evitam quase tudo

**1. Minimização.** O agente recebe os dados de que precisa para a tarefa, e nada mais. Se a
tarefa é pontuar oportunidades por sector, ele não precisa do telefone de ninguém. Passar a base
de dados inteira porque é mais fácil é o erro mais comum e o mais difícil de justificar depois.

**2. Nunca no repositório.** Ficheiros com dados de pessoas não entram no git, mesmo em repositório
privado, mesmo em ramo local. Ficam numa pasta ignorada, ou fora do projecto. Um repositório privado
hoje pode ser partilhado amanhã, e o histórico vai com ele.

**3. Exemplos são inventados.** Toda a documentação, todo o teste, todo o master prompt usa dados
falsos. Um nome real num exemplo de documentação é uma fuga, e é uma fuga que se propaga por
cópia durante anos.

**4. Finalidade declarada.** Os dados foram recolhidos para algo. Usá los para outra coisa precisa
de base legal própria. "Já os tínhamos" não é base legal, e é a frase que aparece em todas as
decisões de contra ordenação.

---

## O que fica fora do repositório

| Não entra | Porquê |
|---|---|
| Listas de contactos, leads, clientes | Dados pessoais identificáveis |
| Exports de sistemas com pessoas dentro | O mesmo, em volume |
| Transcrições de reuniões | Nomes, opiniões, e às vezes coisas ditas em confiança |
| Emails reais, ficheiros de campanha com destinatários | Dados pessoais e conteúdo |
| Capturas de ecrã de sistemas com dados à vista | Escapa sempre, porque ninguém olha para o fundo da imagem |
| Identificadores internos de registos de pessoas | Permitem reidentificação por quem tem acesso ao sistema |

No `.gitignore` isto traduz se em ignorar por pasta e por extensão, e a pasta de trabalho com
dados vive fora da árvore do repositório. É mais seguro do que confiar no `.gitignore`, porque uma
pasta que não está lá não pode ser committada por acidente.

---

## Quando um agente trata dados de pessoas

```
□ A tarefa precisa mesmo dos dados identificáveis, ou chega o agregado?
□ Passei o mínimo, ou passei tudo porque era mais rápido?
□ O resultado vai ter dados pessoais dentro? Quem o vai ler?
□ Onde é que fica guardado o intermédio, e quem o apaga?
□ Se esta pessoa pedisse para ser apagada, eu conseguia apagar tudo?
```

A última pergunta é a que revela os problemas. Se a resposta é "não sei onde isso está todo", o
processo está mal desenhado, independentemente de alguém vir a pedir.

---

## Dados sensíveis

Saúde, opiniões políticas, religião, orientação sexual, dados biométricos, condenações. Categoria
especial no RGPD, com regras mais duras e coimas maiores.

Regra prática: **não entram num agente**, ponto. Se o teu negócio trabalha com esta categoria, o
desenho tem de ser pensado com apoio jurídico antes de existir, e não corrigido depois de existir.

---

## Se houver uma fuga

O RGPD dá **72 horas** para notificar a autoridade de controlo, desde o momento em que tomas
conhecimento. O prazo é curto de propósito, e a contagem não espera pela investigação interna.

```
1. Parar a origem. Revogar acessos, tirar o ficheiro de onde está.
2. Registar o que aconteceu, quando, que dados, quantas pessoas. Por escrito, com horas.
3. Avaliar o risco para as pessoas afectadas.
4. Notificar quem tem de ser notificado, dentro das 72 horas.
5. Só depois a análise de causa e as medidas para não repetir.
```

Ter isto escrito antes de acontecer é a diferença entre uma resposta ordenada e três dias de pânico.
Quinze minutos hoje.
