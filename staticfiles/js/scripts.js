document.addEventListener("DOMContentLoaded", function() {
    const greetingDiv = document.getElementById('greeting');
    let username = greetingDiv.getAttribute('data-username'); // Fetch the username from the data attribute

    // Convert the username to uppercase
    username = username.toUpperCase();

    const now = new Date();
    const hours = now.getHours();
    let greeting = '';

    if (hours < 12) {
        greeting = `Good morning, ${username}!`;
    } else if (hours >= 12 && hours < 17) {
        greeting = `Good afternoon, ${username}!`;
    } else {
        greeting = `Good evening, ${username}!`;
    }

    greetingDiv.innerText = greeting;
});

document.addEventListener("DOMContentLoaded", function() {
    const readMoreLinks = document.querySelectorAll('.read-more');
    readMoreLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const cardBody = this.closest('.card-body');
            const description = cardBody.querySelector('.description');
            const moreText = cardBody.querySelector('.more-text');

            if (moreText.style.display === "none") {
                moreText.style.display = "inline";
                this.innerText = "Read Less";
            } else {
                moreText.style.display = "none";
                this.innerText = "Read More";
            }
        });
    });
});

function validateForm() {
    // Get all input fields within the form
    const inputs = document.querySelectorAll('#mpesa-form input[type="text"], #mpesa-form input[type="number"], #mpesa-form textarea');

    // Check if any input field is empty or contains only whitespace
    for (let input of inputs) {
        if (input.value.trim().length === 0) {
            alert('Please fill in all required fields.');
            return false; // Prevent the form from submitting
        }
    }
    return true; // Allow the form to submit if all fields are properly filled
}

