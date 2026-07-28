# Permissões e hooks

O que o agente pode fazer sem te perguntar, e o que corre na tua máquina sem tu saberes.

---

## Permissões

O Claude Code pergunta antes de acções sensíveis. Podes pré autorizar padrões para não estares
sempre a clicar. É uma boa ideia, e é também onde as pessoas abrem a porta que depois lamentam.

**Autoriza por padrão específico, nunca por categoria larga:**

| Autorização | Veredicto |
|---|---|
| `Bash(git status)`, `Bash(npm test)` | ✅ Específico e reversível |
| `Read(*)` no teu projecto | ✅ Ler não estraga |
| `Bash(git *)` | ⚠️ Inclui `git reset --hard` e `git push --force` |
| `Bash(*)` | ❌ Nunca. É acesso total à máquina |
| `Write(*)` sem limite de pasta | ❌ Inclui o que está fora do projecto |

A regra: autorizar verbos, não ferramentas. `git status` é um verbo. `git` é uma ferramenta com
verbos destrutivos dentro.

**Nunca autorizar por defeito:** apagar recursivo, escrever fora da pasta do projecto, enviar para
fora, alterar configuração do sistema, instalar coisas globalmente.

---

## Um travão para comandos destrutivos

Há uma categoria de comando que deve parar sempre, mesmo com tudo o resto autorizado, mesmo que
tenhas dito ao agente para trabalhar sem interrupções:

```
rm -rf              apagar recursivo
git reset --hard    perder trabalho não commitado
git push --force    reescrever o histórico de outros
drop table, truncate  destruir dados
> ficheiro          sobrescrever
chmod 777           abrir permissões
curl ... | bash     executar código descarregado sem o ler
```

A autonomia é boa para andar depressa. Não é boa para o comando que não tem desfazer. Estes sete
não são uma questão de confiança no agente, são uma questão de assimetria: o ganho de não parar é
um segundo, o custo de estar errado é um dia.

---

## Hooks

Um hook é código teu que o Claude Code corre automaticamente, antes ou depois de certas acções.
São muito úteis: podem correr o gitleaks antes de cada commit, avisar te quando a conversa está a
ficar grande, guardar memória no fim da sessão.

São também o sítio mais discreto para pôr código malicioso, porque:

- correm **sem te avisar**, em cada acção que corresponda ao padrão
- correm com as **tuas permissões**
- estão num ficheiro de configuração para onde ninguém volta a olhar

### Regras

1. **Lê todos os hooks que tens.** Agora, não um dia. `~/.claude/settings.json` e o `settings.json`
   do projecto.
2. **Um hook que veio de fora audita se linha a linha** antes de entrar. Ver
   [02-REPOS-EXTERNOS.md](02-REPOS-EXTERNOS.md).
3. **Um hook não deve fazer rede.** Se um hook fala com a internet, tens de saber exactamente com
   quem e porquê.
4. **Hooks não são copiados no clone.** Quem clonar o repositório não os tem. Se um hook é
   importante para a segurança, tem de estar documentado para ser reinstalado, e não assumido.
5. **Escreve caminhos relativos.** Um hook com um caminho absoluto da máquina de quem o escreveu
   falha em silêncio na tua, e um hook de segurança que falha em silêncio é pior do que nenhum.

### O que vale a pena ter

| Hook | Faz |
|---|---|
| Pre commit com gitleaks | Recusa o commit se encontrar um segredo. Ver [01-SEGREDOS.md](01-SEGREDOS.md) |
| Aviso de contexto | Diz te quando a conversa está a ficar grande, para compactares em bom sítio |
| Memória no fim da sessão | Escreve o que ficou decidido, para não morrer com a conversa |

Três hooks é um bom número. Doze hooks é um sistema que ninguém percebe, e que um dia faz algo
que tu não pediste e não consegues explicar.

---

## MCPs

Um servidor MCP dá ao agente uma capacidade nova. Antes de ligar um, quatro perguntas, e a
auditoria completa está em [02-REPOS-EXTERNOS.md](02-REPOS-EXTERNOS.md):

1. **Que permissões pede?** Pede as mínimas para o que precisas, e não as que ele oferece.
2. **É oficial?** Se existir versão oficial, usa a oficial, mesmo com menos funções.
3. **O que é que ele vê?** Um MCP ligado ao email vê o email todo, e o agente também.
4. **Onde se revoga?** Sabe isso antes de dar o acesso, não no dia em que precisas.

**Nunca:** um MCP com escrita em produção ligado a um agente que lê conteúdo de fora. Ver
[03-INJECCAO-DE-PROMPT.md](03-INJECCAO-DE-PROMPT.md).

---

## Revisão trimestral

Quinze minutos, quatro vezes por ano:

```
□ Que skills tenho instaladas? Uso as todas? Desinstalar o resto
□ Que hooks correm? Li os desde a última vez?
□ Que MCPs estão ligados? Ainda preciso deles todos?
□ Que permissões pré autorizei? Alguma ficou mais larga do que devia?
□ Alguma chave tem mais de um ano?
```

O objectivo não é a paranoia. É que a superfície de ataque cresce sozinha, por acumulação de coisas
úteis, e nunca diminui sem alguém decidir que diminui.
