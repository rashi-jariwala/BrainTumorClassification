// Check Login
window.onload = function () {

    const token = localStorage.getItem("token");

    if (!token) {

        window.location = "/login";
        return;
    }

    loadUser();
};


// Load Username
function loadUser() {

    let email = localStorage.getItem("email");

    if (!email) {

        email = "User";
    }

    document.getElementById("username").innerHTML =
        "Welcome, " + email;
}


// Prediction Page
function openPrediction() {

    window.location.href = "/prediction";
}


// Profile Page
function openProfile() {

    window.location.href = "/profile";
}


// Logout
function logout() {

    const result = confirm("Are you sure you want to logout?");

    if (!result) {

        return;
    }

    localStorage.removeItem("token");
    localStorage.removeItem("email");

    window.location.href = "/login";
}


// Update Total Prediction Card
async function loadDashboard() {

    const token = localStorage.getItem("token");

    if (!token) {

        return;
    }

    try {

        const response = await fetch("/api/dashboard", {

            method: "GET",

            headers: {

                "Authorization": "Bearer " + token
            }

        });

        const result = await response.json();

        if (result.status) {

            document.getElementById("totalPrediction").innerHTML =
                result.total_prediction;

        }

    }
    catch (error) {

        console.log(error);

    }

}


loadDashboard();