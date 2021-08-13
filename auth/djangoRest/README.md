# Try to set token to header

## expiredToken    
* get a token in frontend, and able to send request to another api which needs token
* send request using ajax
  * not able to redirect in both frontend and backend
* maybe `single page application with frontend routing` is suitable for this...

## helloDjangoRest
* not able return token to frontend
* not able to redirect, do return another api 
* Even you login, when you type `http://127.0.0.0:8000/hello/` on the browser, it will think you are logout because there is no token in the request
  * Need frontend routing
