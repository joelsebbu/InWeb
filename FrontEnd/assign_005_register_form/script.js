function set(s,v){
  document.getElementById(s).style.borderColor = 'red';
  document.getElementById(s+'-'+v).style.display = 'block';
}

function reset(s,v){
  document.getElementById(s).style.borderColor = 'mediumseagreen';
  document.getElementById(s+'-'+v).style.display = 'none';
}

let submit = document.getElementById('submit');
submit.addEventListener('click', function(e) {

  if(document.getElementById('name').value == '') set('name','miss')
  else reset('name','miss')

  if(document.getElementById('name').value.match(/^[a-zA-Z]+$/)) reset('name','min')
  else set('name','min')

  if(document.getElementById('email').value == '') set('email','miss')
  else reset('email','miss')

  if(document.getElementById('phone').value == '') set('phone','miss')
  else reset('phone','miss')

  if(document.getElementById('phone').value.match(/^[0-9]{10}$/)) reset('phone','min')
  else set('phone','min')

  if(document.getElementById('pass').value == '') set('pass','miss')
  else reset('pass','miss')

  if(document.getElementById('pass').value.length < 8) set('pass','min')
  else reset('pass','min')


  if(document.getElementById('confirm').value == '') set('confirm','miss')
  else reset('confirm','miss')

  if(document.getElementById('confirm').value.length < 8) set('confirm','min')
  else reset('confirm','min')

});