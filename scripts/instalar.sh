#!/usr/bin/env bash
# Instala os comandos deste ecossistema no teu Claude Code.
# Idempotente: corre as vezes que quiseres.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${HOME}/.claude/skills"
n_ok=0; n_falta=0; n_bak=0

echo "Ecossistema: ${REPO}"
echo "Destino:     ${DEST}"
echo

mkdir -p "${DEST}"

BACKUP="${DEST}/.backup-$(date +%Y%m%d-%H%M%S)"

instalar() {
  local nome="$1" origem="$2"
  if [[ ! -f "${origem}/SKILL.md" ]]; then
    printf '  [ ] %-26s sem SKILL.md, ignorado\n' "${nome}"; n_falta=$((n_falta+1)); return
  fi

  # Se ja existe um comando com este nome e o conteudo e diferente, guarda o antigo
  # antes de o substituir. Um comando teu com o mesmo nome nao se perde em silencio.
  if [[ -d "${DEST}/${nome}" ]] && ! diff -rq "${DEST}/${nome}" "${origem}" >/dev/null 2>&1; then
    mkdir -p "${BACKUP}"
    cp -R "${DEST}/${nome}" "${BACKUP}/${nome}"
    printf '  [!] %-26s ja existia e era diferente, copia em %s\n' "${nome}" "${BACKUP##*/}"
    n_bak=$((n_bak+1))
  fi

  rm -rf "${DEST:?}/${nome}"
  cp -R "${origem}" "${DEST}/${nome}"
  printf '  [x] /%-25s instalado\n' "${nome}"; n_ok=$((n_ok+1))
}

echo "O AGENTE PRINCIPAL"
instalar cerebro "${REPO}/cerebro"

if compgen -G "${REPO}/agentes/*/" > /dev/null; then
  echo; echo "AGENTES QUE TU CRIASTE"
  for d in "${REPO}"/agentes/*/; do instalar "$(basename "$d")" "$d"; done
fi

echo; echo "GATES E FERRAMENTAS DE OFICIO"
for d in "${REPO}"/skills/*/; do [[ -d "$d" ]] && instalar "$(basename "$d")" "$d"; done

echo
echo "Instalados: ${n_ok}. Ignorados: ${n_falta}. Substituidos com copia de seguranca: ${n_bak}."
[[ "${n_bak}" -gt 0 ]] && echo "  As versoes antigas estao em ${BACKUP}"
echo

if [[ ! -f "${REPO}/CLAUDE.md" ]]; then
  echo "FALTA UM PASSO:"
  echo "  cp CLAUDE.md.template CLAUDE.md    e preenche os [A PREENCHER]"
else
  restantes=$(grep -c 'A PREENCHER' "${REPO}/CLAUDE.md" 2>/dev/null || echo 0)
  [[ "${restantes}" -gt 0 ]] \
    && echo "AVISO: o CLAUDE.md ainda tem ${restantes} campos [A PREENCHER]." \
    || echo "CLAUDE.md preenchido."
fi

if [[ ! -f "${REPO}/cerebro/memory/state.md" ]]; then
  echo
  echo "SUGESTAO: cp cerebro/memory/state.md.template cerebro/memory/state.md"
  echo "          (a tua memoria de trabalho, fica fora do repositorio)"
fi

echo
echo "Pronto. Abre o Claude Code nesta pasta e escreve /cerebro"
