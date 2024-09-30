document.addEventListener('DOMContentLoaded', function () {
    var quotes = [
        "Будь успішним",
        "Будь талановитим",
        "Будь впливовим",
        "Будь спритним",
        "Будь винахідливим",
        "Будь вмілим",
        "Будь надійним",
        "Будь цілеспрямованим",
        "Будь відданим",
        "Будь енергійним",
        "Будь стратегічним",
        "Будь креативним",
        "Будь врівноваженим",
        "Будь сильним",
        "Будь допитливим",
        "Будь дисциплінованим",
        "Будь амбіційним",
        "Будь рішучим"
        // ... Додайте решту цитат тут
    ];

    var options = {
        strings: quotes,
        typeSpeed: 50,
        backSpeed: 10,
        backDelay: 2100,
        startDelay: 0,
        loop: true,
        showCursor: false,
    };
    var typed = new Typed('#quote-container', options);


});