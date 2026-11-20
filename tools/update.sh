#!/bin/sh
# Rebuild the website from the LaTeX sources in the Bewerbung project.
#   tools/update.sh [path/to/Bewerbung]
# 1. regenerates the publication list from shared/publications_body.tex
# 2. rebuilds index.html and ambizione.html
# 3. rebuilds the website copy of the CV (email written as [at], no mailto link)
set -e
SITE="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$(cd "${1:-$SITE/../Bewerbung}" && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

python3 -I "$SITE/tools/pubs_by_year.py" "$SRC/shared/publications_body.tex" > "$TMP/pubs.html"
python3 -I "$SITE/tools/build.py" "$TMP/pubs.html" "$SITE"

cd "$SRC"
sed 's|\\email{\\href{mailto:lucien.baumgartner@philos.uzh.ch}{lucien.baumgartner@philos.uzh.ch}}|\\email{lucien.baumgartner [at] philos.uzh.ch}|' cv.tex > cv_web.tex
latexmk -interaction=nonstopmode -halt-on-error cv_web.tex >/dev/null
cp cv_web.pdf "$SITE/cv/Lucien_Baumgartner_CV.pdf"
latexmk -C cv_web.tex >/dev/null
rm -f cv_web.tex cv_web.bbl
echo "Website rebuilt. Review with: python3 -m http.server --directory \"$SITE\""
