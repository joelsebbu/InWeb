function emptyError(err){
  console.log(err);
  
}


let submitButton = document.getElementById('submitButton');
submitButton.addEventListener('click',function(){
  let name = document.getElementById("name").value;
  let email = document.getElementById("email").value;
  let phone = document.getElementById("phone").value;
  let password = document.getElementById("pass").value;
  let confirmPassword = document.getElementById("confirm").value;
  let success =true
  try{
    if(name == "") throw "Name";

    if(email == "") throw "Email";

    if(phone == "") throw "Phone";

    if(password == "") throw "Password";
    
    if(confirmPassword == "") throw "Confirm";
    
    if(password != confirmPassword) throw "Password and Confirm Password must be same";  
  }
  catch(err){
    console.log(typeof(err));
    emptyError(err);
  }
});
