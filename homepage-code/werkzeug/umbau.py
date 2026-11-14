"""Gemeinsamer Umbau fuer Unterseiten: Menue einsetzen (aktuelle Seite als Text),
alte Seitenleiste und Zurueck-Link raus, Nummern/Buchstaben raus, Nach-oben-Knopf."""
import re,os
W=os.path.dirname(__file__)
MENU=open(os.path.join(W,'menue.html')).read()
CSS=open(os.path.join(W,'menue.css')).read()
JS=open(os.path.join(W,'hoch.js')).read()
HOCH='  <!-- ===== NACH-OBEN-KNOPF (rechts unten) ===== -->\n  <a class="jf-hoch" href="#" aria-label="Nach oben">↑</a>\n'
def menue(seite):
    m=MENU.replace(f'<a class="jf-mh" href="{seite}">','<span class="jf-hier" aria-current="page">',1)
    i=m.find('<span class="jf-hier"'); j=m.find('</a>',i)
    return m[:j]+'</span>'+m[j+4:]
def umbau(t,seite):
    # alte Seitenleiste(n) nach dem Header entfernen
    t=re.sub(r'\n  <!-- ===== SEITEN-LEISTE.*?</nav>\n','\n',t,flags=re.S)
    t=t.replace('</header>\n','</header>\n\n'+menue(seite)+'\n',1)
    t=re.sub(r'\n?  <a class="jf-zurueck"[^\n]*</a>\n','\n',t)
    # Nummern und Buchstaben in Klammern in Labels
    t=re.sub(r'(class="jf-(?:eyebrow|seclabel)[^"]*"[^>]*>)\((?:\d\d|[A-Z])\) ',r'\1',t)
    t=re.sub(r'(<!-- ===== )\((?:\d\d|[A-Z])\) ',r'\1',t)
    t=t.replace('Alle Bücher','Bücher')
    # Knopf + Stil + Skript
    k=t.rfind('</div>\n</div>')
    t=t[:k]+'</div>\n'+HOCH+'</div>'+t[k+len('</div>\n</div>'):]
    t+='\n<style>\n'+CSS+'</style>\n<script>\n'+JS+'</script>\n'
    return t
