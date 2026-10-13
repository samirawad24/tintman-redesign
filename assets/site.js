(function () {
  var d = document;
  d.documentElement.classList.add('js');

  // mobile menu
  var menu = d.querySelector('.menu'), nav = d.querySelector('.nav');
  if (menu && nav) {
    menu.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      menu.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // reveal on scroll
  var rv = d.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    rv.forEach(function (el) { io.observe(el); });
  } else {
    rv.forEach(function (el) { el.classList.add('in'); });
  }

  // gallery lightbox
  var dlg = d.querySelector('#lightbox');
  if (dlg && dlg.showModal) {
    var big = dlg.querySelector('img');
    d.querySelectorAll('.gal a').forEach(function (a) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        big.src = a.href;
        big.alt = a.querySelector('img').alt;
        dlg.showModal();
      });
    });
    dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
  }

  // locations map
  var frame = d.querySelector('#map');
  if (frame) {
    d.querySelectorAll('[data-map]').forEach(function (b) {
      b.addEventListener('click', function () {
        frame.src = 'https://www.google.com/maps?q=' + encodeURIComponent(b.getAttribute('data-map')) + '&output=embed';
        d.querySelector('#map-name').textContent = b.getAttribute('data-name');
        if (window.matchMedia('(max-width:900px)').matches) frame.scrollIntoView({ block: 'center' });
      });
    });
  }

  // price builder
  var form = d.querySelector('#price-form');
  if (form) {
    var P = window.TM_PRICES, SHOPS = window.TM_SHOPS;
    var VEH = { car: 'Coupe or sedan', truck: 'Truck', suv: 'SUV' };
    var FILM = { cs: 'CS', xr: 'XR ceramic', xrp: 'XR Plus ceramic' };
    var out = d.querySelector('#q-total'), list = d.querySelector('#q-lines'),
        call = d.querySelector('#q-call'), mail = d.querySelector('#q-mail'), shopSel = d.querySelector('#q-shop');
    var money = function (n) { return '$' + n.toLocaleString('en-US'); };

    function calc() {
      var f = new FormData(form);
      var v = f.get('vehicle'), film = f.get('film'), ws = f.get('windshield');
      var doors = parseInt(f.get('rm-doors'), 10) || 0, rear = f.get('rm-rear') === 'on';
      var lines = [[VEH[v] + ', ' + FILM[film] + ' film', P.base[v][film]]];
      if (ws === 'visor') lines.push(['Visor strip', P.visor[film]]);
      if (ws === 'full') lines.push(['Whole windshield', P.windshield[film]]);
      if (doors) lines.push(['Old tint removal, ' + doors + (doors === 1 ? ' door' : ' doors'), doors * P.removeDoor]);
      if (rear) lines.push(['Old tint removal, rear window', P.removeRear]);
      var total = lines.reduce(function (s, l) { return s + l[1]; }, 0);
      out.textContent = money(total);
      list.innerHTML = '';
      lines.forEach(function (l) {
        var li = d.createElement('li'), a = d.createElement('span'), b = d.createElement('b');
        a.textContent = l[0]; b.textContent = money(l[1]); li.appendChild(a); li.appendChild(b); list.appendChild(li);
      });
      var shop = SHOPS[parseInt(shopSel.value, 10)];
      call.textContent = 'Call ' + shop.name + ' ' + shop.phone;
      call.href = 'tel:+1' + shop.phone.replace(/\D/g, '');
      var body = 'Hi, I priced a tint job on your site.\n\n' +
        lines.map(function (l) { return l[0] + ': ' + money(l[1]); }).join('\n') +
        '\nEstimate before tax: ' + money(total) +
        '\nShop: ' + shop.name + '\n\nMy vehicle (year, make, model): \nBest day for me: \nMy phone: ';
      mail.href = 'mailto:tintmanfl@yahoo.com?subject=' + encodeURIComponent('Tint quote, ' + shop.name) + '&body=' + encodeURIComponent(body);
    }
    form.addEventListener('change', calc);
    form.addEventListener('submit', function (e) { e.preventDefault(); });
    calc();
  }
})();
