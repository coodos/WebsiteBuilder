// setting button event listeners
let addButton = document.getElementById('newElement');
let saveButton = document.getElementById('saveWebsite');
let preview = document.querySelector('.preview');

// defining the global main popup
let popup = document.querySelector('#pop');
// event listener for popup to add a new element
addButton.addEventListener('click', () => {
    popup.style.display = 'block';
    // adding the close event listener
    document.getElementById('popupClose').addEventListener('click', () => {
        popup.style.display = 'none';
    });
});

// event listener to add the set elements
document.getElementById('createElement').addEventListener('click', () => {
    let element = document.getElementById('elemSelect').value;
    if (element == "header") {
        let headerPopup = document.querySelector('.headerPopup');
        popup.style.display = 'none';
        headerPopup.style.display = 'block';
        document.querySelector('.headerPopup .close').addEventListener('click', () => {
            headerPopup.style.display = 'none';
        });
        document.querySelector('.headerPopup input[type=submit]').addEventListener('click', () => {  
            headerPopup.style.display = 'none';
            setTimeout(() => {
                location.reload(true);
            }, 500);
        });
    } 
    if (element == 'main') {
        let mainPopup = document.querySelector('.mainPopup');
        popup.style.display = 'none';
        mainPopup.style.display = 'block';
        document.querySelector('.mainPopup .close').addEventListener('click', () => {
            mainPopup.style.display = 'none';
        });
        document.querySelector('.mainPopup input[type=submit]').addEventListener('click', () => {  
            mainPopup.style.display = 'none';
            setTimeout(() => {
                location.reload(true);
            }, 1000);
        });
    }
    if (element == 'about') {
        let aboutPopup = document.querySelector('.aboutPopup');
        popup.style.display = 'none';
        aboutPopup.style.display = 'block';
        document.querySelector('.aboutPopup .close').addEventListener('click', () => {
            aboutPopup.style.display = 'none';
        });
        document.querySelector('.aboutPopup input[type=submit]').addEventListener('click', () => {
            aboutPopup.style.display = 'none';
            setTimeout(() => {
                location.reload(true);
            }, 1000);
        });
    }
    if (element == 'features') {
        let featuresPopup = document.querySelector('.featuresPopup');
        popup.style.display = 'none';
        featuresPopup.style.display = 'block';
        document.querySelector('.featuresPopup .close').addEventListener('click', () => {
            featuresPopup.style.display = 'none';
        });
        document.querySelector('.featuresPopup input[type=submit]').addEventListener('click', () => {
            featuresPopup.style.display = 'none';
            setTimeout(() => {
                location.reload(true);
            }, 1000);
        });
    }
    if (element == 'contact') {
        let contactPopup = document.querySelector('.contactPopup');
        popup.style.display = 'none';
        contactPopup.style.display = 'block';
        document.querySelector('.contactPopup .close').addEventListener('click', () => {
            contactPopup.style.display = 'none';
        });
        document.querySelector('.contactPopup input[type=submit]').addEventListener('click', () => {
            contactPopup.style.display = 'none';
            setTimeout(() => {
                location.reload(true);
            }, 1000);
        });
    }
    if (element == 'footer') {
        let footerPopup = document.querySelector('.footerPopup');
        popup.style.display = 'none';
        footerPopup.style.display = 'block';
        document.querySelector('.footerPopup .close').addEventListener('click', () => {
            footerPopup.style.display = 'none';
        });
        document.querySelector('.footerPopup input[type=submit]').addEventListener('click', () => {
            footerPopup.style.display = 'none';
            setTimeout(() => {
                location.reload(true);
            }, 1000);
        });
    }
});