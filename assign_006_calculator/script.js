toggle = true
function power(){
    if(toggle){
        reset()
        document.querySelectorAll('.button').forEach(elem => {
            elem.disabled = true;
        });
        toggle = false;
    }
    else{
        document.querySelectorAll('.button').forEach(elem => {
            elem.disabled = false;
        });
        toggle = true;
    }
}
function reset(){
    document.getElementById('screen').value = "";
}

function btnPress(val){
    document.getElementById("screen").value += val;
}

function calculate() {
    let result = eval(document.getElementById("screen").value);
    document.getElementById("screen").value = result;
}
