function toggleForm() {
    var profileInfo = document.getElementById('profile-info');
    var updateForm = document.getElementById('update-form');
    if (profileInfo.style.display === 'none') {
        profileInfo.style.display = 'block';
        updateForm.style.display = 'none';
    } else {
        profileInfo.style.display = 'none';
        updateForm.style.display = 'block';
    }
}
