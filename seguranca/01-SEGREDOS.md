# Segredos

A regra é uma e não tem excepções: **uma chave nunca é escrita num ficheiro que possa entrar no
histórico do git.** Nem "por agora", nem "só para testar", nem num comentário.

A razão não é teórica. Um segredo commitado continua no histórico depois de o apagares do
ficheiro. Quem tiver acesso ao repositório, hoje ou dentro de dois anos, consegue lê lo com um
comando. Apagar a linha não resolve, e reescrever o histórico de um repositório partilhado estraga
o de todos os outros.

---

## Onde vivem as chaves

```
.env              as chaves reais. Está no .gitignore. Nunca entra no repositório
.env.example      os nomes das variáveis, sem valores. Este entra, e é o que documenta
```

No código e nos agentes usa se sempre o **nome da variável**, nunca o valor:

```
correcto:  o token vem de CRM_API_TOKEN
errado:    token: a1b2c3d4... (mesmo truncado, mesmo num exemplo, mesmo inventado)
```

Nos ficheiros de memória e nos master prompts, a mesma coisa: o `core.md` lista o nome da variável
e o que ela serve, nunca o valor.

---

## Verificar antes de publicar

Instala o `gitleaks` uma vez:

```bash
brew install gitleaks        # macOS
```

Corre antes de qualquer publicação:

```bash
gitleaks detect --source . --verbose
```

Zero achados é a condição para publicar. Um achado é um travão, não um aviso.

### Deixa a máquina verificar por ti

Um hook de pre commit corre isto automaticamente e recusa o commit se encontrar algo. Vale os dois
minutos de instalação, porque a vez em que te esqueces é a vez que conta:

```bash
cat > .git/hooks/pre-commit <<'FIM'
#!/usr/bin/env bash
if command -v gitleaks >/dev/null 2>&1; then
  gitleaks protect --staged --redact --verbose || {
    echo ""
    echo "COMMIT RECUSADO: encontrei algo que parece um segredo."
    echo "Tira o valor, põe o nome da variável, e volta a tentar."
    exit 1
  }
fi
FIM
chmod +x .git/hooks/pre-commit
```

Os hooks não são copiados quando alguém clona o repositório. Quem clonar tem de correr isto outra
vez, e por isso está escrito aqui.

---

## O que nunca entra no repositório

| Não entra | Porquê | O que entra em vez disso |
|---|---|---|
| `.env`, chaves, tokens, senhas | Óbvio, e continua a acontecer | `.env.example` com os nomes |
| `settings.json` real do Claude Code | Costuma ter chaves de MCPs dentro | Um template com as chaves em branco |
| A tua memória viva (`state.md`) | Tem clientes, valores e decisões internas | O template da estrutura |
| Exports de conversas | Histórico pessoal e de negócio | Nada. Fica fora, numa pasta ignorada |
| Ficheiros com dados de pessoas | Ver [05-DADOS-PESSOAIS.md](05-DADOS-PESSOAIS.md) | Dados inventados para exemplos |
| Caminhos de ficheiros da tua máquina | Diz o teu nome de utilizador e a estrutura da máquina | Caminhos relativos |

---

## Quando uma chave se expõe

Assume comprometida. Não avalies a probabilidade, porque a avaliação vai sempre dar "provavelmente
ninguém viu", e é o tipo de conta que só se erra uma vez.

```
1. Revoga a chave no sistema que a emitiu. Primeiro isto, antes de qualquer limpeza.
2. Emite uma nova e põe na .env.
3. Só depois limpa o ficheiro e o histórico, se fizer sentido.
4. Vê o registo de acessos do sistema, se ele tiver, à procura de uso que não foi teu.
5. Escreve no state.md o que aconteceu e o que fizeste.
```

O passo 1 antes do passo 3 é o que importa. Uma chave revogada num ficheiro público é inofensiva.
Uma chave válida escondida num histórico limpo é uma porta aberta.

---

## Rotação

As chaves não caducam sozinhas, e uma chave de três anos passou por portáteis, backups e
ferramentas que já nem usas.

| Quando | O que |
|---|---|
| Alguém sai da equipa | Tudo a que essa pessoa teve acesso |
| Uma chave apareceu num sítio errado | Essa, imediatamente |
| Uma vez por ano, sem motivo | Todas. Marca no calendário, senão não acontece |

Guarda a lista das chaves e das datas de rotação num gestor de senhas, não num documento partilhado.
Um documento com chaves em texto simples é o problema, mesmo que o documento seja privado.
