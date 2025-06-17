// static/script.js
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function (e) {
            const title = form.querySelector('input[name="title"]').value.trim();
            const director = form.querySelector('input[name="director"]').value.trim();
            const review = form.querySelector('textarea[name="review"]').value.trim();

            if (!title || !director || !review) {
                alert("Please fill in all fields before submitting your review.");
                e.preventDefault(); // Stop form from submitting
            }
        });
    }
});
