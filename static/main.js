function validateForm() {
    let x = document.forms['converter-form']['decimal'].value;
    if (x == '') {
        alert("Please enter a valid value.");
        return false
    }
}