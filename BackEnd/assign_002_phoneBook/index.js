alert();
// const send_data= {"name":"kile","number":34567}
// const json_ =JSON.stringify(send_data)

// const xhr = new XMLHttpRequest();

// xhr.open('POST','http://127.0.0.1:5000/contacts');
// xhr.setRequestHeader('Content-Type','application/json');
// xhr.send(json_)


var xhr = new XMLHttpRequest();
var url = "https://127.0.0.1:5000/contacts";
xhr.open("POST", url, true);
xhr.setRequestHeader("Content-Type", "application/json");
xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
        var json = JSON.parse(xhr.responseText);
        console.log(json.email + ", " + json.password);
    }
};
var data = JSON.stringify({"name": "Kyle", "number": "34567"});
xhr.send(data);