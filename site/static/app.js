(function(){
  var body=document.body, page=body.dataset.page, root=body.dataset.root;
  var PAGES=window.PAGES||{};
  function load(p){try{return JSON.parse(localStorage.getItem('aisr:'+p)||'[]')}catch(e){return []}}
  function save(p,a){try{localStorage.setItem('aisr:'+p,JSON.stringify(a))}catch(e){}}

  // theme
  var rootEl=document.documentElement, t=null;
  try{t=localStorage.getItem('aisr:theme')}catch(e){}
  if(!t&&window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches)t='dark';
  if(t)rootEl.dataset.theme=t;
  document.getElementById('theme').onclick=function(){
    var n=rootEl.dataset.theme==='dark'?'light':'dark';rootEl.dataset.theme=n;
    try{localStorage.setItem('aisr:theme',n)}catch(e){}
  };
  var menu=document.getElementById('menu');
  menu.onclick=function(){var o=body.classList.toggle('open');menu.setAttribute('aria-expanded',o)};

  // checkboxes
  var cks=[].slice.call(document.querySelectorAll('article .ck'));
  var checked=new Set(load(page));
  function rowOf(c){return c.closest('tr')||c.closest('li')}
  cks.forEach(function(c){
    var i=+c.dataset.i; c.checked=checked.has(i); rowOf(c).classList.toggle('is-done',c.checked);
    c.addEventListener('change',function(){
      if(c.checked)checked.add(i);else checked.delete(i);
      rowOf(c).classList.toggle('is-done',c.checked);
      save(page,[...checked]);update();applyFilters();
    });
  });

  function counts(p,set){
    var info=PAGES[p]; if(!info||!info.n)return null;
    var pool=info.star.length?info.star:null, tot=pool?pool.length:info.n, d=0;
    if(pool)pool.forEach(function(i){if(set.has(i))d++});else d=[...set].filter(function(i){return i<info.n}).length;
    return {d:d,t:tot,star:!!pool};
  }
  function update(){
    var c=counts(page,checked), bar=document.getElementById('bar');
    if(c){
      bar.hidden=false;
      document.getElementById('fill').style.width=(100*c.d/c.t)+'%';
      document.getElementById('bartxt').textContent=c.d+' of '+c.t+(c.star?' must-do items done':' items done');
    }
    document.querySelectorAll('.path li').forEach(function(li){
      var p=li.dataset.page, s=p===page?checked:new Set(load(p)), r=counts(p,s);
      var pc=li.querySelector('[data-pc]'), node=li.querySelector('.node');
      if(!r){pc.textContent='';return}
      var pct=Math.round(100*r.d/r.t);
      node.style.setProperty('--p',pct);
      pc.textContent=pct?pct+'%':'';
      li.classList.toggle('done',pct===100);
    });
  }

  // filters
  var hasRes=document.querySelector('article table.res tr.r-core, article table.res tr.r-comp, article table.res tr.r-depth');
  var fbox=document.getElementById('filters');
  if(hasRes)fbox.hidden=false;
  function applyFilters(){
    var core=document.getElementById('f-core').checked, cc=document.getElementById('f-cc').checked, dn=document.getElementById('f-done').checked;
    document.querySelectorAll('article table.res tbody tr').forEach(function(tr){
      var hide=false;
      if(core&&!tr.classList.contains('r-core'))hide=true;
      if(cc&&!tr.querySelector('.pill-c'))hide=true;
      if(dn&&tr.classList.contains('is-done'))hide=true;
      tr.classList.toggle('hide',hide);
    });
  }
  ['f-core','f-cc','f-done'].forEach(function(id){document.getElementById(id).addEventListener('change',applyFilters)});

  update();
})();
