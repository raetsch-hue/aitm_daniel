#!/usr/bin/env bash

set -u

# Immer im Ordner dieses Skripts arbeiten.
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

echo "============================================================"
echo " Repo:   $PWD"
echo " Remote: origin/main"
echo "============================================================"
echo

echo "Inhaltsverzeichnis der Artefakte wird neu gebaut ..."
if command -v python3 >/dev/null 2>&1; then
  python3 coursetools/inhalt-bauen.py || {
    echo "Hinweis: Das Inhaltsverzeichnis konnte nicht aktualisiert werden."
    echo "INHALT.md bleibt auf dem letzten Stand."
  }
elif command -v python >/dev/null 2>&1; then
  python coursetools/inhalt-bauen.py || {
    echo "Hinweis: Das Inhaltsverzeichnis konnte nicht aktualisiert werden."
    echo "INHALT.md bleibt auf dem letzten Stand."
  }
else
  echo "Hinweis: Kein Python gefunden. INHALT.md bleibt auf dem letzten Stand."
fi
echo

git add . || exit 1

echo "Diese Dateien werden committet:"
echo
git status --short
echo

if git diff --cached --quiet; then
  echo "Keine Änderungen zum Committen vorhanden."
  exit 0
fi

read -r -p "Fortfahren und committen? (j = ja): " ok
if [[ "$ok" != "j" && "$ok" != "J" ]]; then
  echo
  echo "Abgebrochen. Die Änderungen bleiben nur vorgemerkt (staged)."
  exit 0
fi

git commit -m "Projektstruktur AITM 08/2026 DR" || exit 1

echo
echo "Standardmäßig wird ohne --force gepusht."
read -r -p "Jetzt zu origin/main pushen? (j = ja): " push_ok
if [[ "$push_ok" != "j" && "$push_ok" != "J" ]]; then
  echo "Commit erstellt, Push aber abgebrochen."
  exit 0
fi

if ! git push -u origin main; then
  echo
  echo "Push fehlgeschlagen. Prüfe bei Bedarf:"
  echo "  git config --global user.name"
  echo "  git config --global user.email"
  echo "  gh auth login"
  exit 1
fi

echo
echo "Fertig. Datei online unter:"
echo "https://github.com/raetsch-hue/aitm_daniel/blob/main/artefakte/woche-01/gegenrede.md"
