**API CsIndex**
----
  _Trabalho Prático de Engenharia de Software II do curso de Sistemas de Informação / UFMG, 2018/01._

* **URL**

  _/publications/areas/conferences_

* **Method:**

  `GET` 
  
*  **URL Params**

   **Required:**
 
   `area`

   **Optional:**
 
   `conference`

* **Data Params**

 Only one conference must be sent.

* **Success Response:**

  * **Code:** 200
  
    **Content:** `Number of publications of the conference`
    
   OR
   
  * **Code:** 200
  
    **Content:** `Number of publications of the area`
 
* **Error Response:**

  * **Code:** HTTP 400 
  
    **Content:** `{ Error : "You have to specify an area in the request." }`

  OR

  * **Code:** HTTP 404 
  
    **Content:** `{ Error : "There are no data for this area." }`
    
  OR
  * **Code:** HTTP 404 
  
    **Content:** `{ Error : "There are no data for this conference." }`

* **Sample Call:**

  <_Just a sample call to your endpoint in a runnable format ($.ajax call or a curl request) - this makes life easier and more predictable._> 

* **URL**

  _/scores/areas/departments_

* **Method:**

  `GET` 
  
*  **URL Params**

   **Required:**
 
   `area`

   **Optional:**
 
   `departament`

* **Data Params**

  Only one departament must be sent.
 
* **Success Response:**

  * **Code:** 200
  
    **Content:** `{Score of the departament}`
    
  OR
  
  * **Code:** 200
  
    **Content:** `{List of scores}`
 
* **Error Response:**

  * **Code:** HTTP 400 
  
    **Content:** `{ Error : "You have to specify an area in the request." }`

  OR

  * **Code:** HTTP 404 
  
    **Content:** `{ Error : "There are no data for this area." }`
    
  OR
  
  * **Code:** 404 
  
    **Content:** `{ Error : "The number of departments is incorrect." }`

* **Sample Call:**

  <_Just a sample call to your endpoint in a runnable format ($.ajax call or a curl request) - this makes life easier and more predictable._> 
  
  
* **URL**

  _/professors/areas/departments_

* **Method:**

  `GET` 
  
*  **URL Params**

   **Required:**
 
   `area`

   **Optional:**
 
   `departament`

* **Data Params**

  Only one departament must be sent.
 
* **Success Response:**

  * **Code:** 200
  
    **Content:** `{Number of professors of the departament}`
    
  OR
  
  * **Code:** 200
  
    **Content:** `{Number of professors organized by departaments}`
 
* **Error Response:**

  * **Code:** HTTP 400 
  
    **Content:** `{ Error : "You have to specify an area in the request." }`

  OR

  * **Code:** HTTP 404 
  
    **Content:** `{ Error : "There are no data for this area." }`
    
  OR
  
  * **Code:** 404 
  
    **Content:** `{ Error : "The number of departments is incorrect." }`

* **Sample Call:**

  <_Just a sample call to your endpoint in a runnable format ($.ajax call or a curl request) - this makes life easier and more predictable._> 
  
   
* **URL**

  _/papers/areas_

* **Method:**

  `GET` 
  
*  **URL Params**

   **Required:**
 
   `area`

   **Optional:**
 
   `departament`
   
   OR
   
   `year`
   
   OR
   
   `professor`

* **Data Params**

  Only one optional parameter must be sent.
 
* **Success Response:**

  * **Code:** 200
  
    **Content:** `{Papers of the area}`
    
  OR
  
  * **Code:** 200
  
    **Content:** `{Papers of the year}`
  
  OR
  
  * **Code:** 200
  
    **Content:** `{Papers of the departament}`
    
  OR
  
  * **Code:** 200
  
    **Content:** `{Papers of the professor}`
 
* **Error Response:**

  * **Code:** HTTP 400 
  
    **Content:** `{ Error : "You have to specify an area in the request." }`

  OR

  * **Code:** HTTP 404 
  
    **Content:** `{ Rrror : "There are no data for this area." }`
    
  OR
  
  * **Code:** 404 
  
    **Content:** `{ Error : "There are no data for this year" }`
    
  OR
  
  * **Code:** 404 
  
    **Content:** `{ Error : "There are no data for this department" }`
    
  OR
   
  * **Code:** 404 
  
    **Content:** `{ Error : "There are no data for this professor." }`
  
* **Sample Call:**

  <_Just a sample call to your endpoint in a runnable format ($.ajax call or a curl request) - this makes life easier and more predictable._> 
