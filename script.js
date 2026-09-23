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

// ===== Contact Form (Formspree async submit + mailto fallback) =====
var contactForm = document.getElementById('contact-form');
if (contactForm) {
  var formAction = contactForm.getAttribute('action') || '';
  var isFormspree = formAction.indexOf('formspree.io') !== -1;
  var feedback = document.getElementById('form-feedback');

  function showFeedback(msg, type) {
    if (!feedback) return;
    feedback.textContent = msg;
    feedback.className = 'form-feedback ' + (type || '');
  }

  function mailtoFallback(form) {
    var name = form.querySelector('#name').value;
    var email = form.querySelector('#email').value;
    var company = form.querySelector('#company') ? form.querySelector('#company').value || 'N/A' : 'N/A';
    var message = form.querySelector('#message').value;
    var subject = 'Inquiry from ' + name + (company !== 'N/A' ? ' (' + company + ')' : '');
    var body = 'Name: ' + name + '\nEmail: ' + email + '\nCompany: ' + company + '\n\nMessage:\n' + message;
    window.location.href = 'mailto:info@vetzora.cn?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
  }

  contactForm.addEventListener('submit', function(e) {
    if (!isFormspree) {
      e.preventDefault();
      mailtoFallback(contactForm);
      return;
    }
    e.preventDefault();
    var btn = contactForm.querySelector('button[type="submit"]');
    if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }
    showFeedback('', '');

    fetch(formAction, {
      method: 'POST',
      body: new FormData(contactForm),
      headers: { 'Accept': 'application/json' }
    }).then(function(response) {
      if (response.ok) {
        contactForm.reset();
        showFeedback('Thanks! Your message has been sent. We will get back to you shortly.', 'success');
      } else {
        response.json().then(function(data) {
          var msg = data && data.errors ? data.errors.map(function(err){ return err.message; }).join(', ') : 'Something went wrong. Please try again or email us directly at info@vetzora.cn.';
          showFeedback(msg, 'error');
        }).catch(function() {
          showFeedback('Something went wrong. Please try again or email us directly at info@vetzora.cn.', 'error');
        });
      }
    }).catch(function() {
      // Network error -> degrade to mailto
      mailtoFallback(contactForm);
      if (btn) { btn.disabled = false; btn.textContent = 'Send Message'; }
    }).finally(function() {
      if (btn && !contactForm.querySelector('#form-feedback').textContent.includes('sent')) {
        btn.disabled = false; btn.textContent = 'Send Message';
      }
    });
  });
}
