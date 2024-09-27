document.addEventListener('DOMContentLoaded', function() {
  // Check if the user has a cookie-consent cookie set
  if (document.cookie.indexOf('cookie-consent=accepted') > -1) {
    // If it is, hide the cookie banner
    document.getElementById('cookie-banner').style.display = 'none';
  } else {
    // If it isn't, show the cookie banner
    document.getElementById('cookie-banner').style.display = 'flex';
    document.getElementById('cookie-consent').addEventListener('click', function() {
      // Fade out the cookie banner when the button is clicked
      setTimeout(function() {
        document.getElementById('cookie-banner').style.opacity = '0';
      }, 600);
      // Set a cookie that expires in a year
      document.cookie = 'cookie-consent=accepted; max-age=31536000';
    });

    localStorage.setItem("consentGranted", "true");
    function gtag() { dataLayer.push(arguments); }

    gtag('consent', 'update', {
      ad_user_data: 'granted',
      ad_personalization: 'granted',
      ad_storage: 'granted',
      analytics_storage: 'granted',
      ad_user_data: 'granted',
      ad_personalization: 'granted',
    });
  }

    // Load gtag.js script.
    var gtagScript = document.createElement('script');
    gtagScript.async = true;
    gtagScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-GP5DC9YBBD';  
    var firstScript = document.getElementsByTagName('script')[0];
    firstScript.parentNode.insertBefore(gtagScript,firstScript);
});

