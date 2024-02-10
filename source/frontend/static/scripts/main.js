// ---------------------------------------------------------------------------------------
// ----- variables
// ---------------------------------------------------------------------------------------
let is_edit_mode = false;
let is_click_disabled = false;

// ---------------------------------------------------------------------------------------
// ----- functions
// ---------------------------------------------------------------------------------------
window.onunhandledrejection = function (event) {
    console.error("Unhandled Promise Rejection:", event.reason);
};

function add_recipe() {
    // Send AJAX request to delete ingredient
    fetch("/add_recipe", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.status === "success") {
                location.href = "/recipe/new_recipe";
            } else {
                alert("Failed to delete ingredient");
            }
        })
        .catch((error) => {
            console.error("Error:", error);
        });
    return;
}

function toggle_edit_mode(recipe_name, metadata_type, identifier) {
    is_edit_mode = !is_edit_mode;

    var buttons_to_hide = document.querySelectorAll(".up-button, .down-button");
    buttons_to_hide.forEach(function (element) {
        if (is_edit_mode) {
            // To hide the element
            element.classList.add("hidden");
        } else {
            element.classList.remove("hidden");
        }
    });

    if (is_edit_mode) {
    } else {
    }
}