# Locales on Linux

**Locales (i18n)** defines language and country specific setting for your programs and shell session. You can use locales to see date, time, number, currency and other values formatted as per your country or language on a Linux or Unix-like system.

# Environment variables

Different aspects of localisations (like the thousand separator or decimal point character, character set, sorting order, month, day names, language or application messages like error messages, currency symbol) can be set using a few environment variables.

## Precedence

- `LANG` identifies your region.
- The individual `LC_xxx` variables override `LANG`.
- `LC_ALL` overrides all the other localisation settings.

## Format

`fr_CH.UTF-8` means you're in French speaking Switzerland, using UTF-8

## C locale

The C locale is a special locale that is meant to be the simplest locale. The C locale is for computers. In the C locale, characters are single bytes, the charset is ASCII (well, is not required to, but in practice will be in the systems most of us will ever get to use), the sorting order is based on the byte values, the language is usually US English (though for application messages (as opposed to things like month or day names or messages by system libraries), it's at the discretion of the application author) and things like currency symbols are not defined.

You generally run a command with `LC_ALL=C` to avoid the user's settings to interfere with your script.

# Commands to display

## To view the summary of the current locale settings

    $ locale
    LANG=en_GB.UTF-8
    LANGUAGE=
    LC_CTYPE="en_GB.UTF-8"
    LC_NUMERIC="en_GB.UTF-8"
    LC_TIME="en_GB.UTF-8"
    LC_COLLATE="en_GB.UTF-8"
    LC_MONETARY="en_GB.UTF-8"
    LC_MESSAGES="en_GB.UTF-8"
    LC_PAPER="en_GB.UTF-8"
    LC_NAME="en_GB.UTF-8"
    LC_ADDRESS="en_GB.UTF-8"
    LC_TELEPHONE="en_GB.UTF-8"
    LC_MEASUREMENT="en_GB.UTF-8"
    LC_IDENTIFICATION="en_GB.UTF-8"
    LC_ALL=

## To view one locale setting

    $ locale LC_NUMERIC
    .
    ,
    3;3

## To display the name of the category

    $ locale -c LC_NUMERIC
    LC_NUMERIC
    .
    ,
    3;3

## To list the category names

    $ locale -k LC_NUMERIC
    decimal_point="."
    thousands_sep=","
    grouping="3;3"

## To combine the above

    $ locale -c -k LC_NUMERIC
    LC_NUMERIC
    decimal_point="."
    thousands_sep=","
    grouping="3;3"

## To display all available locales

    $ locale -a
    ko_KR.UTF-8
    en_US.UTF-8
    ...
    C
    POSIX

# Commands to set

## View/set locale for one user

    $ vi ~/.bash_profile

## View/set global locale for all users (on a Ubuntu)

To set the locales for all users, enter:

    $ sudo locale-gen en_IN
    $ sudo locale-gen en_IN.UTF-8

Finally run:

    $ sudo update-locale

## View/set global locale for all users (on a CentOS 6.x)

    $ sudo vi /etc/sysconfig/i18n

You can also edit `/etc/profile` and set global locale for all users:

## View/set global locale for all users (on a CentOS 7.x)

Type the following command to see the current locale for all users:

    $ cat /etc/locale.conf

You can use the following systemd command too:

    $ localectl status

To see all locales available, run:

    $ localectl list-locales

To set the default global system locale for all users, type the following command as root:

    $ sudo localectl set-locale LANG=localeValueHere
    $ sudo localectl set-locale LANG=en_IN.UTF-8

# Reference

[](https://unix.stackexchange.com/questions/87745/what-does-lc-all-c-do)

[](https://www.cyberciti.biz/faq/how-to-set-locales-i18n-on-a-linux-unix/)

[](https://www.ibm.com/support/knowledgecenter/en/SSPREK_7.0.0/com.ibm.isam.doc_70/gsk_capicmd_user19.htm)