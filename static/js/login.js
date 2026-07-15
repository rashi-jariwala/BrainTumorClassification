const form=document.getElementById("loginForm");

const btn=document.getElementById("loginBtn");

form.addEventListener("submit",async function(e){

e.preventDefault();

btn.disabled=true;

btn.innerHTML=`
<span class="spinner-border spinner-border-sm"></span>
Logging In...
`;

const data={

email:document.getElementById("email").value,

password:document.getElementById("password").value

};

const response=await fetch("/api/login",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(data)

});

const result=await response.json();

alert(result.message);

btn.disabled=false;

btn.innerHTML="Login";

if(result.status){

localStorage.setItem("token", result.token);
localStorage.setItem("email", data.email);

window.location="/dashboard";

}

});