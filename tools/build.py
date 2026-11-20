"""Assemble index.html and ambizione.html for the website."""
import sys

pubs_file, out_dir = sys.argv[1], sys.argv[2]
pubs = open(pubs_file, encoding='utf-8').read()

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/academicons/1.9.4/css/academicons.min.css">
  <link rel="stylesheet" href="style.css">
</head>
<body>
'''


def topbar(prefix, current):
    cur = ' aria-current="page"' if current == 'project' else ''
    return f'''
<header class="topbar">
  <div class="wrap">
    <a class="brand" href="{prefix or '#'}">Lucien Baumgartner</a>
    <button class="menu-toggle" aria-label="Menu" aria-expanded="false"
            onclick="const t=this.closest('.topbar');t.classList.toggle('open');this.setAttribute('aria-expanded',t.classList.contains('open'))">
      <i class="fa-solid fa-bars"></i>
    </button>
    <ul class="menu">
      <li><a href="{prefix}#about">About</a></li>
      <li><a href="{prefix}#publications">Publications</a></li>
      <li><a href="{prefix}#contact">Contact</a></li>
      <li><a class="project" href="ambizione.html"{cur}>SNSF Ambizione Project</a></li>
    </ul>
  </div>
</header>
'''


FOOT = '''
  <footer>© Lucien Baumgartner · Last updated November 2026</footer>
</main>

<script>
  // close the mobile menu after picking a section
  document.querySelectorAll('.menu a').forEach(a => a.addEventListener('click', () =>
    document.querySelector('.topbar').classList.remove('open')));
</script>
</body>
</html>
'''

index = HEAD.format(
    title='Lucien Baumgartner',
    desc='Lucien Baumgartner, philosopher working on philosophy of language and mind, concepts and evaluative language, with experimental and computational methods.'
) + topbar('', 'home') + '''
<main class="wrap">

  <section id="about" class="hero">
    <h1>Lucien Baumgartner, PhD</h1>
    <p class="tagline">Postdoc at the Chair for Ethics, University of Zurich</p>
    <ul class="links">
      <li><a href="cv/Lucien_Baumgartner_CV.pdf"><i class="fa-regular fa-file-lines"></i>CV (PDF)</a></li>
      <li><a href="https://orcid.org/0000-0003-1698-0114"><i class="ai ai-orcid"></i>ORCID</a></li>
      <li><a href="https://www.semanticscholar.org/author/L.-Baumgartner/2135114773"><i class="ai ai-semantic-scholar"></i>Semantic Scholar</a></li>
      <li><a href="https://www.github.com/lucienbaumgartner"><i class="fa-brands fa-github"></i>GitHub</a></li>
    </ul>
    <p>I am a philosopher working on the philosophy of language and mind. I am currently a postdoctoral researcher at the Chair for Ethics at the University of Zurich. From 2027, I will lead the SNSF Ambizione project <a class="projectname" href="ambizione.html">Cognitive Chimeras: The Dynamics of Category Extension in the Hierarchy of Concepts</a> at the University of Neuchâtel.</p>
    <p>My research asks how we categorize and evaluate with words: how thick and thin evaluative concepts work, what dual character concepts are, and how categories are extended and change over time. I combine philosophical analysis with experimental philosophy, corpus linguistics, and computational methods from natural language processing, including large language models.</p>
  </section>

  <section id="publications">
    <h2>Publications</h2>
''' + pubs + '''
  </section>

  <section id="contact" class="contact">
    <h2>Contact</h2>
    <dl>
      <dt>Email</dt>
      <dd>lucien.baumgartner [at] philos.uzh.ch</dd>
    </dl>
  </section>
''' + FOOT

project = HEAD.format(
    title='Cognitive Chimeras | SNSF Ambizione Project | Lucien Baumgartner',
    desc='SNSF Ambizione project Cognitive Chimeras: The Dynamics of Category Extension in the Hierarchy of Concepts, University of Neuchâtel, 2027–2031.'
) + topbar('index.html', 'project') + '''
<main class="wrap">

  <article class="project-page">
    <p class="eyebrow">SNSF Ambizione · University of Neuchâtel · 2027–2031</p>
    <h1>Cognitive Chimeras: The Dynamics of Category Extension in the Hierarchy of Concepts</h1>

    <p>People often use words in ways that are literally incorrect but pragmatically effective. Calling a friend a <em>saint</em> is not a theological claim but a way of highlighting their generosity or patience. In <em>category extension</em>, the lexical meaning of a term is stretched to include entities not covered by its literal denotation, allowing speakers to communicate rich information with minimal effort. Category extension also has legal consequences: when a brand name comes to stand for an entire type of goods, as with <em>thermos</em>, <em>aspirin</em>, or <em>bubble wrap</em>, it risks genericization and, with it, the loss of trademark protection.</p>

    <p>Although category extension is a ubiquitous mechanism of efficient communication, its theoretical treatment remains fragmented. Research in Relevance Theory treats it as one kind of loose language use, alongside approximation, hyperbole, and metaphor, but what distinguishes it from these phenomena remains underexplored, and empirical data supporting this typology are lacking. The literature has focused heavily on proper names used as common nouns (<em>an Einstein</em> for <em>a genius</em>), the role of prototypes remains largely speculative, and we know little about how extended categories become lexicalized over time.</p>

    <h2 class="subhead">Research question</h2>
    <p>The project asks <strong>how and why speakers construct unlexicalized categories</strong> that deviate from a community’s shared conceptual taxonomy. It pursues five interlocking objectives:</p>
    <ol class="objectives">
      <li>establishing an empirically grounded, multidimensional typology of loose language use and situating category extension within it;</li>
      <li>determining how idealization (“the new Roger Federer”) and demonization (“a real Judas”) of individuals influence the use of proper names as common nouns;</li>
      <li>examining how efficient communication through category extension becomes established and standardized in a community’s shared lexicon;</li>
      <li>analyzing how speakers’ emotions, values, and goals drive loose categorization; and</li>
      <li>operationalizing and measuring the genericization of brand labels using computational corpus-linguistic tools.</li>
    </ol>

    <h2 class="subhead">Methods</h2>
    <p>The project combines computational corpus analysis, survey experiments, and conceptual analysis, so that its theoretical claims are tested against natural language data. Beyond advancing our understanding of how we adapt language to cognitive and communicative demands, it aims to give linguists, cognitive scientists, and legal scholars tools to predict, analyze, and mitigate the real-world consequences of category extension.</p>

    <p>Principal investigator: <a href="index.html">Lucien Baumgartner</a></p>
  </article>
''' + FOOT

open(f'{out_dir}/index.html', 'w', encoding='utf-8').write(index)
open(f'{out_dir}/ambizione.html', 'w', encoding='utf-8').write(project)
print('ok')
