let next = document.querySelector('.next')
let prev = document.querySelector('.prev')

next.addEventListener('click', function(){
    let items = document.querySelectorAll('.item')
    document.querySelector('.slide').appendChild(items[0])
})

prev.addEventListener('click', function(){
    let items = document.querySelectorAll('.item')
    document.querySelector('.slide').prepend(items[items.length - 1])
})

function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    const sectionTop = section.offsetTop;
    const sectionHeight = section.offsetHeight;
    const windowHeight = window.innerHeight;
    const scrollPosition = sectionTop - (windowHeight / 2) + (sectionHeight / 2);
    
    window.scrollTo({
        top: scrollPosition,
        behavior: 'smooth'
    });
}

