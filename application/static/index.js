const toggleButton = document.getElementsByClassName('navbar-toggle')[0];


const navbarLinks = document.getElementsByClassName('navbar-links');

toggleButton.addEventListener('click', function(){
    for(var i=0; i<navbarLinks.length; i++)
    navbarLinks[i].classList.toggle('active')
})



function myFunction() {
    /* Get the text field */
    var copyText = document.getElementById("myInput");
  
    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */
  
     /* Copy the text inside the text field */
    navigator.clipboard.writeText(copyText.value);
  
    /* Alert the copied text */
    alert("Copied the text: " + copyText.value);
  }