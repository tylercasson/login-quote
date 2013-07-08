Login Quote is a simple script that changes the message on the Mac OS X login screen. If you need some motivation to get started on your work, this helps by randomly selecting a motivational quote and displaying it right before you login.

**Note: This script was designed to be run as root.**

## How To Get Started

- Add this script as a cron job as root. (This example runs every hour)
```console
sh-3.2# crontab -e
```
This will open a vim editor. Add a line similar to the one below, then save and exit.
```console
0 * * * * /usr/bin/python <ABSOLUTE PATH>/Login\ Quote/quote.py
~
~
~
"/tmp/crontab.C4QuaYgUjs" 1L, 80C
```
If your cron job had no errors, your console should look like this after exiting:
```console
sh-3.2# crontab -e
crontab: installing new crontab
sh-3.2#
```  

If all went well, your Mac will automatically change the quote on your login screen every hour. Feel free to experiment and have a productive day.

## Contact

Follow me on Twitter [@tgcasson](https://twitter.com/tgcasson)

### Creators

[Tyler Casson](http://tylercasson.com)
[@tgcasson](https://twitter.com/tgcasson)

## License

Login Quote is available under the GNU General Public License. See the LICENSE file for more info.
