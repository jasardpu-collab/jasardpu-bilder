/* Nach-oben-Knopf: erscheint nach etwas Scrollen, scrollt ganz nach oben */
(function(){
  var h=document.querySelector('#jf.jf .jf-hoch');if(!h)return;
  function pruefe(){h.classList.toggle('jf-zeigen',window.scrollY>400)}
  window.addEventListener('scroll',pruefe,{passive:true});pruefe();
  h.addEventListener('click',function(e){e.preventDefault();window.scrollTo({top:0,behavior:'smooth'})});
})();
