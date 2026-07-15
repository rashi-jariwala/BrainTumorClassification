const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("previewImage");

const prediction = document.getElementById("prediction");
const confidence = document.getElementById("confidence");

const loader = document.getElementById("loader");

const predictBtn = document.getElementById("predictBtn");


// ===============================
// Image Preview
// ===============================

function previewImage(event){

    const file = event.target.files[0];

    if(!file){

        return;
    }

    preview.src = URL.createObjectURL(file);

}


// ===============================
// Predict Image
// ===============================

async function predictImage(){

    const file = imageInput.files[0];

    if(!file){

        alert("Please Select MRI Image");

        return;
    }

    loader.style.display="block";

    predictBtn.disabled=true;

    predictBtn.innerHTML=`
    <span class="spinner-border spinner-border-sm"></span>
    Predicting...
    `;

    const formData = new FormData();

    formData.append("image",file);

    const token = localStorage.getItem("token");

    try{

        const response = await fetch("/api/predict",{

            method:"POST",

            headers:{

                "Authorization":"Bearer "+token

            },

            body:formData

        });

        const result = await response.json();

        loader.style.display="none";

        predictBtn.disabled=false;

        predictBtn.innerHTML=`
        <i class="fa-solid fa-brain"></i>
        Predict Brain Tumor
        `;

        if(result.status){

            prediction.innerHTML=result.prediction;

            confidence.innerHTML=result.confidence+" %";

        }
        else{

            alert(result.message);

        }

    }

    catch(error){

        loader.style.display="none";

        predictBtn.disabled=false;

        predictBtn.innerHTML="Predict Brain Tumor";

        alert("Something went wrong.");

        console.log(error);

    }

}


// ===============================
// Logout
// ===============================

function logout(){

    localStorage.clear();

    window.location="/login";

}