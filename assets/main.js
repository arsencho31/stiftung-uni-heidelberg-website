(function(){
  var t=document.querySelector('.nav-toggle'),n=document.querySelector('.side-nav');
  if(t&&n)t.addEventListener('click',function(){var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o)});
  function toast(m){var e=document.createElement('div');e.className='toast';e.setAttribute('role','status');e.textContent=m;document.body.appendChild(e);setTimeout(function(){e.remove()},2200)}
  document.querySelectorAll('[data-copy]').forEach(function(b){b.addEventListener('click',function(){
    var v=b.getAttribute('data-copy');
    (navigator.clipboard?navigator.clipboard.writeText(v):Promise.reject()).then(function(){toast('Kopiert')},function(){toast('Bitte manuell kopieren')});
  })});
})();
