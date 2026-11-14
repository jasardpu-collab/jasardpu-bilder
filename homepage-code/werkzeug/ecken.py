"""Kleine Eck-Bildchen fuer Kacheln (oben rechts)."""
B='stroke="#4A3F36" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"'
ICON={
'buch':f'<svg viewBox="0 0 60 60" width="54" height="54" aria-hidden="true"><rect x="12" y="8" width="36" height="44" rx="4" fill="#F2C4B0" {B}/><path d="M18 8 V52" {B} fill="none"/><path d="M48 46 H18" {B} fill="none"/><circle cx="29" cy="26" r="2.6" fill="#4A3F36"/><circle cx="39" cy="26" r="2.6" fill="#4A3F36"/><path d="M31 31 Q34 34 37 31" {B} fill="none" stroke-width="2.2"/></svg>',
'karte':f'<svg viewBox="0 0 60 60" width="54" height="54" aria-hidden="true"><path d="M6 14 L20 9 L40 15 L54 10 V46 L40 51 L20 45 L6 50 Z" fill="#B8CCE0" {B}/><path d="M20 9 V45 M40 15 V51" {B} fill="none"/><path d="M30 18 C24 18 22 23 24 27 L30 36 L36 27 C38 23 36 18 30 18 Z" fill="#E58C74" {B} stroke-width="2.4"/><circle cx="30" cy="24.5" r="2.4" fill="#FFFFFF"/></svg>',
'youtube':'<svg viewBox="0 0 60 60" width="54" height="54" aria-hidden="true"><rect x="5" y="13" width="50" height="34" rx="10" fill="#E53935"/><path d="M25 22 L39 30 L25 38 Z" fill="#FFFFFF"/></svg>',
'korb':f'<svg viewBox="0 0 60 60" width="54" height="54" aria-hidden="true"><path d="M18 24 L26 8 M42 24 L34 8" {B} fill="none"/><path d="M6 24 H54 L49 50 Q48 53 45 53 H15 Q12 53 11 50 Z" fill="#E6CFAF" {B}/><path d="M20 32 V45 M30 32 V45 M40 32 V45" {B} fill="none" stroke-width="2.4"/></svg>',
'instagram':'<svg viewBox="0 0 60 60" width="54" height="54" aria-hidden="true"><defs><linearGradient id="jfIg" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#F9CE34"/><stop offset=".5" stop-color="#EE2A7B"/><stop offset="1" stop-color="#6228D7"/></linearGradient></defs><rect x="6" y="6" width="48" height="48" rx="14" fill="url(#jfIg)"/><rect x="15" y="15" width="30" height="30" rx="9" fill="none" stroke="#FFFFFF" stroke-width="3.5"/><circle cx="30" cy="30" r="7" fill="none" stroke="#FFFFFF" stroke-width="3.5"/><circle cx="39.5" cy="20.5" r="2.4" fill="#FFFFFF"/></svg>',
}
CSS='''/* Eck-Bildchen oben rechts in Kacheln */
html body #jf.jf .jf-mit-ecke{position:relative}
html body #jf.jf .jf-mit-ecke .jf-k,html body #jf.jf .jf-mit-ecke .jf-t{padding-right:62px}
html body #jf.jf .jf-ecke{position:absolute;top:14px;right:14px;display:block;width:54px;height:54px;pointer-events:none;transform:rotate(6deg);filter:drop-shadow(0 4px 8px rgba(74,63,54,.15))}
html body #jf.jf .jf-ecke svg{display:block;width:100%;height:100%}
html body #jf.jf a.jf-mit-ecke:hover .jf-ecke{transform:rotate(-4deg) scale(1.08);transition:transform .2s}
'''
def ecke(tag_start,art):
    """tag_start: der oeffnende <a ...>-Tag; liefert neuen Tag + Bildchen"""
    t=tag_start.replace('class="jf-tile','class="jf-tile jf-mit-ecke',1)
    return t+'<span class="jf-ecke">'+ICON[art]+'</span>'
