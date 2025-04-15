function showVerification(event) {
    event.preventDefault();
    
    const userConfirmed = confirm("Do you really want to delete this contact?");
    if (userConfirmed){
        event.target.closest("form").submit();
    }
}