# Updating the website

The pages are plain HTML, generated from the LaTeX sources of the CV
(`Bewerbung/shared/publications_body.tex` and `Bewerbung/cv.tex`).

After changing the publication list or the CV, run from the repo root:

    tools/update.sh                # assumes ../Bewerbung
    tools/update.sh /path/to/Bewerbung

This regenerates the publication list (published work only; under review and
in preparation are skipped), rebuilds `index.html` and `ambizione.html`, and
rebuilds the website copy of the CV with the email written as `[at]`.
Then review locally and commit/push to deploy.

- `pubs_by_year.py`: LaTeX publication list → year-grouped HTML
- `build.py`: page templates (About text, Contact, Ambizione description live here)
- `update.sh`: runs all of the above

Requires Python 3 and a TeX installation with LuaLaTeX/latexmk.
