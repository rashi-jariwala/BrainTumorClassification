const form = document.getElementById("forgotForm");
const btn = document.getElementById("updateBtn");

form.addEventListener("submit", async function (e) {

    e.preventDefault();

    const email = document.getElementById("email").value.trim();
    const newPassword = document.getElementById("new_password").value;
    const confirmPassword = document.getElementById("confirm_password").value;

    if (email === "") {

        alert("Email is required.");
        return;
    }

    if (newPassword === "") {

        alert("New Password is required.");
        return;
    }

    if (confirmPassword === "") {

        alert("Confirm Password is required.");
        return;
    }

    if (newPassword !== confirmPassword) {

        alert("Password does not match.");
        return;
    }

    btn.disabled = true;

    btn.innerHTML = `
        <span class="spinner-border spinner-border-sm"></span>
        Updating...
    `;

    try {

        const response = await fetch("/api/forgot-password", {

            method: "PUT",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                email: email,
                new_password: newPassword

            })

        });

        const result = await response.json();

        btn.disabled = false;

        btn.innerHTML = "Update Password";

        if (result.status) {

            alert(result.message);

            setTimeout(() => {

                window.location.href = "/login";

            }, 1500);

        } else {

            alert(result.message);

        }

    } catch (error) {

        console.log(error);

        btn.disabled = false;

        btn.innerHTML = "Update Password";

        alert("Something went wrong.");

    }

});