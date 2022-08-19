// alert("hello world");
// const a =10; //constant
// alert(a);
// var b =20; //variable
// alert(b);
// let c =30; //block scope
// alert(c);
// let a= "lorem ipsum dolor sit amet";
// let b= a.slice(-5,-1)
// let c ="        consectetur adipisicing elit.";
// alert(a.concat(' ',c))
// alert(a.toUpperCase())
// alert(c.trim())
// switch (new Date().getDate()){
//     case 1:
//         day="Monday";
//         break;
//     case 2:
//         day="Tuesday";
//         break;
//     case 3:
//         day="Wednesday";
//         break;
//     case 4:
//         day="Thursday";
//         break;
//     case 5:
//         day="Friday";
//         break;
//     case 6:
//         day="Saturday";
//         break;
//     case 7:
//         day="Sunday";
//         break;
//     default:
//         day="error";
// }



// var sq= (a) =>{
//     return a*a;
// };
// console.log(sq(5));

// var cube = a => a*a*a;
// console.log(cube(5));

// var a =[1,2,3,4,5,6,7,8,9,10];
// var b = a.map(x=>x+x);
// console.log(b);



// var fruits = ["apple","banana","mango","orange","strawberry"];
// console.log(fruits.indexOf("mango"));
// console.log(fruits[3]);

// fruits.push("pineapple");
// console.log(fruits);
// fruits.pop();
// console.log(fruits);
// fruits.unshift("kiwi");
// console.log(fruits);
// fruits.shift();
// console.log(fruits);
// fruits.splice(2,1); //start from index 2 and delete 1 element
// console.log(fruits);
// fruits.splice(2,0,"blackberry","mango"); //start from index 2 and add kiwi and mango
// console.log(fruits);


// for(var i=0;i<fruits.length;i++){
//     console.log(fruits[i]);
// }
// fruits.forEach(i => console.log(i));



// var snacks = ["chips","pizza","soda","icecream"];
// //concat for immutable array
// var newArray = snacks.concat(["chocolate","biscuit"]);
// // console.log(newArray);
// //destructure array
// [first,second,third,...rest] = newArray;
// console.log(first);
// console.log(second);
// console.log(third);
// console.log(rest);




// var student ={
//     name: "John",
//     age: 20,
//     hobbies: ["singing","dancing","reading"],
//     speak: function(){
//         console.log("hello");
//     }
// }
// console.log(student.name);
// console.log(student.age);
// console.log(student.hobbies);
// student.speak();
// student.address={
//     city:"bangalore",
//     state:"karnataka",
//     pincode:560068
// }
// console.log(student.address);


// Objects
// var car={}
// car.name="maruti";
// car.model="swift";
// car.run=function(){
//     console.log(this.name+" "+this.model+" is running");
// }
// car.stop=function(){
//     console.log(this.name+" "+this.model+" has stopped");
// }
// console.log(car);
// car.run();
// car.stop();
// var a =car.stop;
// a();


//OOps

// class Person{
//     constructor(name,age){
//         this.name=name;
//         this.age=age;
//     }
//     speak(){
//         console.log(this.name+" says hello");
//     }
// }
// a = new Person("John",20);
// a.speak()


let bt = document.querySelector("#submit");
bt.addEventListener("click",function(){
    alert("hello");
});

