
class Student{
    constructor(id,name,classes,age, gender, home){
        this.id = id;
        this.name = name;
        this.classes = classes;
        this.age = age;
        this.gender = gender;
        this.home = home;
    }
   
}
class College{
    constructor(){
        this.students =[]
    }
} 
college = new College();   

function isEmpty(str) {
    if(str.length == 0) {
        return true;
    }
    return false;
}

function getStudent(){
    let id = document.getElementById("id").value;
    let name = document.getElementById("name").value;
    let classes = document.getElementById("classes").value;
    let age = document.getElementById("age").value;
    let gender = document.getElementById("gender").value;
    let home = document.getElementById("home").value;
    let success = true;
    try{
        if (isEmpty(id) || isEmpty(name) || isEmpty(classes) || isEmpty(age) || isEmpty(gender) || isEmpty(home)){
            throw "Please fill all the fields";
        }
        if(age < 0 || age > 100){
            throw "Age should be between 0 and 100";
        }
        if(isNaN(age) || isNaN(id)|| isNaN(classes)){
            throw "Age,classes and id should be numbers";
        }

    }
    catch(err){
        success = false;
        alert("Error: "+err);
    }
    if(success){
        college.students.push(new Student(id,name.trim().toLowerCase(),classes,age,gender.trim().toLowerCase(),home.trim().toLowerCase()));
        console.log(college.students);
        alert("student added");
    }
    else{
        clearStudent();
    }
    
 }
function deleteStudent(){
    let id = document.getElementById("id").value;
    for(let i = 0; i < college.students.length; i++){
        if(college.students[i].id == id){
            college.students.splice(i,1);
        }
    }
    alert("student deleted");
    console.log(college.students);
}
function clearStudent(){
    document.getElementById("id").value = "";
    document.getElementById("name").value = "";
    document.getElementById("classes").value = "";
    document.getElementById("age").value = "";
    document.getElementById("gender").value = "";
    document.getElementById("home").value = "";
}
console.log(college.students);

function getAllStudents(){
    alert("Result in the console");
    for(let i = 0; i < college.students.length; i++){
        console.log(college.students[i]);
    }
}

function emptyUpdateError(){
    this.name = "emptyUpdateError";
}
emptyUpdateError.prototype = new Error();

function updateStudent(){
    let id = document.getElementById("id").value;
    let name = document.getElementById("name").value;
    let classes = document.getElementById("classes").value;
    let age = document.getElementById("age").value;
    let gender = document.getElementById("gender").value;
    let home = document.getElementById("home").value;
    let success = true;
    try{
        if(isEmpty(id)) throw "fill id";
    }
    catch(err){
        success = false;
        alert("Error: "+err);
    }
    if(success){
        for(let i = 0; i < college.students.length; i++){
            if(college.students[i].id == id){
                if(!isEmpty(name)) college.students[i].name = name;
                if(!isEmpty(classes)) college.students[i].classes = classes;
                if(!isEmpty(age)) college.students[i].age = age;
                if(!isEmpty(gender)) college.students[i].gender =gender;
                if(!isEmpty(home)) college.students[i].home = home;
            }
        }
        alert("student updated");
    }
    else{
        clearStudent();
    }
}
function searchStudent(){
    let id = document.getElementById("id").value;
    let success = true;
    let ans;
    try{
        if(isEmpty(id)) throw "fill id";
    }
    catch(err){
        alert("Error: "+err);
    }
    if(success){
        for(let i = 0; i < college.students.length; i++){
            if(college.students[i].id == id){
                console.log(college.students[i]);
                ans =i;
                break;
            }
        }
        alert("Answer in the console");
    }
    
}