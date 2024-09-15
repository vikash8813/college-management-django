document.querySelector("#scroll-container").addEventListener('mouseover', function () {
    document.querySelector("#scroll-text").style.animationPlayState = 'paused';
});

document.querySelector("#scroll-container").addEventListener('mouseout', function () {
    document.querySelector("#scroll-text").style.animationPlayState = 'running';
});