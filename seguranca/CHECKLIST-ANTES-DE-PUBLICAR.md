# Checklist antes de publicar

Corre isto antes de tornar público qualquer repositório, ou antes de dar acesso a alguém de fora.
Nenhum passo é opcional, e a ordem importa: o automático primeiro, porque é o que apanha o óbvio, e
o manual depois, porque é o que apanha o que interessa.

---

## Automático

```bash
# 1. Segredos, incluindo o histórico
gitleaks detect --source . --verbose

# 2. Chaves e tokens que o gitleaks não conheça
grep -rniE '(api[_-]?key|secret|token|password|passwd|bearer)[[:space:]]*[:=]' . \
  --exclude-dir=.git --exclude-dir=node_modules | grep -vE '\[A PREENCHER\]|NOME_DA_VARIAVEL|example'

# 3. Caminhos que revelam a tua máquina
grep -rniE 'C:\\\\Users|/Users/[a-z]|/home/[a-z]' . --exclude-dir=.git --exclude-dir=node_modules

# 4. Emails reais
grep -rhoE '[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}' . --exclude-dir=.git | sort -u

# 5. Ficheiros que não deviam existir
find . -name '.env' -o -name '*.key' -o -name '*.pem' -o -name 'settings.json' \
  -o -name '*.csv' -o -name '*.xlsx' | grep -v node_modules

# 6. Ficheiros grandes, que costumam ser dados esquecidos
find . -type f -size +1M -not -path './.git/*' -not -path '*/node_modules/*' -exec ls -lh {} \;
```

Cada um destes tem de dar vazio, ou dar só resultados que tu explicaste a ti mesmo em voz alta.

---

## Manual

O automático não apanha o que faz mais estragos, porque o que faz mais estragos está escrito em
português correcto e parece pertencer ali.

```
□ NOMES. Cada nome de cliente, parceiro ou pessoa: está autorizado a sair?
  Confirmar contra a tabela de prova social do /fact-check, não de memória.

□ RELAÇÕES. Onde diz "cliente", é cliente? Onde diz "parceiro", é parceiro?
  Chamar cliente a um parceiro é uma afirmação falsa, e a pessoa costuma descobrir.

□ NÚMEROS. Cada número tem origem? Correr /fact-check ao repositório todo,
  não só aos documentos que parecem comerciais.

□ CAPACIDADES. "Integramos com X", "temos Y". Existe hoje, em produção?
  Se tem um "estamos a", a frase está errada e tem de mudar.

□ DADOS DE PESSOAS. Algum ficheiro tem contactos, leads, transcrições?
  Ver 05-DADOS-PESSOAIS.md.

□ CAPTURAS DE ECRÃ. Alguma imagem tem dados reais visíveis, mesmo em segundo plano?
  É por aqui que escapa mais vezes, porque ninguém olha para o fundo da imagem.

□ HISTÓRICO. O histórico do git tem coisas que já apagaste dos ficheiros?
  Se sim, e se for sensível: repositório novo com um commit único, não limpeza do histórico.

□ ESCRITO PARA DENTRO. Há comentários, notas ou observações que foram escritos
  a pensar que ninguém de fora ia ler?
```

---

## Publicar

Só quando tudo acima estiver limpo:

```bash
git init && git add -A && git commit -m "..."
gh repo create [nome] --private --source=. --push
```

**Privado primeiro, sempre.** Dar acesso a uma pessoa é um segundo passo, separado e deliberado.
E é o passo que não tem desfazer: a partir do momento em que alguém viu, viu, mesmo que revogues
o acesso cinco minutos depois. Portanto trata a decisão de dar acesso como definitiva, porque é.

```bash
gh api repos/[dono]/[nome]/collaborators/[utilizador] -X PUT   # dar acesso
gh api repos/[dono]/[nome]/collaborators --jq '.[].login'      # ver quem tem
```

Verifica quem tem acesso **antes** de assumires que ninguém tem. É uma linha de comando, e é a
diferença entre saber e supor.
