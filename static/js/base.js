  document.addEventListener('DOMContentLoaded', function() {
        flatpickr("#id_valid_until", {
            enableTime: true, // Enable time selection
            dateFormat: "Y-m-d H:i", // Set date format to include time
            minuteIncrement: 1, // Increment minutes by 1
            time_24hr: true // 24-hour format
        });
    });
