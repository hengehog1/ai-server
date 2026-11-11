document.querySelectorAll('.code').forEach(function(b){
  var btn=b.querySelector('.copy'); if(!btn)return;
  btn.addEventListener('click',function(){
    var t=b.querySelector('pre').innerText.replace(/\n$/,'');
    var done=function(){btn.textContent='Скопировано ✓';btn.classList.add('ok');setTimeout(function(){btn.textContent='Копировать';btn.classList.remove('ok')},1800)};
    if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(t).then(done,fb)}else fb();
    function fb(){var a=document.createElement('textarea');a.value=t;a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();try{document.execCommand('copy');done()}catch(e){}document.body.removeChild(a)}
  });
});
