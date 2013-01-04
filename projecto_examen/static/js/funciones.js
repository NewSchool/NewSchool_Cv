$(document).on("ready", contructor);
  function contructor () {
    $.vegas('slideshow', {
      delay:8000,
      backgrounds:[
        { src:'../../static/img/slider/1.jpg', fade:4000 },
        { src:'../../static/img/slider/2.jpg', fade:4000 },
        { src:'../../static/img/slider/3.jpg', fade:4000 }
      ]
    })('overlay', {
      src:'../../static/overlays/11.png'
    });
  }