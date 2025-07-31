# Security Review – HTTPS and Secure Headers

1. All HTTP traffic is redirected to HTTPS using `SECURE_SSL_REDIRECT`.
2. HTTP Strict Transport Security (HSTS) is enforced for one year with preload and subdomain inclusion.
3. Cookies are secured using `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` to prevent transmission over non-HTTPS.
4. The application is protected from:
   - Clickjacking (`X_FRAME_OPTIONS = 'DENY'`)
   - MIME-sniffing (`SECURE_CONTENT_TYPE_NOSNIFF = True`)
   - Basic XSS attacks (`SECURE_BROWSER_XSS_FILTER = True`)
5. Deployment includes Nginx configured with SSL.
6. These settings collectively protect sensitive data from MITM (Man-in-the-middle), session hijacking, and injection attacks.
 
