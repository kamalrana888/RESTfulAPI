RESTful API- What it is?

Introduction
As we know, REST stands for Representational State Transfer is an architectural style (not a standard), was conceived by Roy Fielding as a resource-oriented, lightweight style. The term, resource-oriented and lightweight shall be discussed shortly. In REST style, HTTP protocol is used as a base for data transfer between a client and server because of ubiquitous use of HTTP in World Wide Web. 
To understand REST architectural style, it is imperative to understand few terms such as resource, json and representation before we move forward. A resource is something which is requested by a client from a server to retrieve its content, or to delete something or to update it. Hence, a resource can be such as a product in an online store, a book of a library, some entity in an organization. JSON stands for java script object notation, which is an open standard for data interchange format. Example of JSON representation of an employee object is as given below.
{
	‘employeeName’:’Arun Kumar’,
	‘empCode’: ‘12345’,
	‘department’: ‘Design’,
	‘designation’: ‘senior manager’
}
 When we talk about representation, we mean the way of expressing a resource in light weight way at a timestamp. When a request is made to the server for a resource, server does not respond with the resource itself, but it sends the representation of the resource. For example, an API call is made at hypothetical <hostname>/PAN URI with GET request having a hypothetical PAN, LIMCA9999L, as parameter the server may respond with a representation of that resource (i.e. LIMCA9999L) in JSON format as shown below
{
‘PAN’:’ LIMCA9999L’,
‘PAN_NAME’:’ABC PVT LTD’,
‘DOI’:’01-01-1970’,
‘ADDRESS’:’ABC Bhawan, Annexure-A, Delhi’
}  
 
Designing a RESTful API
In this section we will try to conceptualize a RESTful API for PAN interaction as discussed above. This Hypothetical API shall assume PAN as a resource around which we will design our URLs for RESTful Services. We may call it as PANInterface. We shall be using Python with Flask microframework as our main programming language to develop this RESTful API. It is assumed that reader have some basic understanding of python language and can install it on their machine for actual development. Installation of python and basic course on python is beyond the scope of this article and reader is requested to use internet for understanding the python language.
   Identification of Key Resource
It is the most important part in design of RESTful API. In our hypothetical PANInterface API, key resource shall be a PAN, which is permanent account number. We are using PANInterface as an example keeping an eye on the intended readers.
   Model URI’s
We can have following model URIs for our PANInterface API.
    • HTTP GET <hostname>/PAN/<pan>  : Get details of PAN with GET http method
    • HTTP POST <hostname>/PAN (JSON in body of message) : Create a new PAN with  POST method
    • HTTP PUT<hostname>/PAN (JSON in body of message) : Update a new PAN with PUT method
    • HTTP DELETE<hostname>/PAN/<pan>  : Delete a PAN with DELETE http method
 
 Sample code is given in paninterface.py file on this repository
 
 Screenshots of the applications are provided below.
 
 
 
         4.4. Output Screens
Working of above API can be tested using cURL or Postman App. We shall be using Postman App to see the working of PANInterface API
    • HTTP GET <hostname>/PAN/<pan>  : Get details of PAN with GET http method


    • HTTP POST <hostname>/PAN (JSON in body of message) : Create a new PAN with  POST method

    • HTTP PUT<hostname>/PAN (JSON in body of message) : Update a new PAN with PUT method

    • HTTP DELETE<hostname>/PAN/<pan>  : Delete a PAN with DELETE http method
