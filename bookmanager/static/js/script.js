document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialization
    let sidenav= document.querySelector('.sidenav');
    M.Sidenav.init(sidenav);


  // select initialization
  let datalists = document.querySelectorAll("datalist");
  M.FormSelect.init(datalists);
  });


