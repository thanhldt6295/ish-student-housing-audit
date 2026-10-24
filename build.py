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
    # Vietnamese source remains maintained; the reader displays English only.
    en,css=render('en',en_source,ROOT/'.en-render.html')
    en=en.replace(' hidden','',1)
    js="""(()=>{function restore(){const id=decodeURIComponent(location.hash.slice(1)).replace(/^(vi|en)-/,'');if(!id)return;const el=document.getElementById('en-'+id);if(!el)return;let parent=el.closest('details');while(parent){parent.open=true;parent=parent.parentElement.closest('details')}if(location.hash!=='#en-'+id)history.replaceState(null,'','#en-'+id);el.scrollIntoView({block:'start'})}window.addEventListener('hashchange',restore);restore()})();"""
    doc='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>ISH Student Housing — UX Audit · English</title><style>'+css+'</style></head><body><header><strong>ISH · Student Housing</strong><span>By application &amp; journey · Updated October 24, 2026</span></header>'+en+'<script>'+js+'</script></body></html>'
    Path(destination).write_text(doc,encoding='utf-8')
    (ROOT/'.en-render.html').unlink(missing_ok=True)
    return doc

if __name__=='__main__':
    doc=build(ROOT/'report.vi.md',ROOT/'report.en.md',ROOT/'index.html')
    print({'reportBytes':len(doc.encode()),'displayLanguage':'en'})
