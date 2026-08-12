// ===== Header Scroll Effect =====
var header = document.getElementById('header');
if (header && !header.classList.contains('always-solid')) {
  window.addEventListener('scroll', function() {
    if (window.scrollY > 60) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });
}

// ===== Mobile Menu Toggle =====
var menuToggle = document.getElementById('menu-toggle');
var navLinks = document.getElementById('nav-links');
if (menuToggle && navLinks) {
  menuToggle.addEventListener('click', function() {
    navLinks.classList.toggle('active');
  });
  navLinks.querySelectorAll('a').forEach(function(link) {
    link.addEventListener('click', function() {
      navLinks.classList.remove('active');
    });
  });
}

// ===== Scroll Reveal =====
var revealObserver = new IntersectionObserver(function(entries) {
  entries.forEach(function(entry) {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });
document.querySelectorAll('.reveal').forEach(function(el) { revealObserver.observe(el); });

// ===== Scroll to Top =====
var scrollTopBtn = document.getElementById('scroll-top');
if (scrollTopBtn) {
  window.addEventListener('scroll', function() {
    if (window.scrollY > 500) {
      scrollTopBtn.classList.add('visible');
    } else {
      scrollTopBtn.classList.remove('visible');
    }
  });
  scrollTopBtn.addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

// ===== FAQ Accordion =====
document.querySelectorAll('.faq-question').forEach(function(q) {
  q.addEventListener('click', function() {
    var item = q.parentElement;
    var wasActive = item.classList.contains('active');
    document.querySelectorAll('.faq-item').forEach(function(f) { f.classList.remove('active'); });
    if (!wasActive) {
      item.classList.add('active');
    }
  });
});

// ===== Contact Form (mailto fallback) =====
var contactForm = document.getElementById('contact-form');
if (contactForm && contactForm.getAttribute('action').indexOf('formspree') === -1) {
  contactForm.addEventListener('submit', function(e) {
    e.preventDefault();
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var company = document.getElementById('company') ? document.getElementById('company').value || 'N/A' : 'N/A';
    var message = document.getElementById('message').value;

    var subject = 'Inquiry from ' + name + (company !== 'N/A' ? ' (' + company + ')' : '');
    var body = 'Name: ' + name + '\nEmail: ' + email + '\nCompany: ' + company + '\n\nMessage:\n' + message;

    window.location.href = 'mailto:info@vetzora.cn?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
  });
}
