/**
 * Al Sadat Builders — Main JavaScript
 * Handles navigation, mobile menu, lead form submission to WhatsApp, counter animations, and scroll animations.
 */

document.addEventListener('DOMContentLoaded', () => {
  // --- Mobile Menu Toggle ---
  const hamburger = document.querySelector('.hamburger');
  const mobileNav = document.querySelector('.mobile-nav');
  const mobileNavClose = document.querySelector('.mobile-nav-close');

  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('open');
      mobileNav.classList.toggle('open');
      document.body.style.overflow = mobileNav.classList.contains('open') ? 'hidden' : '';
    });

    if (mobileNavClose) {
      mobileNavClose.addEventListener('click', () => {
        hamburger.classList.remove('open');
        mobileNav.classList.remove('open');
        document.body.style.overflow = '';
      });
    }

    // Close when clicking mobile nav links
    const mobileLinks = mobileNav.querySelectorAll('a');
    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('open');
        mobileNav.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  // --- Highlight Active Nav Link (Supports Clean URLs & .html) ---
  const rawPath = window.location.pathname.replace(/\/$/, '').replace(/\.html$/, '').split('/').pop() || '';
  document.querySelectorAll('.nav a, .mobile-nav-links a').forEach(link => {
    const rawHref = (link.getAttribute('href') || '').split('?')[0].split('#')[0];
    const cleanHref = rawHref.replace(/^\//, '').replace(/\/$/, '').replace(/\.html$/, '');

    if (
      (rawPath === '' && (cleanHref === '' || cleanHref === 'index')) ||
      (rawPath !== '' && cleanHref === rawPath)
    ) {
      link.classList.add('active');
    }
  });

  // --- Lead Forms Handling (WhatsApp Direct Integration) ---
  const leadForms = document.querySelectorAll('form[data-lead-form]');
  leadForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const name = form.querySelector('[name="name"]')?.value || 'Client';
      const phone = form.querySelector('[name="phone"]')?.value || 'Not provided';
      const location = form.querySelector('[name="location"]')?.value || 'Islamabad/Rawalpindi/Bani Gala';
      const plotSize = form.querySelector('[name="plot_size"]')?.value || 'Not specified';
      const service = form.querySelector('[name="service"]')?.value || 'General Construction';
      const message = form.querySelector('[name="message"]')?.value || 'Looking for project quote & site visit.';

      const whatsappText = `*New Construction Inquiry - Al Sadat Builders*\n` +
        `------------------------------------\n` +
        `👤 *Name:* ${name}\n` +
        `📞 *Phone / WhatsApp:* ${phone}\n` +
        `📍 *Location / Society:* ${location}\n` +
        `📐 *Plot Size:* ${plotSize}\n` +
        `🏗️ *Service Required:* ${service}\n` +
        `💬 *Message / Details:* ${message}\n` +
        `------------------------------------\n` +
        `Sent via Al Sadat Builders Website`;

      const whatsappUrl = `https://wa.me/923469607349?text=${encodeURIComponent(whatsappText)}`;

      // Show success message if element exists
      const successMsg = form.querySelector('.success-msg') || form.parentElement.querySelector('.success-msg');
      if (successMsg) {
        successMsg.style.display = 'block';
        successMsg.textContent = 'Redirecting to WhatsApp with your project details...';
      }

      // Open WhatsApp in new tab
      window.open(whatsappUrl, '_blank');

      // Reset form after short delay
      setTimeout(() => {
        form.reset();
        if (successMsg) {
          successMsg.textContent = 'Thank you! Our engineering team will contact you shortly.';
        }
      }, 1200);
    });
  });

  // --- Number Counter Animation ---
  const animateCounter = (el) => {
    const text = el.innerText.trim();
    const match = text.match(/(\d+)(\+?%?)/);
    if (!match) return;

    const target = parseInt(match[1], 10);
    const suffix = match[2] || '';
    let count = 0;
    const duration = 1200; // ms
    const stepTime = Math.max(Math.floor(duration / target), 20);

    const timer = setInterval(() => {
      count += Math.ceil(target / (duration / stepTime));
      if (count >= target) {
        el.innerText = target + suffix;
        clearInterval(timer);
      } else {
        el.innerText = count + suffix;
      }
    }, stepTime);
  };

  // --- Scroll Animations (IntersectionObserver) ---
  const animatedElements = document.querySelectorAll('.animate-on-scroll');
  if ('IntersectionObserver' in window && animatedElements.length > 0) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');

          // Trigger number counter if contains stat
          entry.target.querySelectorAll('.stat-num, .num').forEach(numEl => {
            if (!numEl.dataset.animated) {
              numEl.dataset.animated = 'true';
              animateCounter(numEl);
            }
          });

          obs.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.05,
      rootMargin: '0px 0px -20px 0px'
    });

    animatedElements.forEach(el => {
      // Check if already in viewport on load
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom > 0) {
        el.classList.add('visible');
        el.querySelectorAll('.stat-num, .num').forEach(numEl => {
          if (!numEl.dataset.animated) {
            numEl.dataset.animated = 'true';
            animateCounter(numEl);
          }
        });
      } else {
        observer.observe(el);
      }
    });
  } else {
    // Fallback if IntersectionObserver not supported
    animatedElements.forEach(el => el.classList.add('visible'));
  }

  // --- Smooth Anchor Scrolling ---
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId.length > 1) {
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          e.preventDefault();
          targetElement.scrollIntoView({
            behavior: 'smooth'
          });
        }
      }
    });
  });
});
