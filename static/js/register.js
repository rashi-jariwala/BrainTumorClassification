const form=document.getElementById("registerForm");

const btn=document.getElementById("registerBtn");

form.addEventListener("submit",async(e)=>{

e.preventDefault();

if(password.value!==confirm_password.value){

alert("Password does not match");

return;

}

btn.disabled=true;

btn.innerHTML=`
<span class="spinner-border spinner-border-sm"></span>
Registering...
`;

const data={

username:username.value,

email:email.value,

password:password.value

};

const response=await fetch("/api/register",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(data)

});

const result=await response.json();

alert(result.message);

btn.disabled=false;

btn.innerHTML="Register";

if(result.status){

window.location="/login";

}

});