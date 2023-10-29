#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from dotenv import load_dotenv

def save_textfile(data, outfile):
    with open(outfile, 'a') as f_txt:
        print(data, file=f_txt)


def main():
    """Run administrative tasks."""
    # If WEBSITE_HOSTNAME is defined as an environment variable, then we're running on Azure App Service

    print('WEBSITE_HOSTNAME: ')
    print(os.environ.get('WEBSITE_HOSTNAME'))
    tmp = os.environ.get('WEBSITE_HOSTNAME')
    save_textfile(tmp,'/home/output.log')

    # Only for Local Development - Load environment variables from the .env file
    if 'WEBSITE_HOSTNAME' not in os.environ:
        print("Loading environment variables for .env file")
        load_dotenv('./.env')

    # When running on Azure App Service you should use the production settings.
    settings_module = "weddo.production" if 'WEBSITE_HOSTNAME' in os.environ else 'weddo.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
