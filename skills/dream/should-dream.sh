#!/usr/bin/env bash
#
# should-dream.sh - Verifica se a consolidação de memória deve correr
#
# Retorna exit code 0 se dream deve correr, 1 se não.
# Condição: 24+ horas desde a última consolidação.

set -euo pipefail

SKILL_DIR="$HOME/.claude/skills/dream"
CONFIG="$SKILL_DIR/.dream-config"
MEMORY_DIR="$HOME/.claude/projects/C--Users-josep-es4uf2w/memory"
LAST_DREAM_FILE="$MEMORY_DIR/.last-dream"

# Se nunca correu, condição satisfeita
if [[ ! -f "$LAST_DREAM_FILE" ]]; then
    echo "Dream conditions met: first-run (no .last-dream found)"
    exit 0
fi

# Verificar: 24+ horas desde última consolidação
LAST_DREAM=$(cat "$LAST_DREAM_FILE")
NOW=$(date +%s)
ELAPSED=$(( NOW - LAST_DREAM ))
HOURS_ELAPSED=$(( ELAPSED / 3600 ))

if (( HOURS_ELAPSED < 24 )); then
    exit 1  # Muito cedo
fi

echo "Dream conditions met: ${HOURS_ELAPSED}h since last dream"
exit 0
