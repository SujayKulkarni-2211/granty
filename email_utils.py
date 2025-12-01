# email_utils.py - RESEND API VERSION (WORKS ON RENDER)
import os
import secrets
from datetime import datetime, timedelta
from threading import Thread
import logging

# Use Resend API instead of SMTP
import resend

# Configure Resend
RESEND_API_KEY = os.getenv('RESEND_API_KEY')
RESEND_FROM_EMAIL = os.getenv('RESEND_FROM_EMAIL', 'onboarding@resend.dev')
REPLY_TO_EMAIL = os.getenv('EMAIL_ADDRESS', 'mailbot.granty@gmail.com')

if RESEND_API_KEY:
    resend.api_key = RESEND_API_KEY
    print(f"✓ Resend configured with from: {RESEND_FROM_EMAIL}, reply-to: {REPLY_TO_EMAIL}")
else:
    print("⚠️ RESEND_API_KEY not configured")

def generate_verification_token():
    """Generate a secure verification token"""
    return secrets.token_urlsafe(32)

def send_email_async(send_function, *args, **kwargs):
    """Send email in background thread to prevent worker timeouts"""
    def _send():
        try:
            result = send_function(*args, **kwargs)
            if result:
                logging.info(f"Email sent successfully")
            else:
                logging.error(f"Email send returned False")
        except Exception as e:
            logging.error(f"Email send failed: {e}")
    
    thread = Thread(target=_send)
    thread.daemon = True
    thread.start()
    logging.info("Email queued for sending in background")

def send_verification_email(user_email, user_name, verification_token, app_url):
    """Send verification email to user via Resend API"""
    try:
        # Check if Resend is configured
        if not RESEND_API_KEY:
            print("Resend API not configured - skipping email send")
            return False
            
        # Verification URL
        verification_url = f"{app_url}/verify-email/{verification_token}"

        # HTML email template
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verify Your Email</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background: #f4f4f4;">
    <div style="max-width: 600px; margin: 0 auto; background: linear-gradient(to bottom, #0f0c29, #302b63, #24243e); padding: 20px;">
        <div style="text-align: center; padding: 20px 0; border-bottom: 2px solid rgba(76, 201, 240, 0.3);">
            <h1 style="color:white;">grant<span style="color:#4cc9f0;">Y</span></h1>
            <p style="color: #7f8c8d; margin: 5px 0 0 0;">Grant Writing Made Easy</p>
        </div>
        
        <div style="padding: 30px 0;">
            <h2 style="color: white">Welcome to Granty, {user_name}!</h2>
            
            <p style="color: white; line-height: 1.6; font-size: 16px;">
                Thank you for creating an account with Granty. To get started and access all features, 
                please verify your email address by clicking the button below.
            </p>
            
            <div style="text-align: center; margin: 30px 0;">
                <a href="{verification_url}" 
                   style="background-color: #3498db; color: white; padding: 15px 30px; 
                          text-decoration: none; border-radius: 5px; font-weight: bold; 
                          display: inline-block; font-size: 16px;">
                    Verify Email Address
                </a>
            </div>
            
            <p style="color: white; font-size: 14px; line-height: 1.5;">
                If the button doesn't work, copy and paste this link into your browser:
                <br><a href="{verification_url}" style="color: #3498db;">{verification_url}</a>
            </p>
            
            <p style="color: white; font-size: 14px;">
                This verification link will expire in 24 hours for security reasons.
            </p>
        </div>
        
        <div style="border-top: 1px solid #eee; padding-top: 20px; text-align: center;">
            <p style="color: #999; font-size: 12px; margin: 0;">
                This email was sent by Granty. If you didn't create an account, please ignore this email.
            </p>
        </div>
    </div>
</body>
</html>"""

        # Plain text version
        text_content = f"""Welcome to Granty, {user_name}!

Thank you for creating an account with Granty. To get started and access all features, 
please verify your email address by visiting the following link:

{verification_url}

If you can't click the link, copy and paste it into your browser.

This verification link will expire in 24 hours for security reasons.

If you didn't create an account, please ignore this email.

