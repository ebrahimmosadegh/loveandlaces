var swiper = new Swiper('.swiper-container', {
    loop: true,
    effect: 'fade',
    autoplay: {
      delay: 4000,
      disableOnInteraction: true,
  },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
      type: 'fraction',
    renderFraction: function (currentClass, totalClass) {
      return '<span class="' + currentClass + '"></span>' +
      '<span class="border-fraction"></span>' +
              '<span class="' + totalClass + '"></span>';
  }
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });

