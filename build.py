from pathlib import Path
import re,runpy,html
ROOT=Path(__file__).resolve().parent
# Render the same structure for each language; all content is local and static.
def render(lang,source,out):
    namespace=runpy.run_path(str(ROOT/'render_single.py'),init_globals={'SOURCE_PATH':str(source),'OUTPUT_PATH':str(out)})
    doc=namespace['document']
    css=re.search(r'<style>(.*?)</style>',doc,re.S)[1]
    main=re.search(r'<main>(.*?)</main>',doc,re.S)[1]
    nav=re.search(r'<nav class="sidebar"[^>]*>(.*?)</nav>',doc,re.S)[1]
    if lang=='en':
        for a,b in [('Ba ứng dụng','Three applications'),('01 · Nhận hồ sơ','01 · Collect applications'),('02 · Xử lý và quản lý','02 · Review and manage'),('03 · Theo dõi và tự phục vụ','03 · Track and self-serve'),('Audit theo mẫu · Phân biệt quan sát, suy luận và đề xuất · Không chứa credential','Sample-based audit · Observation, inference and proposal distinguished · No credentials')]:
            main=main.replace(a,b)
    fragment='<div class="layout" data-lang="'+lang+'"'+(' hidden' if lang=='en' else '')+'><nav class="sidebar" aria-label="'+('Mục lục' if lang=='vi' else 'Contents')+'">'+nav+'</nav><main lang="'+lang+'">'+main+'</main></div>'
    fragment=re.sub(r'id="([^"]+)"',lambda m:'id="'+lang+'-'+m[1]+'"',fragment)
    fragment=re.sub(r'href="#([^"]+)"',lambda m:'href="#'+lang+'-'+m[1]+'"',fragment)
    return fragment,css

def build(vi_source,en_source,destination):
    # Render intermediates outside tracked source files.
    vi,css=render('vi',vi_source,ROOT/'.vi-render.html')
    en,_=render('en',en_source,ROOT/'.en-render.html')
    extra='''[hidden]{display:none!important}.language-switch{display:flex;gap:4px;padding:4px;border:1px solid #7191a3;border-radius:9px;flex-shrink:0}.language-switch button{background:transparent;color:white;border:0;border-radius:5px;padding:8px 12px;font:600 14px system-ui;cursor:pointer}.language-switch button[aria-pressed="true"]{background:white;color:#0b3b56}.language-switch button:focus-visible{outline:3px solid #ffd86a;outline-offset:3px}.header-meta{display:flex;align-items:center;gap:20px}.header-meta>span{font-size:12px}@media(max-width:700px){header{flex-wrap:wrap;gap:10px}.header-meta{width:100%;justify-content:space-between}.header-meta>span{font-size:11px}}'''
    js='''(()=>{let lang='vi';const panels=[...document.querySelectorAll('[data-lang]')];const buttons=[...document.querySelectorAll('[data-set-lang]')];const meta=document.getElementById('report-meta');function logical(id){return id.replace(/^(vi|en)-/,'')}function current(){const p=document.querySelector('[data-lang="'+lang+'"]');const heads=[...p.querySelectorAll('h2')];return logical((heads.filter(h=>h.getBoundingClientRect().top<=160).pop()||heads[0]).id)}function show(next,initial=false){if(!['vi','en'].includes(next))return;const hash=decodeURIComponent(location.hash.slice(1));const target=initial?(hash?logical(hash):null):current();lang=next;panels.forEach(p=>p.hidden=p.dataset.lang!==lang);buttons.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.setLang===lang)));document.documentElement.lang=lang;document.title='ISH Student Housing — '+(lang==='vi'?'UX Audit · Tiếng Việt':'UX Audit · English');meta.textContent=lang==='vi'?'Theo ứng dụng & hành trình · 23/10/2026':'By application & journey · October 23, 2026';try{localStorage.setItem('ish-audit-language',lang)}catch(e){}if(target){const el=document.getElementById(lang+'-'+target);if(el){let parent=el.closest('details');while(parent){parent.open=true;parent=parent.parentElement.closest('details')}history.replaceState(null,'','#'+lang+'-'+target);requestAnimationFrame(()=>el.scrollIntoView({block:'start'}))}}}buttons.forEach(b=>b.addEventListener('click',()=>show(b.dataset.setLang)));panels.forEach(p=>p.querySelectorAll('details').forEach((d,i)=>d.addEventListener('toggle',()=>{const other=document.querySelector('[data-lang="'+(p.dataset.lang==='vi'?'en':'vi')+'"]');const match=other.querySelectorAll('details')[i];if(match&&match.open!==d.open)match.open=d.open})));let saved='vi';try{saved=localStorage.getItem('ish-audit-language')||'vi'}catch(e){}if(location.hash.startsWith('#en-'))saved='en';if(location.hash.startsWith('#vi-'))saved='vi';show(saved,true)})();'''
    doc='<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>ISH Student Housing — UX Audit · VI / EN</title><style>'+css+extra+'</style></head><body><header><strong>ISH · Student Housing</strong><div class="header-meta"><span id="report-meta">Theo ứng dụng & hành trình · 23/10/2026</span><div class="language-switch" role="group" aria-label="Language / Ngôn ngữ"><button type="button" data-set-lang="vi" aria-pressed="true" lang="vi">VI</button><button type="button" data-set-lang="en" aria-pressed="false" lang="en">EN</button></div></div></header>'+vi+en+'<script>'+js+'</script></body></html>'
    Path(destination).write_text(doc,encoding='utf-8')
    for f in [ROOT/'.vi-render.html',ROOT/'.en-render.html']:
        f.unlink(missing_ok=True)
    return doc

if __name__=='__main__':
    doc=build(ROOT/'report.vi.md',ROOT/'report.en.md',ROOT/'index.html')
    print({'bilingualBytes':len(doc.encode()),'languages':['vi','en']})
