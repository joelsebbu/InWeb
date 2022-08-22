fetch("http://localhost:3001/staff")
    .then(response => response.json())
    .then(data => {
        console.log(data);
    }).catch(err => {
        console.log(err);
    });

    // fetch("http://localhost:3001/staff", {
    //     method: "POST",
    //     headers: {
    //         "Content-Type": "application/json" // setting the content type to json
    //     },
    //     body: JSON.stringify({
    //         "id": 6,
    //         "email": "a@g.com",
    //         "password": "testpassword6",
    //         "first_name": "FirstName 6",
    //         "last_name": "LastName 6",
    //         "mobile_no": "6666666666",
    //         "date_of_joining": "06-06-2021"
    //     })
    // }).then(response => response.json())
    //     .then(data => {
    //         console.log(data);
    //     }).catch(err => {
    //         console.log(err);
    //     });

