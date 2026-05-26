// DARK MODE TOGGLE

const darkBtn = document.getElementById('darkModeBtn');

darkBtn.addEventListener('click', () => {

    document.body.classList.toggle('dark-mode');

    // SAVE MODE

    if(document.body.classList.contains('dark-mode')){

        localStorage.setItem('theme', 'dark');

    }else{

        localStorage.setItem('theme', 'light');
    }
});

// LOAD SAVED MODE

if(localStorage.getItem('theme') === 'dark'){

    document.body.classList.add('dark-mode');
}