Best regards,
The Granty Team"""

        # Send via Resend API
        params = {
            "from": RESEND_FROM_EMAIL,
            "to": [user_email],
            "subject": "Verify Your Granty Account",
            "html": html_content,
            "text": text_content,
            "reply_to": REPLY_TO_EMAIL
        }
        
        print(f"Sending verification email via Resend to {user_email}")
        email = resend.Emails.send(params)
        
        print(f"✓ Verification email sent to {user_email} via Resend (ID: {email.get('id')})")
        return True
        
    except Exception as e:
        print(f"❌ Error sending verification email via Resend: {e}")
        import traceback
        traceback.print_exc()
        return False

def send_welcome_email(user_email, user_name):
    """Send welcome email after successful verification via Resend API"""
    try:
        # Check if Resend is configured
        if not RESEND_API_KEY:
            print("Resend API not configured - skipping email send")
            return False

        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Granty</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background: #f4f4f4;">
    <div style="max-width: 600px; margin: 0 auto; background: linear-gradient(to bottom, #0f0c29, #302b63, #24243e); padding: 20px;">
        <div style="text-align: center; padding: 20px 0; border-bottom: 2px solid rgba(76, 201, 240, 0.3);">
            <h1 style="color:white;">grant<span style="color:#4cc9f0;">Y</span></h1>
            <p style="color: #7f8c8d; margin: 5px 0 0 0;">Grant Writing Made Easy</p>
        </div>
        
        <div style="padding: 30px 0;">
            <h2 style="color: #27ae60;">🎉 Account Verified Successfully!</h2>
            
            <p style="color: white; line-height: 1.6; font-size: 16px;">
                Hi {user_name},
            </p>
            
            <p style="color: white; line-height: 1.6; font-size: 16px;">
                Congratulations! Your email has been verified and your Granty account is now fully active. 
                You can now access all features and start creating professional grant proposals.
            </p>
            
            <div style="background-color: #ecf0f1; padding: 20px; border-radius: 8px; margin: 20px 0;">
                <h3 style="color: #2c3e50; margin-top: 0;">What you can do now:</h3>
                <ul style="color: #555; line-height: 1.6;">
                    <li>Create grant proposals using our professional templates</li>
                    <li>Upload custom templates and get AI-powered assistance</li>
                    <li>Generate comprehensive proposals with AI</li>
                    <li>Download your proposals as PDF documents</li>
                    <li>Find funding opportunities relevant to your projects</li>
                </ul>
            </div>
            
            <div style="text-align: center; margin: 30px 0;">
                <a href="{os.getenv('APP_URL', 'http://localhost:5000')}/dashboard" 
                   style="background-color: #27ae60; color: white; padding: 15px 30px; 
                          text-decoration: none; border-radius: 5px; font-weight: bold; 
                          display: inline-block; font-size: 16px;">
                    Go to Dashboard
                </a>
            </div>
        </div>
        
        <div style="border-top: 1px solid #eee; padding-top: 20px; text-align: center;">
            <p style="color: #999; font-size: 12px; margin: 0;">
                Thank you for choosing Granty for your grant writing needs!
            </p>
        </div>
    </div>
</body>
</html>"""

        text_content = f"""Account Verified Successfully!

Hi {user_name},

Congratulations! Your email has been verified and your Granty account is now fully active.
You can now access all features and start creating professional grant proposals.

Visit your dashboard: {os.getenv('APP_URL', 'http://localhost:5000')}/dashboard

Thank you for choosing Granty!

Best regards,
The Granty Team"""

        # Send via Resend API
        params = {
            "from": RESEND_FROM_EMAIL,
            "to": [user_email],
            "subject": "Welcome to Granty - Your Account is Verified!",
            "html": html_content,
            "text": text_content,
            "reply_to": REPLY_TO_EMAIL
        }
        
        print(f"Sending welcome email via Resend to {user_email}")
        email = resend.Emails.send(params)
        
        print(f"✓ Welcome email sent to {user_email} via Resend (ID: {email.get('id')})")
        return True
        
    except Exception as e:
        print(f"❌ Error sending welcome email via Resend: {e}")
        import traceback
        traceback.print_exc()
        return False
