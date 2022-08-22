<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

<center><span style="font-size: 60pt;">CRM</span></center>
<center><h2>REST API Documentation</h2></center>

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>




# Index

- [Courses](#courses)
    - [List all courses](#list-all-courses)
    - [View specific course](#view-specific-course)
    - [Create new course](#create-new-course)
    - [Update course](#update-course)
    - [Delete course](#delete-course)


- [Enquiries](#enquiries)
    - [List all enquiries](#list-all-enquiries)
    - [View specific enquiry](#view-specific-enquiry)
    - [Create new enquiry](#create-new-enquiry)
    - [Update enquiry](#update-enquiry)
    - [Delete enquiry](#delete-enquiry)


- [Users](#users)
    - [List all users](#list-all-users)
    - [View specific user](#view-specific-user)
    - [Create new user](#create-new-user)
    - [Update user](#update-user)
    - [Delete user](#delete-user)


- [Categories](#categories)
    - [List all categories](#list-all-categories)
    - [View specific category](#view-specific-category)
    - [Create new category](#create-new-category)
    - [Update category](#update-category)
    - [Delete category](#delete-category)


- [Qualifications](#qualifications)
    - [List all qualifications](#list-all-qualifications)
    - [View specific qualification](#view-specific-qualification)
    - [Create new qualification](#create-new-qualification)
    - [Update qualification](#update-qualification)
    - [Delete qualification](#delete-qualification)


- [Batches](#batches)
    - [List all batches](#list-all-batches)
    - [View specific batch](#view-specific-batch)
    - [Create new batch](#create-new-batch)
    - [Update batch](#update-batch)
    - [Delete batch](#delete-batch)



## Courses

- ### List all courses  
    ```
    GET    /v1/courses
    ```  
 
    Response body:
    ```js
    [
        {
            "id": Number,
            "code": String,
            "name": String,
            "description": String,
            "qualification": String,
            "trainer": Number,  // trainer id
            "duration": Number, // days
            "startDate": String,
            "amount": Number
        },
        ...
    ]
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 200         | OK          |


- ### View specific course
    ```
    GET    /v1/courses/{id}
    ```  

    Response body:
    ```js
    {
        "id": Number,
        "code": String,
        "name": String,
        "description": String,
        "qualification": String,
        "trainer": Number,  // trainer id
        "duration": Number, // days
        "startDate": String,
        "amount": Number
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 200         | OK          |
    | 404         | Not found   |

- ### Create new course
    ```
    POST   /v1/courses
    ```  

    Request header:
    ```http
    Authorization: Token <token>
    Content-Type: application/json
    ```

    Request body:
    ```js
    {
        "code": String,
        "name": String,
        "description": String,
        "qualification": String,
        "trainer": Number,  // trainer id
        "duration": Number, // days
        "startDate": String,
        "amount": Number
    }
    ```

    Response body:
    ```js
    {
        "id": Number,
        "code": String,
        "name": String,
        "description": String,
        "qualification": String,
        "trainer": Number,  // trainer id
        "duration": Number, // days
        "startDate": String,
        "amount": Number
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 201         | Created     |
    | 400         | Bad Request |
    | 401         | Unauthorized |
    | 403         | Forbidden   |
    | 409         | Conflict    |

- ### Update course
    ```
    PUT    /v1/courses/{id}
    PATCH  /v1/courses/{id}
    ```  

    Request header:
    ```http
    Authorization: Token <token>
    Content-Type: application/json
    ```

    Request body:
    ```js
    {
        "code": String,
        "name": String,
        "description": String,
        "qualification": String,
        "trainer": Number,  // trainer id
        "duration": Number, // days
        "startDate": String,
        "amount": Number
    }
    ```

    Response body:
    ```js
    {
        "id": Number,
        "code": String,
        "name": String,
        "description": String,
        "qualification": String,
        "trainer": Number,  // trainer id
        "duration": Number, // days
        "startDate": String,
        "amount": Number
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 201         | Created     |
    | 400         | Bad Request |
    | 401         | Unauthorized |
    | 403         | Forbidden   |
    | 404         | Not found   |
    | 409         | Conflict    |


- ### Delete course
    ```
    DELETE /v1/courses/{id}
    ```  

    Request header:
    ```http
    Authorization: Token <token>
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 204         | No Content (Deleted successfully) |
    | 401         | Unauthorized |
    | 403         | Forbidden   |
    | 404         | Not found   |


---


## Enquiries

- ### List all enquiries  
    ```
    GET    /v1/enquiries
    ```  

    Request header:
    ```http
    Authorization: Token <token>
    ```
 
    Response body:
    ```js
    [
        {
            "id": Number,
            "title": String,
            "description": String,
            "course": Number,       // course id
            "user": Number          // user id
        },
        ...
    ]
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 200         | OK          |
    | 401         | Unauthorized |
    | 403         | Forbidden   |

- ### View specific enquiry
    ```
    GET    /v1/enquiries/{id}
    ```  

    Request header:
    ```http
    Authorization: Token <token>
    ```

    Response body:
    ```js
    {
        "id": Number,
        "title": String,
        "description": String,
        "course": Number,       // course id
        "user": Number          // user id
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 200         | OK          |
    | 401         | Unauthorized |
    | 403         | Forbidden   |
    | 404         | Not found   |

- ### Create new enquiry
    ```
    POST   /v1/enquiries
    ```  

    Request header:
    ```http
    Authorization: Token <token>
    Content-Type: application/json
    ```

    Request body:
    ```js
    {
        "title": String,
        "description": String,
        "course": Number,       // course id
        "user": Number          // user id
    }
    ```

    Response body:
    ```js
    {
        "id": Number,
        "title": String,
        "description": String,
        "course": Number,       // course id
        "user": Number          // user id
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 201         | Created     |
    | 400         | Bad Request |
    | 401         | Unauthorized |
    | 403         | Forbidden   |

- ### Update enquiry
    ```
    PUT    /v1/enquiries/{id}
    PATCH  /v1/enquiries/{id}
    ```  

    Request header:
    ```http
    Authorization: Token <token>
    Content-Type: application/json
    ```

    Request body:
    ```js
    {
        "title": String,
        "description": String,
        "course": Number,       // course id
        "user": Number          // user id
    }
    ```

    Response body:
    ```js
    {
        "id": Number,
        "title": String,
        "description": String,
        "course": Number,       // course id
        "user": Number          // user id
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 201         | Created     |
    | 400         | Bad Request |
    | 401         | Unauthorized |
    | 403         | Forbidden   |
    | 404         | Not found   |

- ### Delete enquiry
    ```
    DELETE /v1/enquiries/{id}
    ```  

    Request header:
    ```http
    Authorization: Token <token>
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 204         | No Content (Deleted successfully) |
    | 401         | Unauthorized |
    | 403         | Forbidden   |
    | 404         | Not found   |


---


## Users
- ### List all users
    ```
    GET    /v1/users
    ```  

    Request header:
    ```http
    Authorization: Token <token>
    ```

    Response body:
    ```js
    [
        {
            "id": Number,
            "name": String,
            "email": String,
            "phone": String,
            "date_of_birth": String
        },
        ...
    ]
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 200         | OK          |
    | 401         | Unauthorized |
    | 403         | Forbidden   |

- ### View specific user
    ```
    GET    /v1/users/{id}
    ``` 

    Request header:
    ```http
    Authorization: Token <token>
    ```

    Response body:
    ```js
    {
        "id": Number,
        "name": String,
        "email": String,
        "phone": String,
        "date_of_birth": String
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 200         | OK          |
    | 401         | Unauthorized |
    | 403         | Forbidden   |
    | 404         | Not found   |

- ### Create new user
    ```
    POST   /v1/users
    ```  
        
    Request header:
    ```http
    Content-Type: application/json
    ```

    Request body:
    ```js
    {
        "name": String,
        "email": String,
        "phone": String,
        "date_of_birth": String,
        "password": String
    }
    ```

    Response body:
    ```js
    {
        "id": Number,
        "name": String,
        "email": String,
        "phone": String,
        "date_of_birth": String
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 201         | Created     |
    | 400         | Bad Request |

- ### Update user
    ```
    PUT    /v1/users/{id}
    PATCH  /v1/users/{id}
    ```  
        
    Request header:
    ```http
    Authorization: Token <token>
    Content-Type: application/json
    ```

    Request body:
    ```js
    {
        "name": String,
        "email": String,
        "phone": String,
        "date_of_birth": String,
        "password": String
    }
    ```

    Response body:
    ```js
    {
        "id": Number,
        "name": String,
        "email": String,
        "phone": String,
        "date_of_birth": String
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 201         | Created     |
    | 400         | Bad Request |
    | 401         | Unauthorized |
    | 403         | Forbidden   |
    | 404         | Not found   |

- ### Delete user
    ```
    DELETE /v1/users
    ```  
        
    Request header:
    ```http
    Authorization: Token <token>
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 204         | No Content (Deleted successfully) |
    | 401         | Unauthorized |
    | 403         | Forbidden   |
    | 404         | Not found   |


---


## Categories
- ### List all categories
    ```
    GET    /v1/categories
    ```  

    Response body:
    ```js
    [
        {
            "id": Number,
            "name": String
        },
        ...
    ]
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 200         | OK          |

- ### View specific category
    ```
    GET    /v1/categories/{id}
    ```  
        
    Response body:
    ```js
    {
        "id": Number,
        "name": String
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 200         | OK          |
    | 404         | Not found   |

- ### Create new category
    ```
    POST   /v1/categories
    ```  
        
    Request header:
    ```http
    Authorization: Token <token>
    Content-Type: application/json
    ```

    Request body:
    ```js
    {
        "name": String
    }
    ```

    Response body:
    ```js
    {
        "id": Number,
        "name": String
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 201         | Created     |
    | 400         | Bad Request |
    | 401         | Unauthorized |
    | 403         | Forbidden   |

- ### Update category
    ```
    PUT    /v1/categories/{id}
    PATCH  /v1/categories/{id}
    ```  
        
    Request header:
    ```http
    Authorization: Token <token>
    Content-Type: application/json
    ```

    Request body:
    ```js
    {
        "name": String
    }
    ```

    Response body:
    ```js
    {
        "id": Number,
        "name": String
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 201         | Created     |
    | 400         | Bad Request |
    | 401         | Unauthorized |
    | 403         | Forbidden   |
    | 404         | Not found   |

- ### Delete category
    ```
    DELETE /v1/categories/{id}
    ```  
        
    Request header:
    ```http
    Authorization: Token <token>
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 204         | No Content (Deleted successfully) |
    | 401         | Unauthorized |
    | 403         | Forbidden   |
    | 404         | Not found   |


---


## Qualifications
- ### List all qualifications
    ```
    GET    /v1/qualifications
    ```  
 
    Response body:
    ```js
    [
        {
            "id": Number,
            "code": String,
            "name": String
        },
        ...
    ]
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 200         | OK          |

- ### View specific qualification
    ```
    GET    /v1/qualifications/{id}
    ```  
 
    Response body:
    ```js
    {
        "id": Number,
        "code": String,
        "name": String
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 200         | OK          |
    | 404         | Not found   |

- ### Create new qualification
    ```
    POST   /v1/qualifications
    ```  
        
    Request header:
    ```http
    Authorization: Token <token>
    Content-Type: application/json
    ```

    Request body:
    ```js
    {
        "code": String,
        "name": String
    }
    ```

    Response body:
    ```js
    {
        "id": Number,
        "code": String,
        "name": String
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 201         | Created     |
    | 400         | Bad Request |
    | 401         | Unauthorized |
    | 403         | Forbidden   |

- ### Update qualification
    ```
    PUT    /v1/qualifications/{id}
    PATCH  /v1/qualifications/{id}
    ```  
        
    Request header:
    ```http
    Authorization: Token <token>
    Content-Type: application/json
    ```

    Request body:
    ```js
    {
        "code": String,
        "name": String
    }
    ```

    Response body:
    ```js
    {
        "id": Number,
        "code": String,
        "name": String
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 201         | Created     |
    | 400         | Bad Request |
    | 401         | Unauthorized |
    | 403         | Forbidden   |
    | 404         | Not found   |

- ### Delete qualification
    ```
    DELETE /v1/qualifications/{id}
    ```  
        
    Request header:
    ```http
    Authorization: Token <token>
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 204         | No Content (Deleted successfully) |
    | 401         | Unauthorized |
    | 403         | Forbidden   |
    | 404         | Not found   |


---


## Batches
- ### List all batches
    ```
    GET    /v1/batches
    ```  

    Response body:
    ```js
    [
        {
            "id": Number,
            "code": String,
            "name": String
        },
        ...
    ]
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 200         | OK          |

- ### View specific batch
    ```
    GET    /v1/batches/{id}
    ``` 
    
    Response body:
    ```js
    {
        "id": Number,
        "code": String,
        "name": String
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 200         | OK          |
    | 404         | Not found   |

- ### Create new batch
    ```
    POST   /v1/batches
    ```  
        
    Request header:
    ```http
    Authorization: Token <token>
    Content-Type: application/json
    ```

    Request body:
    ```js
    {
        "code": String,
        "name": String
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 201         | Created     |
    | 400         | Bad Request |
    | 401         | Unauthorized |
    | 403         | Forbidden   |

- ### Update batch
    ```
    PUT    /v1/batches/{id}
    PATCH  /v1/batches/{id}
    ```  
        
    Request header:
    ```http
    Authorization: Token <token>
    Content-Type: application/json
    ```

    Request body:
    ```js
    {
        "code": String,
        "name": String
    }
    ```

    Response body:
    ```js
    {
        "id": Number,
        "code": String,
        "name": String
    }
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 201         | Created     |
    | 400         | Bad Request |
    | 401         | Unauthorized |
    | 403         | Forbidden   |
    | 404         | Not found   |

- ### Delete batch
    ```
    DELETE /v1/batches/{id}
    ```  
        
    Request header:
    ```http
    Authorization: Token <token>
    ```

    HTTP Status:  
    | Status Code | Description |  
    |:-----------:|:------------|
    | 204         | No Content (Deleted successfully) |
    | 401         | Unauthorized |
    | 403         | Forbidden   |
    | 404         | Not found   |
