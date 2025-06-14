


const studentModal = document.getElementById('studentModal');
studentModal.addEventListener('show.bs.modal', event => {
    
    const button  = event.relatedTarget;
    const name = button.getAttribute('data-name');
    const tel = button.getAttribute('data-tel');
    const email = button.getAttribute('data-email');
    const joining_date = button.getAttribute('data-joining')

    // populate student name into the modal
    
    document.getElementById('modalName').textContent = name
    document.getElementById('modalTel').textContent = tel
    document.getElementById('modalEmail').textContent = email
    document.getElementById('modalJoiningDate').textContent = joining_date
});