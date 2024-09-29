document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    const errorMessages = [];
    const fullName = document.getElementById('fullName').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    // Validation
    if (fullName.length < 5) {
        errorMessages.push("Full Name must be at least 5 characters long.");
    }

    if (!email.includes('@') || !email.includes('.')) {
        errorMessages.push("Enter a correct Email ID.");
    }

    if (!/^\d{10}$/.test(phone) || phone === "123456789") {
        errorMessages.push("Phone Number must be a 10-digit number and not '123456789'.");
    }

    if (password.length < 8 || password.toLowerCase() === 'password' || password.toLowerCase() === fullName.toLowerCase()) {
        errorMessages.push("Password is not strong. It must be at least 8 characters long and cannot be 'password' or your name.");
    }

    if (password !== confirmPassword) {
        errorMessages.push("Passwords do not match.");
    }

    // Display errors if any
    const errorMessagesDiv = document.getElementById('errorMessages');
    errorMessagesDiv.innerHTML = errorMessages.join('<br>');
    if (errorMessages.length === 0) {
        // If no errors, you can proceed with form submission or further processing
        errorMessagesDiv.innerHTML = "Form submitted successfully!";
    }
});

