# from jinja2 import Template

from colibris import email
from colibris import template


def notify_customer_on_sign_up(*, tel, name):
    # email_content = template.render('notify.html')
    # email_content = template.render_string('knalkdsbdnfb')

    msg = email.EmailMessage('Owner created with name={} and tel={}'.format(name, tel),
                             body='owner created', to=['david.luca1996@gmail.com'])
    email.send(msg)
