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
ICON['tasche']=f'<svg viewBox="0 0 60 60" width="54" height="54" aria-hidden="true"><path d="M22 20 V15 Q22 8 30 8 Q38 8 38 15 V20" {B} fill="none"/><path d="M10 20 H50 L47 52 H13 Z" fill="#F2A877" {B}/><circle cx="25" cy="33" r="2.6" fill="#4A3F36"/><circle cx="35" cy="33" r="2.6" fill="#4A3F36"/><path d="M27 39 Q30 42 33 39" {B} fill="none" stroke-width="2.2"/></svg>'
ICON['stoff']=f'<svg viewBox="0 0 60 60" width="54" height="54" aria-hidden="true"><path d="M14 14 H40 V46 H14 Z" fill="#A9B8A2" {B}/><path d="M40 14 Q50 14 50 22 V54 L40 46" fill="#DDE5D8" {B}/><ellipse cx="14" cy="30" rx="5" ry="16" fill="#C9D6C2" {B}/><path d="M21 22 L27 28 M29 22 L35 28 M21 32 L27 38 M29 32 L35 38" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="round"/></svg>'
ICON['kamera']=f'<svg viewBox="0 0 60 60" width="54" height="54" aria-hidden="true"><path d="M22 16 L25 10 H35 L38 16" {B} fill="#D8C6AE"/><rect x="6" y="16" width="48" height="34" rx="7" fill="#D8C6AE" {B}/><circle cx="30" cy="33" r="10" fill="#B8CCE0" {B}/><circle cx="27" cy="30" r="2.5" fill="#FFFFFF"/><circle cx="46" cy="23" r="2" fill="#4A3F36"/></svg>'
ICON['haus']=f'<svg viewBox="0 0 60 60" width="54" height="54" aria-hidden="true"><path d="M10 28 L30 10 L50 28 V52 H10 Z" fill="#FFFFFF" {B}/><path d="M18 18 Q30 2 42 18" fill="#F2C4B0" {B}/><circle cx="24" cy="34" r="2.6" fill="#4A3F36"/><circle cx="36" cy="34" r="2.6" fill="#4A3F36"/><path d="M27 40 Q30 43 33 40" {B} fill="none" stroke-width="2.2"/></svg>'
ICON['welten']=f'<svg viewBox="0 0 60 60" width="54" height="54" aria-hidden="true"><circle cx="30" cy="30" r="22" fill="#B8CCE0" {B}/><path d="M14 22 Q22 26 20 34 Q26 38 22 46 M36 10 Q34 20 42 22 Q50 26 46 38" {B} fill="none" stroke-width="2.4"/><path d="M30 24 C27 20 22 24 25 27 L30 32 L35 27 C38 24 33 20 30 24 Z" fill="#E58C74" stroke="#4A3F36" stroke-width="2"/></svg>'
